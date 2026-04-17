from __future__ import annotations

import json
import os
import re
import unicodedata
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

TECHNIQUE_ROOT = Path(__file__).resolve().parent
ROOT = TECHNIQUE_ROOT.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from TECHNIQUE.vector_memory import VectorMemory


DEFAULT_ALLOWED_LAYERS = ("CANON", "RAG_SUPPORT")
SUPPORTED_EXTENSIONS = {".md", ".json", ".txt"}


class IngestionPipeline:
    def __init__(
        self,
        memory: VectorMemory,
        chunk_size: int = 1200,
        overlap: int = 150,
        allowed_layers: Optional[List[str]] = None,
    ):
        self.memory = memory
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.allowed_layers = set(allowed_layers or DEFAULT_ALLOWED_LAYERS)

        # Keep the retrieval surface small and explicit.
        self.excluded_dirs = {
            ".git",
            ".github",
            ".obsidian",
            "__pycache__",
            "node_modules",
            "venv",
            ".venv",
            "ARCHIVES",
            "TECHNIQUE",
        }

        self.max_file_size = 300_000

    def _slugify(self, value: str) -> str:
        normalized = unicodedata.normalize("NFKD", value)
        ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
        slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_value).strip("-")
        return slug.upper() if slug else "ROOT"

    def _extract_section_id(self, text: str) -> str:
        body = self._strip_frontmatter(text)
        for line in body.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                heading = stripped.lstrip("#").strip()
                if heading:
                    return self._slugify(heading)
        return "ROOT"

    def _document_role(self, relative_path: str, layer: str) -> str:
        lower = relative_path.lower()
        if lower.endswith("readme.md"):
            return "navigation"
        if "00_registre_autorite" in lower:
            return "registry"
        if layer == "RAG_SUPPORT":
            return "support"
        return "canonical"

    def _default_retrieval_weight(self, layer: str, document_role: str, relative_path: str) -> float:
        weight = 1.0 if layer == "CANON" else 0.92
        if document_role == "navigation":
            weight *= 0.28
        elif document_role == "registry":
            weight *= 0.52
        elif document_role == "support":
            weight *= 0.96

        if "index" in relative_path.lower():
            weight *= 0.86

        return round(weight, 3)

    def clean_text(self, text: str) -> str:
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def chunk_text(self, text: str) -> List[str]:
        text = self.clean_text(text)
        if not text:
            return []

        paragraphs = [part.strip() for part in re.split(r"\n{2,}", text) if part.strip()]
        chunks: List[str] = []
        current = ""

        for paragraph in paragraphs:
            if not current:
                current = paragraph
                continue

            candidate = f"{current}\n\n{paragraph}"
            if len(candidate) <= self.chunk_size:
                current = candidate
                continue

            chunks.append(current)
            current = paragraph

            while len(current) > self.chunk_size:
                split_at = current.rfind("\n", 0, self.chunk_size)
                if split_at < self.chunk_size // 2:
                    split_at = current.rfind(" ", 0, self.chunk_size)
                if split_at < self.chunk_size // 2:
                    split_at = self.chunk_size
                chunks.append(current[:split_at].strip())
                current = current[split_at:].strip()

        if current:
            chunks.append(current)

        return [chunk for chunk in chunks if len(chunk) > 40]

    def _detect_layer(self, relative_path: str) -> Optional[str]:
        parts = Path(relative_path).parts
        if not parts:
            return None
        layer = parts[0]
        return layer if layer in self.allowed_layers else None

    def _parse_frontmatter(self, text: str) -> Dict[str, str]:
        metadata: Dict[str, str] = {}
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return metadata

        for line in lines[1:]:
            stripped = line.strip()
            if stripped == "---":
                break
            if ":" not in stripped:
                continue
            key, value = stripped.split(":", 1)
            metadata[key.strip().lower()] = value.strip().strip('"').strip("'")
        return metadata

    def _strip_frontmatter(self, text: str) -> str:
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return text

        for index, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                return "\n".join(lines[index + 1 :]).strip()

        return text

    def _build_metadata(
        self,
        relative_path: str,
        content: str,
        chunk_index: int,
        layer_hint: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        layer = layer_hint or self._detect_layer(relative_path)
        if layer is None:
            return None

        parsed = self._parse_frontmatter(content)
        canonical_id = parsed.get("canonical_id")
        if not canonical_id:
            return None

        section_id = self._extract_section_id(content)
        document_role = parsed.get("document_role", self._document_role(relative_path, layer)).lower()
        status = parsed.get("status", "canonical" if layer == "CANON" else "support").lower()
        citation_id = parsed.get("citation_id") or canonical_id
        retrieval_weight = parsed.get("retrieval_weight")
        if retrieval_weight is None:
            retrieval_weight_value = self._default_retrieval_weight(layer, document_role, relative_path)
        else:
            try:
                retrieval_weight_value = round(float(retrieval_weight), 3)
            except (TypeError, ValueError):
                retrieval_weight_value = self._default_retrieval_weight(layer, document_role, relative_path)

        return {
            "source": relative_path,
            "layer": layer,
            "status": status,
            "canonical_id": canonical_id,
            "concept_id": parsed.get("concept_id", ""),
            "citation_id": citation_id,
            "section_id": section_id,
            "document_role": document_role,
            "retrieval_weight": retrieval_weight_value,
            "chunk": str(chunk_index),
        }

    def process_corpus(self, folder_path: str, layer_hint: Optional[str] = None):
        total_chunks = 0
        total_files = 0

        for root, dirs, files in os.walk(folder_path):
            dirs[:] = [d for d in dirs if d not in self.excluded_dirs]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext not in SUPPORTED_EXTENSIONS:
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                display_path = os.path.join(layer_hint, relative_path) if layer_hint else relative_path

                try:
                    with open(file_path, "r", encoding="utf-8", errors="strict") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    print(f"SKIP utf8-error: {relative_path}")
                    continue
                except Exception as e:
                    print(f"ERROR reading {relative_path}: {e}")
                    continue

                if len(content) > self.max_file_size:
                    print(f"SKIP too-large: {relative_path}")
                    continue

                metadata_template = self._build_metadata(display_path, content, 1, layer_hint=layer_hint)
                if metadata_template is None:
                    print(f"SKIP non-canonical-or-unregistered: {display_path}")
                    continue

                content_for_chunks = self._strip_frontmatter(content)
                chunks = self.chunk_text(content_for_chunks)
                if not chunks:
                    continue

                metadatas = []
                for index, _ in enumerate(chunks, start=1):
                    chunk_metadata = dict(metadata_template)
                    chunk_metadata["chunk"] = str(index)
                    metadatas.append(chunk_metadata)

                print(f"INGEST {display_path} -> {len(chunks)} chunks")
                self.memory.add_chunks(chunks, metadatas)
                total_chunks += len(chunks)
                total_files += 1

        print("\nINGESTION FINISHED")
        print(f"Files processed: {total_files}")
        print(f"Total chunks: {total_chunks}")

    def run(self, path: Optional[str] = None):
        base = Path(path) if path else ROOT

        if not base.exists():
            raise FileNotFoundError(f"Folder not found: {base}")

        print("Starting gated ingestion...\n")

        # Default behaviour: only the authoritative retrieval surface.
        if path is None:
            for layer in self.allowed_layers:
                layer_path = ROOT / layer
                if layer_path.exists():
                    self.process_corpus(str(layer_path), layer_hint=layer)
        else:
            self.process_corpus(str(base), layer_hint=base.name if base.name in self.allowed_layers else None)

        print("Done.")


if __name__ == "__main__":
    memory = VectorMemory()
    pipeline = IngestionPipeline(memory)

    pipeline.run()
    memory.save_to_json(str(TECHNIQUE_ROOT / "vector_memory.json"))
