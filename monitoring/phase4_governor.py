from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from event_tracker import EventTracker
from quarantine_monitor import QuarantineDecision, QuarantineMonitor


PRIMARY_LAYERS = ("CANON", "RAG_SUPPORT")
SUPPORTED_TEXT_EXTENSIONS = {".md", ".txt"}
FORBIDDEN_PRIMARY_TERMS = (
    "prompts",
    "logs",
    "wrappers",
    "auto_audits",
    "releases",
    "mirrors",
)
REPORT_CANDIDATES = [
    ROOT / "AUDIT" / "rag_validation_report_phase4.json",
    ROOT / "AUDIT" / "rag_validation_report_phase3.json",
    ROOT / "AUDIT" / "rag_validation_report.json",
]
POLICY_PATH = SCRIPT_DIR / "phase4_policy.json"
HEALTH_REPORT_PATH = SCRIPT_DIR / "phase4_health_report.json"
HEALTH_MD_PATH = SCRIPT_DIR / "phase4_health_report.md"
HEALTH_HISTORY_PATH = SCRIPT_DIR / "phase4_health_history.jsonl"
EVENT_LOG_PATH = SCRIPT_DIR / "phase4_events.jsonl"


@dataclass(frozen=True)
class MetricView:
    name: str
    metrics: Dict[str, Any]


@dataclass(frozen=True)
class HealthResult:
    alert_level: str
    rollback_required: bool
    production_ready: bool
    benchmark_path: str
    quarantine_count: int
    quarantine_examples: List[Dict[str, Any]]
    pivot_watchlist: List[Dict[str, Any]]
    drift: Dict[str, Any]
    metric_views: Dict[str, Dict[str, Any]]
    previous_alert_level: Optional[str]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)


def parse_frontmatter(text: str) -> Dict[str, str]:
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


def first_existing_report() -> Path:
    for candidate in REPORT_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No benchmark report found for phase 4 monitoring.")


def flatten_metrics(report: Mapping[str, Any]) -> Dict[str, Dict[str, Any]]:
    views: Dict[str, Dict[str, Any]] = {}
    for key in ("phase3_canonical", "phase3_production", "phase3_combined", "phase4_canonical", "phase4_production", "phase4_combined"):
        value = report.get(key)
        if isinstance(value, dict):
            views[key] = value
    return views


def previous_history() -> Optional[Dict[str, Any]]:
    if not HEALTH_HISTORY_PATH.exists():
        return None

    last: Optional[Dict[str, Any]] = None
    with HEALTH_HISTORY_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                last = json.loads(stripped)
            except json.JSONDecodeError:
                continue
    return last


def load_policy() -> Dict[str, Any]:
    policy = load_json(POLICY_PATH, {})
    if policy:
        return policy
    return {
        "targets": {
            "top5_pertinent_min": 70.0,
            "citation_canonical_min": 95.0,
            "citation_stable_min": 90.0,
            "archive_leak_zero": True,
            "tech_leak_zero": True,
            "no_valid_source_zero": True,
            "monopoly_violation_zero": True,
            "support_coverage_min": 60.0,
        },
        "alerts": {
            "yellow": {
                "top5_drop_points": 2.0,
                "citation_stable_drop_points": 2.0,
                "support_drop_points": 5.0,
                "concentration_max": 0.25,
            },
            "orange": {
                "top5_drop_points": 5.0,
                "citation_stable_drop_points": 5.0,
                "support_drop_points": 8.0,
                "concentration_max": 0.30,
            },
        },
        "quarantine": {
            "require_canonical_id": True,
            "require_status": True,
            "allowed_primary_layers": list(PRIMARY_LAYERS),
            "forbidden_primary_terms": list(FORBIDDEN_PRIMARY_TERMS),
        },
    }


def select_metrics(report: Mapping[str, Any]) -> Dict[str, Dict[str, Any]]:
    views = flatten_metrics(report)
    selected = {
        "canonical": views.get("phase3_canonical", views.get("phase4_canonical", views.get("phase3_combined", {}))),
        "production": views.get("phase3_production", views.get("phase4_production", views.get("phase3_combined", {}))),
        "combined": views.get("phase3_combined", views.get("phase4_combined", views.get("phase3_canonical", {}))),
    }
    return selected


def metric_value(metrics: Mapping[str, Any], key: str, default: float = 0.0) -> float:
    try:
        return float(metrics.get(key, default))
    except (TypeError, ValueError):
        return default


