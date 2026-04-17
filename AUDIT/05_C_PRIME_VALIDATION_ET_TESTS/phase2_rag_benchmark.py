from __future__ import annotations

import json
import sys
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from TECHNIQUE.ingest import IngestionPipeline, ROOT
from TECHNIQUE.vector_memory import VectorMemory


BASELINE_REPORT_PATH = ROOT / "AUDIT" / "rag_validation_report.json"
PHASE3_REPORT_PATH = ROOT / "AUDIT" / "rag_validation_report_phase3.json"
PHASE3_MD_PATH = ROOT / "AUDIT" / "rag_validation_report_phase3.md"
GOVERNED_INDEX_PATH = ROOT / "TECHNIQUE" / "vector_memory_governed_phase3.json"
LEGACY_GOVERNED_INDEX_PATH = ROOT / "TECHNIQUE" / "vector_memory_governed.json"


PRIMARY_LAYERS = {"CANON", "RAG_SUPPORT"}


@dataclass(frozen=True)
class QuerySpec:
    id: str
    query: str
    expected_ids: Sequence[str]
    kind: str


@dataclass
class QueryResult:
    id: str
    query: str
    kind: str
    top5: List[str]
    relevant: int
    canon: int
    support: int
    archive: int
    tech: int
    other: int
    dup: int
    citation_canonical: bool
    citation_stable: bool
    concentration: float
    score: float
    top1_source: str
    top1_citation: str
    no_valid_source: bool


