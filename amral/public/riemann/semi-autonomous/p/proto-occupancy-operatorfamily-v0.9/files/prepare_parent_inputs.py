from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent / "RH_IntervalGreenKernel_AtomicCertificate_v0.7"
COPIES = (
    (
        PARENT / "data" / "rational_atomic_witness_v0.6.json",
        ROOT / "data" / "parent_v0.7_rational_atomic_witness.json",
    ),
    (
        PARENT / "outputs" / "interval_atomic_certificate.json",
        ROOT / "data" / "parent_v0.7_interval_atomic_certificate.json",
    ),
)


def main() -> None:
    for source, target in COPIES:
        if not source.is_file():
            raise SystemExit(f"missing parent input: {source}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        print(f"{source.name} -> {target.name}")


if __name__ == "__main__":
    main()

