from __future__ import annotations

import argparse
import json

from validated_certificate.certificate import run_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="examples/certificate.json")
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()
    result = run_certificate(args.config, args.output)
    print(json.dumps({
        "passed": result["strict_intersection_certificate_passed"],
        "region_upper": result["region"]["global_block_upper"],
        "arithmetic_interval": result["arithmetic"]["arithmetic_total_interval"],
        "certified_cells": result["region"]["certified_cell_count"],
        "unresolved_cells": result["region"]["unresolved_cell_count"],
    }, indent=2))


if __name__ == "__main__":
    main()
