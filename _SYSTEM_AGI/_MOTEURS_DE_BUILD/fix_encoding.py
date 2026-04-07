#!/usr/bin/env python3
"""Normalize scientific corpus files and strip BOM markers.

The tool is intentionally conservative:
- it targets only `.py`, `.md`, `.json`, and `.jsonld` files;
- it removes leading BOM markers and any stray U+FEFF characters;
- it normalizes line endings to the current platform convention;
- it optionally creates `.bak` backups before writing.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

TARGET_SUFFIXES = {".py", ".md", ".json", ".jsonld"}
LINE_ENDING = "\r\n" if sys.platform.startswith("win") else "\n"


@dataclass
class FileReport:
 path: Path
 changed: bool
 removed_bom: int
 line_ending_changed: bool
 json_valid: bool | None = None


def iter_target_files(roots: list[Path]) -> Iterable[Path]:
 for root in roots:
 if root.is_file():
 if root.suffix.lower() in TARGET_SUFFIXES:
 yield root
 continue
 if not root.exists():
 continue
 for path in root.rglob("*"):
 if path.is_file() and path.suffix.lower() in TARGET_SUFFIXES:
 yield path


def normalize_text(text: str) -> tuple[str, int, bool]:
 removed_bom = text.count("\ufeff")
 if removed_bom:
 text = text.replace("\ufeff", "")

 line_ending_changed = ("\r\n" in text) or ("\r" in text)
 text = text.replace("\r\n", "\n").replace("\r", "\n")
 text = LINE_ENDING.join(text.split("\n"))
 return text, removed_bom, line_ending_changed


def process_file(path: Path, *, apply: bool, backup: bool) -> FileReport:
 with path.open("r", encoding="utf-8", newline="") as handle:
 original = handle.read()

 normalized, removed_bom, line_ending_changed = normalize_text(original)
 changed = normalized != original
 json_valid: bool | None = None

 if path.suffix.lower() in {".json", ".jsonld"}:
 try:
 json.loads(normalized)
 json_valid = True
 except json.JSONDecodeError:
 json_valid = False

 if changed and apply:
 if backup:
 backup_path = path.with_suffix(path.suffix + ".bak")
 backup_path.write_text(original, encoding="utf-8", newline="")
 path.write_text(normalized, encoding="utf-8", newline="")

 return FileReport(
 path=path,
 changed=changed,
 removed_bom=removed_bom,
 line_ending_changed=line_ending_changed,
 json_valid=json_valid,
 )


def main(argv: list[str] | None = None) -> int:
 parser = argparse.ArgumentParser(
 description="Remove BOM markers and normalize scientific text encodings."
 )
 parser.add_argument(
 "paths",
 nargs="*",
 default=["."],
 help="Files or directories to scan. Defaults to the current directory.",
 )
 parser.add_argument(
 "--apply",
 action="store_true",
 help="Write normalized content back to disk.",
 )
 parser.add_argument(
 "--backup",
 action="store_true",
 help="Write a .bak copy before modifying each file.",
 )
 args = parser.parse_args(argv)

 roots = [Path(p).resolve() for p in args.paths]
 reports: list[FileReport] = []

 for file_path in iter_target_files(roots):
 try:
 reports.append(process_file(file_path, apply=args.apply, backup=args.backup))
 except UnicodeDecodeError as exc:
 print(f"[skip] {file_path} : {exc}", file=sys.stderr)
 except json.JSONDecodeError as exc:
 print(f"[skip] {file_path} : invalid JSON ({exc})", file=sys.stderr)

 changed = [report for report in reports if report.changed]
 print(f"scanned={len(reports)} changed={len(changed)} apply={args.apply}")

 for report in changed:
 extra = ""
 if report.json_valid is not None:
 extra = f" json_valid={report.json_valid}"
 print(
 f"{report.path} | removed_bom={report.removed_bom} "
 f"line_endings_changed={report.line_ending_changed}{extra}"
 )

 return 0


if __name__ == "__main__":
 raise SystemExit(main())
