from __future__ import annotations

import argparse
import json
from pathlib import Path

from validated_certificate.certificate import run_certificate


def main() -> None:
    parser = argparse.ArgumentParser(description="Replay the validated certificate from source data")
    parser.add_argument("--config", default="examples/certificate.json")
    parser.add_argument("--output", default="outputs/replay")
    parser.add_argument("--reference", default="outputs/certificate.json")
    args = parser.parse_args()
    replay = run_certificate(args.config, args.output)
    reference = json.loads(Path(args.reference).read_text(encoding="utf-8"))
    checks = {
        "replay_passed": replay["strict_intersection_certificate_passed"],
        "reference_passed": reference["strict_intersection_certificate_passed"],
        "region_upper_negative": replay["region"]["global_block_upper"] < 0,
        "arithmetic_lower_positive": replay["arithmetic"]["arithmetic_total_interval"][0] > 0,
        "no_unresolved_cells": replay["region"]["unresolved_cell_count"] == 0,
    }
    print(json.dumps(checks, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