def detect_pivot_watchlist(report: Mapping[str, Any]) -> List[Dict[str, Any]]:
    top1_counter: Counter[str] = Counter()
    layer_counter: Counter[str] = Counter()
    watchlist: List[Dict[str, Any]] = []

    for bucket in ("canonical_queries", "production_queries"):
        for item in report.get(bucket, []):
            top1 = str(item.get("top1_source", "")).strip()
            if top1:
                top1_counter[top1] += 1
                layer = top1.split(" | ")[1] if " | " in top1 else "UNKNOWN"
                layer_counter[layer] += 1

    total = sum(top1_counter.values()) or 1
    for source, count in top1_counter.most_common(5):
        share = round(count / total, 3)
        if share >= 0.15:
            watchlist.append({"source": source, "share": share, "count": count})

    for layer, count in layer_counter.most_common():
        share = round(count / total, 3)
        if share >= 0.25:
            watchlist.append({"layer": layer, "share": share, "count": count})

    return watchlist


def scan_primary_surface(policy: Mapping[str, Any]) -> List[Dict[str, Any]]:
    quarantine: List[Dict[str, Any]] = []
    q_policy = policy.get("quarantine", {})
    require_canonical_id = bool(q_policy.get("require_canonical_id", True))
    require_status = bool(q_policy.get("require_status", True))
    allowed_statuses = {
        "CANON": {"canonical", "navigation", "registry", "guide", "policy"},
        "RAG_SUPPORT": {"support", "navigation", "guide", "answer_card", "faq", "crosswalk", "policy"},
    }
    forbidden_statuses = {"archive", "quarantine", "derived", "mirror", "prompt", "log", "wrapper", "auto_audit", "release"}

    for layer in PRIMARY_LAYERS:
        layer_root = ROOT / layer
        if not layer_root.exists():
            continue

        for path in layer_root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in SUPPORTED_TEXT_EXTENSIONS:
                continue

            reasons: List[str] = []
            try:
                text = path.read_text(encoding="utf-8", errors="strict")
            except UnicodeDecodeError:
                quarantine.append(
                    {
                        "layer": layer,
                        "path": str(path),
                        "status": "quarantine",
                        "reasons": ["utf8_error"],
                    }
                )
                continue

            metadata = parse_frontmatter(text)
            canonical_id = str(metadata.get("canonical_id", "")).strip()
            status = str(metadata.get("status", "")).strip().lower()
            document_role = str(metadata.get("document_role", "")).strip().lower()
            retrieval_weight = metadata.get("retrieval_weight", "")

            if require_canonical_id and not canonical_id:
                reasons.append("missing_canonical_id")
            if require_status and not status:
                reasons.append("missing_status")

            if status:
                if status in forbidden_statuses:
                    reasons.append("forbidden_status")
                elif status not in allowed_statuses.get(layer, {status}):
                    reasons.append("unexpected_status")

            if reasons:
                quarantine.append(
                    {
                        "layer": layer,
                        "path": str(path),
                        "status": status or "missing",
                        "canonical_id": canonical_id or "missing",
                        "document_role": document_role or "missing",
                        "retrieval_weight": retrieval_weight,
                        "reasons": reasons,
                    }
                )

    return quarantine


