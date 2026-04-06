#!/usr/bin/env python3



"""Scan and normalize mojibake in markdown and JSON files.







The script is intentionally conservative:



- it only touches .md and .json files;



- it rewrites line by line, only when a candidate repair improves the text;



- it validates JSON after repair before writing.



"""







from __future__ import annotations







import argparse



import json



import re



import shutil



import sys



import unicodedata



from dataclasses import dataclass



from pathlib import Path



from typing import Iterable











MOJIBAKE_PATTERNS = (



    re.compile(r"."),



    re.compile(r"."),



    re.compile(r"[]"),



    re.compile(r""),



)











@dataclass



class FileReport:



    path: Path



    suspicious_before: int



    suspicious_after: int



    changed: bool



    valid_json: bool | None = None











def suspicious_count(text: str) -> int:



    return sum(len(pattern.findall(text)) for pattern in MOJIBAKE_PATTERNS)











def candidate_repair(text: str) -> str | None:



    candidates: list[str] = []







    for encoding in ("cp1252", "latin-1"):



        try:



            fixed = text.encode(encoding).decode("utf-8")



        except (UnicodeEncodeError, UnicodeDecodeError):



            continue



        candidates.append(unicodedata.normalize("NFC", fixed))







    if not candidates:



        return None







    best = min(candidates, key=lambda item: (suspicious_count(item), item.count(""), abs(len(item) - len(text))))



    if suspicious_count(best) < suspicious_count(text):



        return best



    return None











def normalize_text(text: str) -> tuple[str, bool]:



    changed = False



    lines: list[str] = []







    for line in text.splitlines(keepends=True):



        repaired = candidate_repair(line)



        if repaired is not None and repaired != line:



            lines.append(repaired)



            changed = True



        else:



            lines.append(line)







    normalized = "".join(lines)



    if normalized != text:



        changed = True



    return normalized, changed











def iter_target_files(paths: Iterable[Path]) -> Iterable[Path]:



    for base in paths:



        if base.is_file() and base.suffix.lower() in {".md", ".json"}:



            yield base



            continue



        if not base.exists():



            continue



        for file in base.rglob("*"):



            if file.is_file() and file.suffix.lower() in {".md", ".json"}:



                yield file











def process_file(path: Path, apply: bool, backup: bool) -> FileReport:



    original = path.read_text(encoding="utf-8", errors="strict")



    before = suspicious_count(original)



    if before == 0:



        return FileReport(path=path, suspicious_before=0, suspicious_after=0, changed=False)







    repaired, changed = normalize_text(original)



    after = suspicious_count(repaired)



    valid_json: bool | None = None







    if path.suffix.lower() == ".json" and changed:



        try:



            json.loads(repaired)



            valid_json = True



        except json.JSONDecodeError:



            valid_json = False



            repaired = original



            changed = False



            after = before







    if changed and apply:



        if backup:



            shutil.copy2(path, path.with_suffix(path.suffix + ".bak"))



        path.write_text(repaired, encoding="utf-8", newline="")







    return FileReport(



        path=path,



        suspicious_before=before,



        suspicious_after=after,



        changed=changed,



        valid_json=valid_json,



    )











def main() -> int:



    parser = argparse.ArgumentParser(description="Normalize encoding issues in .md and .json files.")



    parser.add_argument("paths", nargs="*", default=["."], help="Root paths to scan.")



    parser.add_argument("--apply", action="store_true", help="Write repaired files back to disk.")



    parser.add_argument("--backup", action="store_true", help="Create .bak copies before writing.")



    args = parser.parse_args()







    roots = [Path(p).resolve() for p in args.paths]



    reports: list[FileReport] = []







    for file_path in iter_target_files(roots):



        try:



            reports.append(process_file(file_path, apply=args.apply, backup=args.backup))



        except UnicodeDecodeError as exc:



            print(f"[skip] {file_path} : {exc}", file=sys.stderr)



        except json.JSONDecodeError as exc:



            print(f"[skip] {file_path} : invalid UTF-8/JSON content ({exc})", file=sys.stderr)







    changed = [r for r in reports if r.changed]



    print(f"scanned={len(reports)} changed={len(changed)} apply={args.apply}")



    for report in changed:



        extra = ""



        if report.valid_json is not None:



            extra = f" json_valid={report.valid_json}"



        print(



            f"{report.path} | suspicious_before={report.suspicious_before} "



            f"suspicious_after={report.suspicious_after}{extra}"



        )







    return 0











if __name__ == "__main__":



    raise SystemExit(main())



