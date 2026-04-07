from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


DEFAULT_PROFILE: Dict[str, Any] = {
 "name": "Ynor Market Quant v1",
 "entry_threshold": 3.0,
 "exit_threshold": -1.0,
 "risk": {
 "trail_factor": 0.5,
 "max_volatility": 0.06,
 },
 "weights": {
 "trend": 1.5,
 "momentum": 1.0,
 "volume": 1.0,
 "breakout": 1.5,
 "sweep": 1.5,
 "volatility": -1.0,
 },
}


def load_strategy_profile(path: str | None) -> Dict[str, Any]:
 if not path:
 return DEFAULT_PROFILE

 profile_path = Path(path)
 if not profile_path.exists():
 return DEFAULT_PROFILE

 with profile_path.open("r", encoding="utf-8") as f:
 data = json.load(f)

 merged = DEFAULT_PROFILE.copy()
 merged.update(data)
 merged.setdefault("risk", {}).update(data.get("risk", {}))
 merged.setdefault("weights", {}).update(data.get("weights", {}))
 return merged


def score_market(features: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
 weights = profile.get("weights", {})
 risk = profile.get("risk", {})
 components: Dict[str, float] = {}

 trend = 1.0 if features.get("ema_fast", 0.0) > features.get("ema_slow", 0.0) else -1.0
 components["trend"] = weights.get("trend", 0.0) * trend

 momentum = 0.0
 if features.get("momentum_5", 0.0) > 0:
 momentum += 0.5
 if features.get("momentum_20", 0.0) > 0:
 momentum += 0.5
 components["momentum"] = weights.get("momentum", 0.0) * momentum

 volume_ratio = float(features.get("volume_ratio_20", 0.0))
 components["volume"] = weights.get("volume", 0.0) * (1.0 if volume_ratio >= 1.1 else 0.0)

 components["breakout"] = weights.get("breakout", 0.0) * (1.0 if features.get("breakout_20") else 0.0)
 components["sweep"] = weights.get("sweep", 0.0) * (1.0 if features.get("sweep_reversal") else 0.0)

 volatility = float(features.get("volatility_20", 0.0))
 components["volatility"] = weights.get("volatility", 0.0) if volatility > float(risk.get("max_volatility", 1.0)) else 0.0

 score = float(sum(components.values()))
 decision = "hold"
 if score >= float(profile.get("entry_threshold", 3.0)):
 decision = "buy"
 elif score <= float(profile.get("exit_threshold", -1.0)):
 decision = "sell"

 return {
 "score": score,
 "decision": decision,
 "components": components,
 "entry_threshold": profile.get("entry_threshold", 3.0),
 "exit_threshold": profile.get("exit_threshold", -1.0),
 }