CANONICAL_QUERIES: List[QuerySpec] = [
    QuerySpec("q01", "Definis mu et la loi de survie documentaire.", ["MDLYNOR-CANON-008", "MDLYNOR-CANON-013", "MDLYNOR-RAGSUP-005", "MDLYNOR-RAGSUP-010", "MDLYNOR-RAGSUP-021"], "canonical"),
    QuerySpec("q02", "Quelle est la relation entre alpha, beta et kappa ?", ["MDLYNOR-CANON-009", "MDLYNOR-CANON-008", "MDLYNOR-RAGSUP-006", "MDLYNOR-RAGSUP-005"], "canonical"),
    QuerySpec("q03", "Explique la loi e infini proportionnelle a epsilon sur mu.", ["MDLYNOR-CANON-010", "MDLYNOR-CANON-008", "MDLYNOR-CANON-013", "MDLYNOR-RAGSUP-007", "MDLYNOR-RAGSUP-005", "MDLYNOR-RAGSUP-021"], "canonical"),
    QuerySpec("q04", "Quel est l operateur D et son role ?", ["MDLYNOR-CANON-011", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-008"], "canonical"),
    QuerySpec("q05", "Quelle est la doctrine Goodhart dans MDL Ynor ?", ["MDLYNOR-CANON-012", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-009", "MDLYNOR-RAGSUP-006"], "canonical"),
    QuerySpec("q06", "Quels sont les regimes de stabilite et de cohesion ?", ["MDLYNOR-CANON-013", "MDLYNOR-CANON-005", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-010", "MDLYNOR-RAGSUP-021"], "canonical"),
    QuerySpec("q07", "Quelle difference entre canon et archive ?", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-017", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-002"], "canonical"),
    QuerySpec("q08", "Quel est le role du registre d autorite ?", ["MDLYNOR-CANON-REGISTRY-001", "MDLYNOR-CANON-REGISTRY-PORTAL-001", "MDLYNOR-CANON-REGISTRY-DOCTRINE-001", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-019"], "canonical"),
    QuerySpec("q09", "Quel est le role de RAG_SUPPORT ?", ["MDLYNOR-RAGSUP-ROOT-001", "MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-002", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-004", "MDLYNOR-RAGSUP-005", "MDLYNOR-RAGSUP-022", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001"], "canonical"),
    QuerySpec("q10", "Quel est le role des gates de validation ?", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-014", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-022"], "canonical"),
    QuerySpec("q11", "Quel est le statut des prompts, logs et wrappers ?", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-015"], "canonical"),
    QuerySpec("q12", "Explique le principe 1 concept = 1 source canonique.", ["MDLYNOR-CANON-014", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-011", "MDLYNOR-RAGSUP-020"], "canonical"),
    QuerySpec("q13", "Decris la structure CANON, RAG_SUPPORT, ARCHIVES, TECHNIQUE.", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-017", "MDLYNOR-RAGSUP-015", "MDLYNOR-RAGSUP-022"], "canonical"),
    QuerySpec("q14", "Quel est le seuil de survie documentaire ?", ["MDLYNOR-CANON-008", "MDLYNOR-CANON-013", "MDLYNOR-CANON-005", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-005", "MDLYNOR-RAGSUP-010", "MDLYNOR-RAGSUP-021"], "canonical"),
    QuerySpec("q15", "Que signifie canonical_id ?", ["MDLYNOR-CANON-014", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-RAGSUP-011", "MDLYNOR-RAGSUP-004", "MDLYNOR-RAGSUP-020"], "canonical"),
    QuerySpec("q16", "Quelle relation entre theorie, constitution et gouvernance ?", ["MDLYNOR-CANON-016", "MDLYNOR-CANON-003", "MDLYNOR-CANON-004", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-013", "MDLYNOR-RAGSUP-018"], "canonical"),
    QuerySpec("q17", "Pourquoi les miroirs doivent-ils etre exclus du retrieval principal ?", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-017", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-002"], "canonical"),
    QuerySpec("q18", "Quelle est la fonction de l index canonique ?", ["MDLYNOR-CANON-INDEX-001", "MDLYNOR-CANON-001", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-016", "MDLYNOR-RAGSUP-002"], "canonical"),
    QuerySpec("q19", "Que dit le noyau memoire sur le collapse canonique ?", ["MDLYNOR-CANON-005", "MDLYNOR-CANON-013", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-021"], "canonical"),
    QuerySpec("q20", "Quel est l ordre de lecture canonique recommande ?", ["MDLYNOR-RAGSUP-001", "MDLYNOR-CANON-INDEX-001", "MDLYNOR-CANON-001", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-016", "MDLYNOR-RAGSUP-002"], "canonical"),
]


PRODUCTION_QUERIES: List[QuerySpec] = [
    QuerySpec("p01", "Quelle citation dois-je utiliser pour mu ?", ["MDLYNOR-CANON-007", "MDLYNOR-CANON-008", "MDLYNOR-RAGSUP-004", "MDLYNOR-RAGSUP-005", "MDLYNOR-RAGSUP-021", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-020"], "production"),
    QuerySpec("p02", "Comment resoudre un citation_id sans ambiguite ?", ["MDLYNOR-CANON-007", "MDLYNOR-CANON-014", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-RAGSUP-004", "MDLYNOR-RAGSUP-011", "MDLYNOR-RAGSUP-020", "MDLYNOR-RAGSUP-003"], "production"),
    QuerySpec("p03", "Quelle couche repond a une question doctrinale ?", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-015", "MDLYNOR-RAGSUP-019", "MDLYNOR-CANON-REGISTRY-DOCTRINE-001"], "production"),
    QuerySpec("p04", "Que faire si aucune source canonique ne soutient la reponse ?", ["MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-004", "MDLYNOR-RAGSUP-022", "MDLYNOR-CANON-007", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-020"], "production"),
    QuerySpec("p05", "Comment eviter le monopole d un document pivot ?", ["MDLYNOR-RAGSUP-003", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-RAGSUP-014", "MDLYNOR-RAGSUP-007", "MDLYNOR-RAGSUP-011", "MDLYNOR-RAGSUP-004"], "production"),
    QuerySpec("p06", "Quelle fiche couvre Goodhart ?", ["MDLYNOR-CANON-012", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-009", "MDLYNOR-RAGSUP-014", "MDLYNOR-RAGSUP-018"], "production"),
    QuerySpec("p07", "Quelle fiche couvre la relation theorie constitution gouvernance ?", ["MDLYNOR-CANON-016", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-013", "MDLYNOR-RAGSUP-018"], "production"),
    QuerySpec("p08", "Quel est le comportement attendu des doublons non canoniques ?", ["MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-017", "MDLYNOR-RAGSUP-019"], "production"),
    QuerySpec("p09", "Quelle fiche stabilise canonical_id et citation_id ?", ["MDLYNOR-CANON-007", "MDLYNOR-CANON-014", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-RAGSUP-004", "MDLYNOR-RAGSUP-011", "MDLYNOR-RAGSUP-020"], "production"),
    QuerySpec("p10", "Quelle fiche donne l ordre de lecture canonique ?", ["MDLYNOR-RAGSUP-001", "MDLYNOR-CANON-INDEX-001", "MDLYNOR-CANON-001", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-016"], "production"),
    QuerySpec("p11", "Quel est le role des gates de validation ?", ["MDLYNOR-RAGSUP-014", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-003", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-022"], "production"),
    QuerySpec("p12", "Quel est le role de RAG_SUPPORT ?", ["MDLYNOR-RAGSUP-022", "MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-002", "MDLYNOR-RAGSUP-004", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-014"], "production"),
    QuerySpec("p13", "Les prompts, logs et wrappers ont-ils une autorite doctrinale ?", ["MDLYNOR-RAGSUP-015", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-019"], "production"),
    QuerySpec("p14", "Quelle difference entre canon et archive et miroirs ?", ["MDLYNOR-RAGSUP-017", "MDLYNOR-CANON-015", "MDLYNOR-CANON-REGISTRY-LAYERS-001", "MDLYNOR-RAGSUP-012", "MDLYNOR-RAGSUP-019"], "production"),
    QuerySpec("p15", "Quel est le role du registre d autorite ?", ["MDLYNOR-RAGSUP-019", "MDLYNOR-CANON-REGISTRY-001", "MDLYNOR-CANON-REGISTRY-PORTAL-001", "MDLYNOR-CANON-REGISTRY-DOCTRINE-001", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-CANON-REGISTRY-LAYERS-001"], "production"),
    QuerySpec("p16", "Explique le principe 1 concept = 1 source canonique.", ["MDLYNOR-RAGSUP-020", "MDLYNOR-CANON-014", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-CANON-REGISTRY-LAYERS-001"], "production"),
    QuerySpec("p17", "Quelle est la fonction de l index canonique ?", ["MDLYNOR-RAGSUP-016", "MDLYNOR-CANON-INDEX-001", "MDLYNOR-CANON-001", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-001", "MDLYNOR-RAGSUP-002"], "production"),
    QuerySpec("p18", "Quel est le seuil de survie documentaire ?", ["MDLYNOR-RAGSUP-021", "MDLYNOR-CANON-008", "MDLYNOR-CANON-013", "MDLYNOR-CANON-005", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-005", "MDLYNOR-RAGSUP-010", "MDLYNOR-RAGSUP-014"], "production"),
    QuerySpec("p19", "Quelle relation entre theorie, constitution et gouvernance ?", ["MDLYNOR-RAGSUP-018", "MDLYNOR-CANON-016", "MDLYNOR-CANON-003", "MDLYNOR-CANON-015", "MDLYNOR-RAGSUP-013"], "production"),
    QuerySpec("p20", "Que faire si aucune source canonique ne soutient la reponse ?", ["MDLYNOR-RAGSUP-022", "MDLYNOR-RAGSUP-004", "MDLYNOR-CANON-007", "MDLYNOR-CANON-REGISTRY-CITATION-001", "MDLYNOR-RAGSUP-019", "MDLYNOR-RAGSUP-020"], "production"),
]


def pct(part: int, total: int) -> float:
    return round((part / total) * 100.0, 2) if total else 0.0


def canonical_citation(meta: Dict[str, Any]) -> str:
    citation_id = meta.get("citation_id") or meta.get("canonical_id") or "UNKNOWN"
    section_id = meta.get("section_id") or "ROOT"
    chunk = meta.get("chunk") or "1"
    layer = meta.get("layer", "UNKNOWN")
    source = meta.get("source", "UNKNOWN")
    return f"{citation_id}::{section_id}::C{chunk} | {layer} | {source}"


def canonical_key(meta: Dict[str, Any]) -> str:
    return str(meta.get("canonical_id") or meta.get("source") or "UNKNOWN")


def evaluate_once(memory: VectorMemory, spec: QuerySpec) -> QueryResult:
    records = memory.search(
        spec.query,
        top_k=5,
        threshold=0.05,
        allowed_layers=("CANON", "RAG_SUPPORT"),
        require_canonical=False,
        max_per_canonical_id=1,
        max_per_source=1,
    )

    top5 = [canonical_citation(record.get("metadata", {})) for record in records]
    metas = [record.get("metadata", {}) for record in records]
    canonical_ids = [canonical_key(meta) for meta in metas]
    layers = [str(meta.get("layer", "UNKNOWN")) for meta in metas]
    sources = [str(meta.get("source", "UNKNOWN")) for meta in metas]

    expected = set(spec.expected_ids)
    relevant = sum(1 for meta in metas if canonical_key(meta) in expected)
    canon = sum(1 for layer in layers if layer == "CANON")
    support = sum(1 for layer in layers if layer == "RAG_SUPPORT")
    archive = sum(1 for layer in layers if layer == "ARCHIVES")
    tech = sum(1 for layer in layers if layer == "TECHNIQUE")
    other = len(records) - (canon + support + archive + tech)
    duplicate_hits = sum(count - 1 for count in Counter(canonical_ids).values() if count > 1)

    top1_meta = metas[0] if metas else {}
    top1_layer = str(top1_meta.get("layer", "UNKNOWN"))
    top1_key = canonical_key(top1_meta)
    top1_citation = top5[0] if top5 else ""
    citation_canonical = bool(records) and top1_layer in PRIMARY_LAYERS and top1_key in expected
    top1_share = (Counter(canonical_ids).most_common(1)[0][1] / len(records)) if records else 0.0
    unique_share = len(set(canonical_ids)) / len(records) if records else 0.0
    citation_stable = bool(records) and top1_citation == evaluate_once.cached_top1.get(spec.id, top1_citation)
    if spec.id not in evaluate_once.cached_top1:
        evaluate_once.cached_top1[spec.id] = top1_citation

    score = round(
        10.0
        * (
            0.40 * (relevant / 5.0 if records else 0.0)
            + 0.20 * (1.0 if citation_canonical else 0.0)
            + 0.20 * (1.0 if citation_stable else 0.0)
            + 0.20 * unique_share
        ),
        2,
    )

    no_valid_source = not records or not citation_canonical

    return QueryResult(
        id=spec.id,
        query=spec.query,
        kind=spec.kind,
        top5=top5,
        relevant=relevant,
        canon=canon,
        support=support,
        archive=archive,
        tech=tech,
        other=other,
        dup=duplicate_hits,
        citation_canonical=citation_canonical,
        citation_stable=citation_stable,
        concentration=round(top1_share, 2),
        score=score,
        top1_source=canonical_citation(top1_meta) if top1_meta else "",
        top1_citation=top1_citation,
        no_valid_source=no_valid_source,
    )


evaluate_once.cached_top1 = {}


def evaluate_query(memory: VectorMemory, spec: QuerySpec) -> QueryResult:
    evaluate_once.cached_top1 = {}
    first = evaluate_once(memory, spec)
    second = evaluate_once(memory, spec)
    first.citation_stable = bool(first.top1_citation and first.top1_citation == second.top1_citation)
    first.score = round(
        10.0
        * (
            0.40 * (first.relevant / 5.0 if first.top5 else 0.0)
            + 0.20 * (1.0 if first.citation_canonical else 0.0)
            + 0.20 * (1.0 if first.citation_stable else 0.0)
            + 0.20 * (len(set(first.top5)) / 5.0 if first.top5 else 0.0)
        ),
        2,
    )
    return first


def summarize(results: Sequence[QueryResult]) -> Dict[str, Any]:
    total_slots = len(results) * 5
    relevant_slots = sum(item.relevant for item in results)
    canon_slots = sum(item.canon for item in results)
    support_slots = sum(item.support for item in results)
    archive_slots = sum(item.archive for item in results)
    tech_slots = sum(item.tech for item in results)
    other_slots = sum(item.other for item in results)
    dup_slots = sum(item.dup for item in results)
    citation_canonical = sum(1 for item in results if item.citation_canonical)
    citation_stable = sum(1 for item in results if item.citation_stable)
    no_valid_source = sum(1 for item in results if item.no_valid_source)
    monopoly_violations = sum(1 for item in results if item.concentration > 0.40)

    diversity_score = sum(len(set(item.top5)) / 5.0 if item.top5 else 0.0 for item in results) / len(results) if results else 0.0
    robustness = round(
        10.0
        * (
            0.35 * (relevant_slots / total_slots if total_slots else 0.0)
            + 0.25 * (citation_canonical / len(results) if results else 0.0)
            + 0.25 * (citation_stable / len(results) if results else 0.0)
            + 0.15 * diversity_score
        ),
        2,
    )

    return {
        "queries": len(results),
        "top5_pertinent_rate": pct(relevant_slots, total_slots),
        "canonical_rate": pct(canon_slots, total_slots),
        "support_rate": pct(support_slots, total_slots),
        "archive_leak_rate": pct(archive_slots, total_slots),
        "tech_leak_rate": pct(tech_slots, total_slots),
        "other_rate": pct(other_slots, total_slots),
        "duplicate_rate": pct(dup_slots, total_slots),
        "citation_canonical_rate": pct(citation_canonical, len(results)),
        "citation_stable_rate": pct(citation_stable, len(results)),
        "no_valid_source_rate": pct(no_valid_source, len(results)),
        "monopoly_violation_rate": pct(monopoly_violations, len(results)),
        "average_concentration": round(sum(item.concentration for item in results) / len(results), 2) if results else 0.0,
        "average_score": robustness,
    }


def load_baseline_governed_summary() -> Dict[str, Any]:
    if not BASELINE_REPORT_PATH.exists():
        return {}

    with BASELINE_REPORT_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    governed_entries = data.get("governed", [])
    if not governed_entries:
        return {}

    total = len(governed_entries) * 5
    relevant = sum(int(item.get("relevant", 0)) for item in governed_entries)
    canon = sum(int(item.get("canon", 0)) for item in governed_entries)
    archive = sum(int(item.get("archive", 0)) for item in governed_entries)
    tech = sum(int(item.get("tech", 0)) for item in governed_entries)
    other = sum(int(item.get("other", 0)) for item in governed_entries)
    dup = sum(int(item.get("dup", 0)) for item in governed_entries)
    citation_canonical = sum(1 for item in governed_entries if item.get("citation_canonical"))
    citation_stable = sum(1 for item in governed_entries if item.get("citation_stable"))
    no_valid_source = sum(1 for item in governed_entries if int(item.get("relevant", 0)) == 0 or not item.get("citation_canonical"))

    return {
        "queries": len(governed_entries),
        "top5_pertinent_rate": pct(relevant, total),
        "canonical_rate": pct(canon, total),
        "archive_leak_rate": pct(archive, total),
        "tech_leak_rate": pct(tech, total),
        "other_rate": pct(other, total),
        "duplicate_rate": pct(dup, total),
        "citation_canonical_rate": pct(citation_canonical, len(governed_entries)),
        "citation_stable_rate": pct(citation_stable, len(governed_entries)),
        "no_valid_source_rate": pct(no_valid_source, len(governed_entries)),
        "average_score": round(sum(float(item.get("score", 0.0)) for item in governed_entries) / len(governed_entries), 2),
    }


def build_governed_index() -> VectorMemory:
    memory = VectorMemory()
    pipeline = IngestionPipeline(memory)
    pipeline.run()
    memory.save_to_json(str(GOVERNED_INDEX_PATH))
    memory.save_to_json(str(LEGACY_GOVERNED_INDEX_PATH))
    return memory


def render_markdown(before: Dict[str, Any], canonical_results: Sequence[QueryResult], production_results: Sequence[QueryResult], after_summary: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Phase 3 RAG benchmark")
    lines.append("")
    lines.append("## Baseline vs phase 3")
    lines.append("")
    lines.append("| Metric | Baseline governed | Phase 3 canonical | Phase 3 production |")
    lines.append("|---|---:|---:|---:|")
    lines.append(f"| Top-5 pertinent | {before.get('top5_pertinent_rate', 0)}% | {after_summary.get('canonical', {}).get('top5_pertinent_rate', 0)}% | {after_summary.get('production', {}).get('top5_pertinent_rate', 0)}% |")
    lines.append(f"| Archive leak | {before.get('archive_leak_rate', 0)}% | {after_summary.get('canonical', {}).get('archive_leak_rate', 0)}% | {after_summary.get('production', {}).get('archive_leak_rate', 0)}% |")
    lines.append(f"| Tech leak | {before.get('tech_leak_rate', 0)}% | {after_summary.get('canonical', {}).get('tech_leak_rate', 0)}% | {after_summary.get('production', {}).get('tech_leak_rate', 0)}% |")
    lines.append(f"| Citation canonical | {before.get('citation_canonical_rate', 0)}% | {after_summary.get('canonical', {}).get('citation_canonical_rate', 0)}% | {after_summary.get('production', {}).get('citation_canonical_rate', 0)}% |")
    lines.append(f"| Citation stable | {before.get('citation_stable_rate', 0)}% | {after_summary.get('canonical', {}).get('citation_stable_rate', 0)}% | {after_summary.get('production', {}).get('citation_stable_rate', 0)}% |")
    lines.append(f"| Monopoly violations | n/a | {after_summary.get('canonical', {}).get('monopoly_violation_rate', 0)}% | {after_summary.get('production', {}).get('monopoly_violation_rate', 0)}% |")
    lines.append(f"| Average score | {before.get('average_score', 0)} | {after_summary.get('canonical', {}).get('average_score', 0)} | {after_summary.get('production', {}).get('average_score', 0)} |")
    lines.append("")
    lines.append("## Canonical queries")
    for item in canonical_results:
        lines.append(f"- {item.id}: {item.query}")
        lines.append(f"  - top5: {', '.join(item.top5)}")
        lines.append(f"  - score: {item.score}")
        lines.append(f"  - citation_stable: {item.citation_stable}")
        lines.append(f"  - citation_canonical: {item.citation_canonical}")
    lines.append("")
    lines.append("## Production queries")
    for item in production_results:
        lines.append(f"- {item.id}: {item.query}")
        lines.append(f"  - top5: {', '.join(item.top5)}")
        lines.append(f"  - score: {item.score}")
        lines.append(f"  - citation_stable: {item.citation_stable}")
        lines.append(f"  - citation_canonical: {item.citation_canonical}")
    return "\n".join(lines)


def main() -> None:
    baseline = load_baseline_governed_summary()
    memory = build_governed_index()

    canonical_results = [evaluate_query(memory, spec) for spec in CANONICAL_QUERIES]
    production_results = [evaluate_query(memory, spec) for spec in PRODUCTION_QUERIES]

    canonical_summary = summarize(canonical_results)
    production_summary = summarize(production_results)
    combined_summary = summarize([*canonical_results, *production_results])

    gates = {
        "citation_stable_min": canonical_summary["citation_stable_rate"] >= 90.0,
        "citation_canonical_min": canonical_summary["citation_canonical_rate"] >= 95.0,
        "archive_leak_zero": canonical_summary["archive_leak_rate"] == 0.0,
        "tech_leak_zero": canonical_summary["tech_leak_rate"] == 0.0,
        "top5_pertinent_min": canonical_summary["top5_pertinent_rate"] >= 70.0,
        "no_valid_source_zero": canonical_summary["no_valid_source_rate"] == 0.0,
        "monopoly_rate_zero": canonical_summary["monopoly_violation_rate"] == 0.0,
        "production_top5_min": production_summary["top5_pertinent_rate"] >= 70.0,
        "support_coverage": production_summary["support_rate"] >= 60.0,
    }
    production_ready = all(gates.values())

    report: Dict[str, Any] = {
        "baseline_governed": baseline,
        "phase3_canonical": canonical_summary,
        "phase3_production": production_summary,
        "phase3_combined": combined_summary,
        "canonical_queries": [asdict(item) for item in canonical_results],
        "production_queries": [asdict(item) for item in production_results],
        "gates": gates,
        "production_ready": production_ready,
        "index_path": str(GOVERNED_INDEX_PATH),
    }

    PHASE3_REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    PHASE3_MD_PATH.write_text(
        render_markdown(baseline, canonical_results, production_results, {
            "canonical": canonical_summary,
            "production": production_summary,
        }),
        encoding="utf-8",
    )

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
