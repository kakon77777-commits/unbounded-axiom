#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import subprocess, sys

root = Path(__file__).resolve().parent
steps = [
    ("BUILD", [sys.executable, "build_parameter_tube.py"]),
    ("CENTER", [sys.executable, "verify_cross_regularity.py"]),
    ("TUBE", [sys.executable, "verify_parameter_tube.py"]),
]
lines = []
for name, cmd in steps:
    p = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
    lines.append(f"[{name}] returncode={p.returncode}")
    lines.append(p.stdout.rstrip())
    if p.stderr.strip():
        lines.append("STDERR:")
        lines.append(p.stderr.rstrip())
    if p.returncode != 0:
        text = "\n".join(lines) + "\n"
        (root / "ALL_VERIFY.txt").write_text(text, encoding="utf-8")
        raise SystemExit(p.returncode)
lines += [
    "OPTIONAL_CROSSCHECK=crosscheck_parameter_tube.py",
    "ALL_EXACT_CHECKS_OK",
    "RH_CLAIM=False",
]
text = "\n".join(lines) + "\n"
(root / "ALL_VERIFY.txt").write_text(text, encoding="utf-8")
print(text, end="")
