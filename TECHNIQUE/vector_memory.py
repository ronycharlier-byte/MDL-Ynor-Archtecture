from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple
from collections import defaultdict

import numpy as np
from langchain_openai import OpenAIEmbeddings
from sklearn.feature_extraction.text import HashingVectorizer


class LocalHashingEmbeddings:
    def __init__(self, n_features: int = 1024):
        self.vectorizer = HashingVectorizer(
            n_features=n_features,
            alternate_sign=False,
            norm="l2",
            lowercase=True,
            ngram_range=(1, 2),
        )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        matrix = self.vectorizer.transform(texts)
        return matrix.toarray().astype(np.float32).tolist()

    def embed_query(self, text: str) -> List[float]:
        matrix = self.vectorizer.transform([text])
        return matrix.toarray()[0].astype(np.float32).tolist()


class VectorMemory:
    _STOPWORDS = {
        "the",
        "and",
        "or",
        "of",
        "to",
        "a",
        "an",
        "de",
        "du",
        "des",
        "la",
        "le",
        "les",
        "un",
        "une",
        "et",
        "ou",
        "en",
        "dans",
        "sur",
        "pour",
        "avec",
        "sans",
        "quel",
        "quelle",
        "quels",
        "quelles",
        "est",
        "sont",
        "role",
        "statut",
        "fonction",
    }

    def __init__(self, model: str = "text-embedding-3-small"):
        self.embedding_backend = "openai"
        self.embeddings_model = None
        try:
            candidate = OpenAIEmbeddings(model=model)
            # Probe once so an invalid API key falls back immediately.
            candidate.embed_query("vector-memory-probe")
            self.embeddings_model = candidate
        except Exception:
            self.embeddings_model = LocalHashingEmbeddings()
            self.embedding_backend = "local_hashing"
        self.vectors: List[np.ndarray] = []
        self.documents: List[str] = []
        self.metadata: List[Dict[str, Any]] = []

    def add_chunks(
        self,
        texts: List[str],
        metadatas: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        if not texts:
            return

        new_vectors = self.embeddings_model.embed_documents(texts)
        self.vectors.extend([np.array(v) for v in new_vectors])
        self.documents.extend(texts)

        if metadatas:
            self.metadata.extend(metadatas)
        else:
            self.metadata.extend([{} for _ in texts])

    def _cosine_similarity(self, v1: np.ndarray, v2: np.ndarray) -> float:
        dot_product = np.dot(v1, v2)
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)
        if norm_v1 == 0 or norm_v2 == 0:
            return 0.0
        return float(dot_product / (norm_v1 * norm_v2))

    def _normalize_text(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip().lower()

    def _tokenize(self, text: str) -> List[str]:
        tokens = re.findall(r"[a-z0-9_]+", self._normalize_text(text))
        return [token for token in tokens if len(token) > 2 and token not in self._STOPWORDS]

    def _query_alignment_bonus(self, query: str, text: str, meta: Dict[str, Any]) -> float:
        query_norm = self._normalize_text(query)
        text_norm = self._normalize_text(text)
        query_tokens = set(self._tokenize(query))
        if not query_tokens:
            return 1.0

        text_tokens = set(self._tokenize(text))
        overlap = len(query_tokens & text_tokens) / len(query_tokens)

        bonus = 1.0 + (0.55 * overlap)

        if query_norm and query_norm in text_norm:
            bonus += 0.2

        role = str(meta.get("document_role", "")).lower()
        layer = str(meta.get("layer", "")).upper()

        if role in {"support", "guide", "answer_card", "faq", "crosswalk"}:
            bonus += 0.10
        elif role in {"navigation", "registry"} and overlap < 0.2:
            bonus -= 0.05

        if layer == "CANON" and role == "answer_card":
            bonus += 0.02

        return max(0.5, min(bonus, 1.45))

    def _document_weight(self, meta: Dict[str, Any]) -> float:
        weight = meta.get("retrieval_weight", 1.0)
        try:
            weight_value = float(weight)
        except (TypeError, ValueError):
            weight_value = 1.0

        status = str(meta.get("status", "")).lower()
        document_role = str(meta.get("document_role", "")).lower()
        source = str(meta.get("source", "")).lower()
        layer = str(meta.get("layer", "")).upper()

        if status in {"archive", "quarantine", "derived"}:
            weight_value *= 0.05

        if document_role == "navigation" or source.endswith("readme.md"):
            weight_value *= 0.30
        elif document_role == "registry":
            weight_value *= 0.60
        elif document_role in {"support", "guide", "faq", "crosswalk"}:
            weight_value *= 1.08
        elif document_role == "answer_card" and layer == "CANON":
            weight_value *= 1.00

        if layer == "RAG_SUPPORT":
            weight_value *= 1.15

        return weight_value

    def search(
        self,
        query: str,
        top_k: int = 5,
        threshold: float = 0.05,
        allowed_layers: Optional[Sequence[str]] = None,
        require_canonical: bool = False,
        max_per_canonical_id: Optional[int] = 1,
        max_per_source: Optional[int] = 1,
        **kwargs: Any,
    ) -> List[Dict[str, Any]]:
        if "k" in kwargs and kwargs["k"] is not None:
            top_k = int(kwargs["k"])

        if not self.vectors:
            return []

        allowed = set(allowed_layers) if allowed_layers else None
        query_vector = np.array(self.embeddings_model.embed_query(query))

        results: List[Tuple[float, float, str, Dict[str, Any]]] = []
        for index, vector in enumerate(self.vectors):
            meta = self.metadata[index] if index < len(self.metadata) else {}
            layer = meta.get("layer")
            status = str(meta.get("status", "")).lower()
            text = self.documents[index]

            if allowed and layer not in allowed:
                continue
            if require_canonical and status != "canonical":
                continue

            raw_score = self._cosine_similarity(query_vector, vector)
            if raw_score < threshold:
                continue

            weighted_score = raw_score * self._document_weight(meta) * self._query_alignment_bonus(query, text, meta)

            results.append((weighted_score, raw_score, text, meta))

        results.sort(key=lambda item: (item[0], item[1]), reverse=True)
        top_results = results[:top_k]

        if not top_results:
            return []

        selected: List[Tuple[float, float, str, Dict[str, Any]]] = []
        seen_chunks = set()
        per_canonical: Dict[str, int] = defaultdict(int)
        per_source: Dict[str, int] = defaultdict(int)

        for weighted_score, raw_score, text, meta in results:
            canonical_id = str(meta.get("canonical_id") or meta.get("source") or "UNKNOWN")
            source = str(meta.get("source") or canonical_id)
            normalized_text = self._normalize_text(text)

            if normalized_text in seen_chunks:
                continue

            if max_per_canonical_id is not None and per_canonical[canonical_id] >= max_per_canonical_id:
                continue

            if max_per_source is not None and per_source[source] >= max_per_source:
                continue

            selected.append((weighted_score, raw_score, text, meta))
            seen_chunks.add(normalized_text)
            per_canonical[canonical_id] += 1
            per_source[source] += 1

            if len(selected) >= top_k:
                break

        if not selected:
            selected = top_results[:top_k]

        records: List[Dict[str, Any]] = []
        for score, raw_score, text, meta in selected:
            records.append(
                {
                    "text": text,
                    "metadata": meta,
                    "score": score,
                    "raw_score": raw_score,
                }
            )

        return records

    def search_context(
        self,
        query: str,
        top_k: int = 5,
        threshold: float = 0.05,
        allowed_layers: Optional[Sequence[str]] = None,
        require_canonical: bool = False,
        **kwargs: Any,
    ) -> Tuple[str, List[str]]:
        records = self.search(
            query,
            top_k=top_k,
            threshold=threshold,
            allowed_layers=allowed_layers,
            require_canonical=require_canonical,
            max_per_canonical_id=1,
            max_per_source=1,
            **kwargs,
        )

        if not records:
            return "", []

        context_chunks = [item["text"] for item in records]
        sources: List[str] = []
        seen = set()

        for record in records:
            meta = record.get("metadata", {})
            canonical_id = meta.get("canonical_id") or meta.get("source") or "UNKNOWN"
            layer = meta.get("layer", "UNKNOWN")
            source_path = meta.get("source", "UNKNOWN")
            citation_root = meta.get("citation_id") or canonical_id
            section_id = meta.get("section_id") or "ROOT"
            chunk = meta.get("chunk") or "1"
            citation = f"{citation_root}::{section_id}::C{chunk} | {layer} | {source_path}"
            if citation not in seen:
                seen.add(citation)
                sources.append(citation)

        return "\n\n".join(context_chunks), sources

    def save_to_json(self, filepath: str) -> None:
        data = {
            "documents": self.documents,
            "vectors": [v.tolist() for v in self.vectors],
            "metadata": self.metadata,
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_from_json(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.documents = data.get("documents", [])
        self.vectors = [np.array(v) for v in data.get("vectors", [])]
        self.metadata = data.get("metadata") or data.get("metadatas") or []
