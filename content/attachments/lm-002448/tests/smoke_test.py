#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cdi_runtime_mvp import demo, smoke_assert

db = ROOT / "tests" / "cdi_smoke.db"
result = demo(db)
smoke_assert(result)
out = ROOT / "tests" / "MVP_SMOKE_TEST.json"
out.write_text(json.dumps({"status":"PASS","result":result}, ensure_ascii=False, indent=2), encoding="utf-8")
print("PASS")
print(out)
