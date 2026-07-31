"""Moser Skew Lab v0.13 result replay."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
summary = json.loads(
    (root / "data" / "round13_summary.json").read_text(encoding="utf-8")
)
print(json.dumps(summary["round13_candidate"], indent=2))
print("KKT rank:", summary["smooth_event_kkt"]["jacobian_rank"])
print(
    "stationarity residual:",
    summary["smooth_event_kkt"]["weighted_stationarity_norm"],
)