def classify_alert(
    policy: Mapping[str, Any],
    current: Mapping[str, Any],
    previous: Optional[Mapping[str, Any]],
    pivot_watchlist: Sequence[Mapping[str, Any]],
    quarantine_count: int,
    production_ready: bool,
) -> Tuple[str, List[str], bool]:
    targets = policy.get("targets", {})
    alerts = policy.get("alerts", {})
    yellow = alerts.get("yellow", {})
    orange = alerts.get("orange", {})

    top5 = metric_value(current, "top5_pertinent_rate")
    citation_stable = metric_value(current, "citation_stable_rate")
    citation_canonical = metric_value(current, "citation_canonical_rate")
    archive_leak = metric_value(current, "archive_leak_rate")
    tech_leak = metric_value(current, "tech_leak_rate")
    no_valid_source = metric_value(current, "no_valid_source_rate")
    monopoly = metric_value(current, "monopoly_violation_rate")
    support_rate = metric_value(current, "support_rate")
    concentration = metric_value(current, "average_concentration")
    reasons: List[str] = []
    hard_fail = (
        top5 < float(targets.get("top5_pertinent_min", 70.0))
        or citation_stable < float(targets.get("citation_stable_min", 90.0))
        or citation_canonical < float(targets.get("citation_canonical_min", 95.0))
        or archive_leak > 0.0
        or tech_leak > 0.0
        or no_valid_source > 0.0
        or monopoly > 0.0
        or quarantine_count > 0
    )

    if hard_fail:
        reasons.append("gate_failure")

    if archive_leak > 0.0 or tech_leak > 0.0:
        reasons.append("forbidden_layer_leak")
    if no_valid_source > 0.0:
        reasons.append("missing_valid_source")
    if monopoly > 0.0:
        reasons.append("topk_monopoly_violation")
    if support_rate < float(targets.get("support_coverage_min", 60.0)):
        reasons.append("support_coverage_below_target")

    pivot_pressure = False
    for item in pivot_watchlist:
        share = float(item.get("share", 0.0))
        label = json.dumps(item, ensure_ascii=False).lower()
        if share >= 0.25 and any(token in label for token in ("readme", "regist", "index")):
            pivot_pressure = True
            break

    alert_level = "GREEN"
    if hard_fail:
        alert_level = "RED"

    if previous:
        prev_metrics = previous.get("metrics", {})
        prev_combined = prev_metrics.get("combined", {})
        prev_alert = str(previous.get("alert_level", "GREEN")).upper()

        if alert_level == "GREEN":
            top5_drop = metric_value(prev_combined, "top5_pertinent_rate") - top5
            stable_drop = metric_value(prev_combined, "citation_stable_rate") - citation_stable
            support_drop = metric_value(prev_combined, "support_rate") - support_rate

            if top5_drop >= yellow.get("top5_drop_points", 2.0) or stable_drop >= yellow.get("citation_stable_drop_points", 2.0):
                alert_level = "YELLOW"
                reasons.append("light_drift")

            if top5_drop >= orange.get("top5_drop_points", 5.0) or stable_drop >= orange.get("citation_stable_drop_points", 5.0):
                alert_level = "ORANGE"
                reasons.append("material_drift")

            if support_drop >= yellow.get("support_drop_points", 5.0):
                alert_level = max(alert_level, "YELLOW", key=lambda value: ["GREEN", "YELLOW", "ORANGE", "RED", "CRITICAL"].index(value))
                reasons.append("support_drop")

            if concentration >= yellow.get("concentration_max", 0.25):
                alert_level = max(alert_level, "YELLOW", key=lambda value: ["GREEN", "YELLOW", "ORANGE", "RED", "CRITICAL"].index(value))
                reasons.append("topk_concentration_high")

        if alert_level == "RED" and prev_alert in {"RED", "ORANGE"}:
            alert_level = "CRITICAL"
            reasons.append("consecutive_red_or_better")

    if pivot_pressure and alert_level == "GREEN":
        alert_level = "YELLOW"
        reasons.append("pivot_pressure")
    elif pivot_pressure and alert_level == "YELLOW":
        alert_level = "ORANGE"
        reasons.append("pivot_pressure_material")

    rollback_required = alert_level in {"RED", "CRITICAL"} or hard_fail

    if not production_ready and alert_level == "GREEN":
        alert_level = "ORANGE"
        reasons.append("benchmark_not_marked_production_ready")

    return alert_level, sorted(set(reasons)), rollback_required


def render_markdown(result: HealthResult) -> str:
    lines: List[str] = []
    lines.append("# Phase 4 health report")
    lines.append("")
    lines.append(f"- Alert level: `{result.alert_level}`")
    lines.append(f"- Rollback required: `{result.rollback_required}`")
    lines.append(f"- Production ready: `{result.production_ready}`")
    lines.append(f"- Benchmark path: `{result.benchmark_path}`")
    lines.append(f"- Quarantine count: `{result.quarantine_count}`")
    lines.append("")
    lines.append("## Metric views")
    for name, metrics in result.metric_views.items():
        lines.append(f"### {name}")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|---|---:|")
        for key in (
            "top5_pertinent_rate",
            "citation_canonical_rate",
            "citation_stable_rate",
            "archive_leak_rate",
            "tech_leak_rate",
            "no_valid_source_rate",
            "monopoly_violation_rate",
            "support_rate",
            "average_concentration",
            "average_score",
        ):
            if key in metrics:
                lines.append(f"| {key} | {metrics.get(key)} |")
        lines.append("")
    lines.append("## Drift")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(result.drift, indent=2, ensure_ascii=False))
    lines.append("```")
    lines.append("")
    lines.append("## Quarantine examples")
    lines.append("")
    if result.quarantine_examples:
        for item in result.quarantine_examples[:10]:
            lines.append(f"- {item.get('path')} -> {', '.join(item.get('reasons', []))}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Pivot watchlist")
    lines.append("")
    if result.pivot_watchlist:
        for item in result.pivot_watchlist[:10]:
            if "source" in item:
                lines.append(f"- {item['source']} ({item['share']})")
            elif "layer" in item:
                lines.append(f"- layer:{item['layer']} ({item['share']})")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Decision")
    lines.append("")
    if result.rollback_required:
        lines.append("- rollback or ingestion block is required")
    else:
        lines.append("- maintenance remains green")
    return "\n".join(lines)


