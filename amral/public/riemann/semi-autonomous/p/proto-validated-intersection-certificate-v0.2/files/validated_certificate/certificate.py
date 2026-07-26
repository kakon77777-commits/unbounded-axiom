from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path

from .arithmetic import certify_arithmetic
from .model import HatSplineModel
from .region import certify_region


def load_config(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def run_certificate(config_path: str | Path, output_dir: str | Path) -> dict:
    config_path = Path(config_path).resolve()
    config = load_config(config_path)
    project_root = config_path.parent.parent
    node_file = project_root / config["node_file"]
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    model = HatSplineModel.from_csv(node_file, dps=int(config["interval_dps"]))
    region = certify_region(
        model,
        config["x_min"],
        config["x_max"],
        config["y_min"],
        config["y_max"],
        int(config["initial_nx"]),
        int(config["initial_ny"]),
        int(config["max_depth"]),
    )
    arithmetic = certify_arithmetic(
        model,
        float(config["first_interval_step"]),
        float(config["near_zero_midpoint_step"]),
        float(config["far_midpoint_step"]),
        float(config["near_zero_chunk"]),
        float(config["far_chunk"]),
    )
    result = {
        "format": "RH-VALIDATED-INTERSECTION-CERTIFICATE-0.2",
        "model": {
            "spline_node_count": model.size,
            "spline_spacing": [float(model.h.a), float(model.h.b)],
            "support_radius": [float(model.support_radius.a), float(model.support_radius.b)],
            "function_definition": (
                "psi(t)=sum_i y_i max(1-|t-t_i|/h,0), with the central ordinate "
                "defined by the exact endpoint-correction ratio in the verifier"
            ),
        },
        "region": region.to_dict(),
        "arithmetic": arithmetic,
        "strict_intersection_certificate_passed": (
            region.to_dict()["continuous_region_certified_negative"]
            and arithmetic["arithmetic_scalar_certified_positive"]
        ),
        "scope_warning": (
            "This certifies one explicitly defined piecewise-linear finite-dimensional test "
            "function in the stated normalization. It does not control contributions of all "
            "other zeta zeros and does not prove the Riemann hypothesis. The verifier relies "
            "on mpmath interval arithmetic rather than a proof-assistant kernel."
        ),
        "config": config,
    }
    with (output / "certificate.json").open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    with (output / "certified_region_cells.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(region.certified[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(cell) for cell in region.certified)
    with (output / "unresolved_region_cells.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["x_lo", "x_hi", "y_lo", "y_hi", "depth", "block_upper"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(asdict(cell) for cell in region.unresolved)
    return result
