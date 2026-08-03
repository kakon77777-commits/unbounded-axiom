from __future__ import annotations

import argparse
import json
from pathlib import Path

from arithmetic_psd import ArithmeticScanConfig, run_scan
from arithmetic_psd.io import save_scan


def main() -> None:
    parser = argparse.ArgumentParser(description="RH arithmetic matrix / PSD research prototype")
    parser.add_argument("--config", required=True, help="Path to a JSON config")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()

    raw = json.loads(Path(args.config).read_text(encoding="utf-8"))
    raw["support_radii"] = tuple(raw["support_radii"])
    config = ArithmeticScanConfig(**raw)
    results = run_scan(config)
    save_scan(config, results, args.output)

    print("support_radius  activated  min_arch       min_finite     min_total      PSD?")
    for result in results:
        print(
            f"{result.support_radius:>13.4f}  "
            f"{len(result.activated_prime_powers):>9d}  "
            f"{result.min_eigen_archimedean:>12.5e}  "
            f"{result.min_eigen_finite:>12.5e}  "
            f"{result.min_eigen_total:>12.5e}  "
            f"{str(result.numerical_psd):>5s}"
        )


if __name__ == "__main__":
    main()