def build_health_result(report_path: Optional[Path] = None) -> HealthResult:
    policy = load_policy()
    benchmark_path = report_path or first_existing_report()
    report = load_json(benchmark_path, {})
    metric_views = select_metrics(report)
    combined = metric_views.get("combined", {})

    previous = previous_history()
    quarantine_items = scan_primary_surface(policy)
    pivot_watchlist = detect_pivot_watchlist(report)
    monitor = QuarantineMonitor()
    legacy_decision = monitor.evaluate_metrics(
        combined,
        (previous or {}).get("metrics", {}).get("combined", {}),
    )

    alert_level, reasons, rollback_required = classify_alert(
        policy,
        combined,
        previous,
        pivot_watchlist,
        len(quarantine_items),
        production_ready=bool(report.get("production_ready", False)),
    )

    if legacy_decision.severity in {"ORANGE", "RED"} and alert_level == "GREEN":
        alert_level = legacy_decision.severity
        reasons.append("legacy_quarantine_monitor_triggered")

    if quarantine_items:
        reasons.append("quarantine_items_present")

    production_ready = bool(report.get("production_ready", False))

    drift = {
        "current": combined,
        "previous": (previous or {}).get("metrics", {}).get("combined", {}),
        "reasons": reasons,
        "legacy_quarantine_status": legacy_decision.status,
    }

    if previous:
        prev_combined = previous.get("metrics", {}).get("combined", {})
        drift["delta"] = {
            "top5_pertinent_rate": round(metric_value(combined, "top5_pertinent_rate") - metric_value(prev_combined, "top5_pertinent_rate"), 2),
            "citation_stable_rate": round(metric_value(combined, "citation_stable_rate") - metric_value(prev_combined, "citation_stable_rate"), 2),
            "citation_canonical_rate": round(metric_value(combined, "citation_canonical_rate") - metric_value(prev_combined, "citation_canonical_rate"), 2),
            "support_rate": round(metric_value(combined, "support_rate") - metric_value(prev_combined, "support_rate"), 2),
        }
    else:
        drift["delta"] = {}

    result = HealthResult(
        alert_level=alert_level,
        rollback_required=rollback_required,
        production_ready=production_ready,
        benchmark_path=str(benchmark_path),
        quarantine_count=len(quarantine_items),
        quarantine_examples=quarantine_items[:10],
        pivot_watchlist=pivot_watchlist,
        drift=drift,
        metric_views=metric_views,
        previous_alert_level=(previous or {}).get("alert_level"),
    )

    tracker = EventTracker(str(EVENT_LOG_PATH))
    tracker.log_event(
        alert_level,
        {
            "benchmark_path": str(benchmark_path),
            "production_ready": production_ready,
            "quarantine_count": len(quarantine_items),
            "rollback_required": rollback_required,
            "metrics": metric_views,
            "drift": drift,
        },
        kind="phase4_health_check",
    )

    if quarantine_items:
        for item in quarantine_items[:25]:
            tracker.log_event("RED", item, kind="quarantine")

    history_entry = {
        "timestamp": time.time(),
        "alert_level": alert_level,
        "rollback_required": rollback_required,
        "benchmark_path": str(benchmark_path),
        "metrics": metric_views,
        "quarantine_count": len(quarantine_items),
        "production_ready": production_ready,
    }
    HEALTH_HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with HEALTH_HISTORY_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(history_entry, ensure_ascii=False) + "\n")

    write_json(HEALTH_REPORT_PATH, asdict(result))
    HEALTH_MD_PATH.write_text(render_markdown(result), encoding="utf-8")

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 4 governance monitor for MDL YNOR")
    parser.add_argument("--report", type=str, default="", help="Explicit benchmark report path")
    args = parser.parse_args()

    report_path = Path(args.report).expanduser().resolve() if args.report else None
    result = build_health_result(report_path)
    print(json.dumps(asdict(result), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
