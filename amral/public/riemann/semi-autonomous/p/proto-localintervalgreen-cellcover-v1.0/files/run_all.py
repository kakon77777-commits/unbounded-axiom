from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "generate_cell_cover.py",
    "verify_cell_cover.py",
    "run_summary.py",
    "run_tests.py",
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
