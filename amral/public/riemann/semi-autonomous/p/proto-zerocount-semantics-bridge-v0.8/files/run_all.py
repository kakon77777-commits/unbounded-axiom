from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "run_semantic_bridge.py",
    "run_count_profile.py",
    "run_lineage_audit.py",
    "run_lower_profile_experiment.py",
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
