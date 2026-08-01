from __future__ import annotations

import argparse
import json
from pathlib import Path

from phase_shaping.core import PhaseShapingConfig, fit_phase_shaper
from phase_shaping.io import save_result


def main() -> None:
    parser = argparse.ArgumentParser(description="Regional Paley-Wiener phase shaper")
    parser.add_argument("--config", required=True, help="Path to a JSON config")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()

    raw = json.loads(Path(args.config).read_text(encoding="utf-8"))
    config = PhaseShapingConfig(**raw)
    result = fit_phase_shaper(config)
    save_result(result, args.output)

    summary = result.summary_dict()
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
