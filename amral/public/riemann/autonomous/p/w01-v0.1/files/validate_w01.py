from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
records = json.loads((ROOT / "RH-W-01_subgaps.json").read_text(encoding="utf-8"))
schema = json.loads((ROOT / "candidate_schema.json").read_text(encoding="utf-8"))

required_record = {
    "id", "title", "type", "severity", "status",
    "obligation", "failure_witness", "depends_on"
}

ids = [r.get("id") for r in records]
assert len(records) == 8, f"expected 8 subgaps, got {len(records)}"
assert len(ids) == len(set(ids)), "duplicate IDs"
assert ids == [f"RH-W-01-{c}" for c in "ABCDEFGH"], ids

known = set(ids)
for r in records:
    missing = required_record - set(r)
    assert not missing, f"{r.get('id')}: missing {sorted(missing)}"
    assert r["severity"] in {"S0", "S1", "S2", "S3"}
    for dep in r["depends_on"]:
        assert dep in known, f"{r['id']}: unknown dependency {dep}"

assert schema["properties"]["sign_convention"]["const"] == "Q_B0=-E_arith"
print(f"subgaps={len(records)}")
print("ids=OK")
print("dependencies=OK")
print("candidate_schema=OK")
print("VALID")
