from __future__ import annotations

import argparse
import json
from pathlib import Path

from intersection_solver import IntersectionConfig, run_scan
from intersection_solver.io import save_outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="RH separation-positivity intersection prototype")
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()

    raw = json.loads(Path(args.config).read_text(encoding="utf-8"))
    raw["support_radii"] = tuple(raw["support_radii"])
    config = IntersectionConfig(**raw)
    results = run_scan(config)
    save_outputs(config, results, args.output)

    print(
        "R       primes  min_eig(A)   q_A(c)       max_block(check)  intersection  optimizer"
    )
    for result in results:
        print(
            f"{result.support_radius:>4.1f}  "
            f"{len(result.activated_prime_powers):>7d}  "
            f"{result.arithmetic_min_eigenvalue:>11.4e}  "
            f"{result.arithmetic_value:>11.4e}  "
            f"{result.check_grid_max_block:>16.4e}  "
            f"{str(result.intersection_found_on_grid):>12s}  "
            f"{str(result.optimizer_success):>9s}"
        )


if __name__ == "__main__":
    main()
