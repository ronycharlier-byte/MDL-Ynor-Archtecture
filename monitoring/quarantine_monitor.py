from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional


@dataclass(frozen=True)
class QuarantineDecision:
    status: str
    severity: str
    reasons: List[str]
    rollback_required: bool


class QuarantineMonitor:
    """
    Phase 4 maintenance guard.

    Legacy update(s1, rayleigh_p) remains available, but the main use is
    metric-based production monitoring.
    """

    def __init__(
        self,
        s1_threshold: float = 0.15,
        p_threshold: float = 0.05,
        top5_min: float = 70.0,
        citation_stable_min: float = 90.0,
        citation_canonical_min: float = 95.0,
        support_min: float = 60.0,
    ):
        self.s1_threshold = s1_threshold
        self.p_threshold = p_threshold
        self.top5_min = top5_min
        self.citation_stable_min = citation_stable_min
        self.citation_canonical_min = citation_canonical_min
        self.support_min = support_min
        self.status = "STABLE"
        self.history: List[float] = []

    def update(self, s1: float, rayleigh_p: float) -> str:
        self.history.append(s1)

        if s1 > self.s1_threshold or rayleigh_p < self.p_threshold:
            self.status = "QUARANTINE"
        elif s1 > 0.10:
            self.status = "MONITORING"
        else:
            self.status = "STABLE"

        return self.status

    def get_gdi(self) -> float:
        """Ghost Drift Index."""
        if len(self.history) < 2:
            return 0.0
        return abs(self.history[-1] - self.history[-2])

    def evaluate_metrics(
        self,
        metrics: Mapping[str, Any],
        previous: Optional[Mapping[str, Any]] = None,
    ) -> QuarantineDecision:
        reasons: List[str] = []
        severity = "GREEN"

        top5 = float(metrics.get("top5_pertinent_rate", 0.0))
        citation_stable = float(metrics.get("citation_stable_rate", 0.0))
        citation_canonical = float(metrics.get("citation_canonical_rate", 0.0))
        archive_leak = float(metrics.get("archive_leak_rate", 0.0))
        tech_leak = float(metrics.get("tech_leak_rate", 0.0))
        no_valid_source = float(metrics.get("no_valid_source_rate", 0.0))
        monopoly = float(metrics.get("monopoly_violation_rate", 0.0))
        support_rate = float(metrics.get("support_rate", metrics.get("support_coverage", 0.0)))
        concentration = float(metrics.get("average_concentration", 0.0))

        hard_fail = (
            top5 < self.top5_min
            or citation_stable < self.citation_stable_min
            or citation_canonical < self.citation_canonical_min
            or archive_leak > 0.0
            or tech_leak > 0.0
            or no_valid_source > 0.0
            or monopoly > 0.0
        )
        if hard_fail:
            severity = "RED"

        if support_rate < self.support_min and severity == "GREEN":
            severity = "ORANGE"
            reasons.append(f"support_rate_below_{self.support_min}")

        if concentration > 0.25 and severity == "GREEN":
            severity = "YELLOW"
            reasons.append("topk_concentration_high")

        if previous:
            prev_top5 = float(previous.get("top5_pertinent_rate", top5))
            prev_citation_stable = float(previous.get("citation_stable_rate", citation_stable))
            prev_support_rate = float(previous.get("support_rate", support_rate))
            if prev_top5 - top5 >= 2.0 and severity == "GREEN":
                severity = "YELLOW"
                reasons.append("top5_regression_light")
            if prev_top5 - top5 >= 5.0 and severity in {"GREEN", "YELLOW"}:
                severity = "ORANGE"
                reasons.append("top5_regression_material")
            if prev_citation_stable - citation_stable >= 2.0 and severity == "GREEN":
                severity = "YELLOW"
                reasons.append("citation_stability_drift")
            if prev_citation_stable - citation_stable >= 5.0 and severity in {"GREEN", "YELLOW"}:
                severity = "ORANGE"
                reasons.append("citation_stability_material_drift")
            if prev_support_rate - support_rate >= 5.0 and severity == "GREEN":
                severity = "YELLOW"
                reasons.append("support_coverage_soft_drop")

        if hard_fail:
            reasons.extend(
                [
                    "top5_below_gate" if top5 < self.top5_min else "",
                    "citation_stable_below_gate" if citation_stable < self.citation_stable_min else "",
                    "citation_canonical_below_gate" if citation_canonical < self.citation_canonical_min else "",
                    "archive_leak_detected" if archive_leak > 0.0 else "",
                    "tech_leak_detected" if tech_leak > 0.0 else "",
                    "no_valid_source_detected" if no_valid_source > 0.0 else "",
                    "monopoly_violation_detected" if monopoly > 0.0 else "",
                ]
            )
            reasons = [reason for reason in reasons if reason]

        rollback_required = severity in {"RED", "ORANGE"} and (
            archive_leak > 0.0
            or tech_leak > 0.0
            or no_valid_source > 0.0
            or top5 < self.top5_min
            or citation_stable < self.citation_stable_min
        )

        return QuarantineDecision(
            status=severity,
            severity=severity,
            reasons=reasons,
            rollback_required=rollback_required,
        )
