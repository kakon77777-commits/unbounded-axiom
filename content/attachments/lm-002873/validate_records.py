#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

BASE = Path(__file__).resolve().parent
SCHEMA = json.loads((BASE / "game_intelligence_archaeology_research_unit_v0.2.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

def validate_record(record, label):
    errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
    if errors:
        print(f"[FAIL] {label}")
        for e in errors:
            path = ".".join(map(str, e.path)) or "<root>"
            print(f"  {path}: {e.message}")
        return False
    print(f"[PASS] {label}")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_records.py <record.json|records.json|records.jsonl>")
        raise SystemExit(2)

    p = Path(sys.argv[1])
    ok = True
    if p.suffix.lower() == ".jsonl":
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            ok &= validate_record(json.loads(line), f"{p.name}:{i}")
    else:
        data = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(data, list):
            for i, rec in enumerate(data):
                ok &= validate_record(rec, f"{p.name}[{i}]")
        else:
            ok &= validate_record(data, p.name)

    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
