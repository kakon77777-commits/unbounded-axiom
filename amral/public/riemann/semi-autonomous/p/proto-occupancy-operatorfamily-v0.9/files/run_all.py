from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "run_semantic_bridge.py",
    "generate_cover_certificate.py",
    "verify_cover_certificate.py",
    "run_clamped_radius_certificate.py",
    "verify_clamped_radius_certificate.py",
    "run_floating_clamped_study.py",
    "run_summary.py",
    "verify_outputs.py",
    "validate_package.py",
)


def main() -> None:
    for script in SCRIPTS:
        subprocess.run(
            [sys.executable, str(ROOT / script)],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    main()

