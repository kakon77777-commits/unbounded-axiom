from __future__ import annotations

import copy
import json
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

from local_green.box_certificate import build_box_certificate


ROOT = Path(__file__).resolve().parent
WITNESS_PATH = ROOT / "data" / "parent_v0.7_rational_atomic_witness.json"
FLOATING_PATH = ROOT / "data" / "parent_v0.9_floating_location_study.json"
OUTPUT = ROOT / "outputs"
MAXIMUM_PASSING_RADIUS = Fraction(89, 50_000_000)
FIRST_FAILED_BRACKET_RADIUS = Fraction(9, 5_000_000)
CORNER_POINT_RADIUS = Fraction(1, 1_000)
RADIUS_LADDER = (
    ("center", Fraction(0)),
    ("requested_1e-8", Fraction(1, 100_000_000)),
    ("requested_1e-6", Fraction(1, 1_000_000)),
    ("strongest_tested_pass", MAXIMUM_PASSING_RADIUS),
    ("first_tested_boundary_failure", FIRST_FAILED_BRACKET_RADIUS),
    ("requested_1e-4", Fraction(1, 10_000)),
    ("requested_1e-3", Fraction(1, 1_000)),
)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            value,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def fraction_string(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_row(value: Fraction) -> dict[str, int]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def source_fraction(row: dict[str, int]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def certificate_summary(
    label: str,
    radius: Fraction,
    certificate: dict[str, Any],
) -> dict[str, Any]:
    proof = certificate["proof"]
    return {
        "label": label,
        "axis_cell_half_width": fraction_string(radius),
        "axis_cell_half_width_decimal": format(float(radius), ".12g"),
        "certificate_pass": proof["certificate_pass"],
        "failure_class": proof["failure_class"],
        "neumann_defect_infinity_norm_upper": proof[
            "neumann_defect_infinity_norm_upper"
        ],
        "first_leading_minor_lower": proof.get(
            "first_leading_minor_lower"
        ),
        "determinant_lower": proof.get("determinant_lower"),
        "maximum_projected_interval_width": certificate[
            "green_kernel"
        ]["maximum_projected_interval_width"],
        "failure_is_point_counterexample": False,
    }


def build_cover_family(
    witness: dict[str, Any],
) -> dict[str, Any]:
    cells = []
    for band_index, support in enumerate(witness["axis_supports"]):
        for atom_index, atom in enumerate(support):
            center = source_fraction(atom["x"])
            cells.append(
                {
                    "atom_id": f"b{band_index}_a{atom_index}",
                    "band_index": band_index,
                    "center": fraction_string(center),
                    "closed_cell": {
                        "lo": fraction_string(
                            center - MAXIMUM_PASSING_RADIUS
                        ),
                        "hi": fraction_string(
                            center + MAXIMUM_PASSING_RADIUS
                        ),
                    },
                }
            )
    return {
        "schema": "RH.LocalIntervalGreen.DownwardClosedCoverFamily.v1.0",
        "node": "RH-LocalIntervalGreen-CellCover-20260725-v1.0",
        "coordinate_count": len(cells),
        "band_count": len(witness["axis_supports"]),
        "band_atom_counts": [
            len(support)
            for support in witness["axis_supports"]
        ],
        "maximal_product_box": {
            "uniform_half_width": fraction_string(
                MAXIMUM_PASSING_RADIUS
            ),
            "leaf_count": 1,
            "cells": cells,
        },
        "family_rule": (
            "Every Cartesian product of closed rational subintervals "
            "contained coordinatewise in the maximal product box "
            "inherits the maximal-box certificate."
        ),
        "coverage": {
            "all_58_locations_vary_independently": True,
            "maximal_product_box_covered": True,
            "downward_closed_subbox_family_covered": True,
        },
        "classification": {
            "abstract_local_location_cover_family": True,
            "actual_zeta_occupancy_family": False,
            "explicit_formula_transfer_certified": False,
            "global_rh_certificate": False,
        },
    }


def build_corner_witness(
    witness: dict[str, Any],
    floating: dict[str, Any],
) -> dict[str, Any]:
    result = copy.deepcopy(witness)
    source_row = next(
        row
        for row in floating["adversarial_corner_rows"]
        if abs(float(row["cell_half_width"]) - 0.016) < 1e-12
    )
    signs = iter(source_row["corner_signs"])
    coordinates = []
    for band_index, support in enumerate(result["axis_supports"]):
        for atom_index, atom in enumerate(support):
            sign = int(next(signs))
            center = source_fraction(atom["x"])
            shifted = center + sign * CORNER_POINT_RADIUS
            atom["x"] = fraction_row(shifted)
            coordinates.append(
                {
                    "atom_id": f"b{band_index}_a{atom_index}",
                    "parent_center": fraction_string(center),
                    "sign": sign,
                    "shifted_center": fraction_string(shifted),
                }
            )
    result["v1.0_corner_point_provenance"] = {
        "source": (
            "parent v0.9 deterministic adversarial signs selected at "
            "floating half-width 0.016"
        ),
        "exact_shift_radius": fraction_string(CORNER_POINT_RADIUS),
        "coordinates": coordinates,
        "classification": {
            "single_exact_rational_point": True,
            "universal_box_statement": False,
            "global_rh_certificate": False,
        },
    }
    return result


def main() -> None:
    witness = json.loads(WITNESS_PATH.read_text(encoding="utf-8"))
    floating = json.loads(FLOATING_PATH.read_text(encoding="utf-8"))
    rows = []
    maximum_certificate = None
    for label, radius in RADIUS_LADDER:
        started = time.perf_counter()
        certificate = build_box_certificate(witness, radius)
        elapsed = time.perf_counter() - started
        rows.append(
            certificate_summary(
                label,
                radius,
                certificate,
            )
        )
        print(
            json.dumps(
                {
                    "label": label,
                    "radius": fraction_string(radius),
                    "pass": certificate["proof"][
                        "certificate_pass"
                    ],
                    "failure": certificate["proof"]["failure_class"],
                    "seconds": elapsed,
                }
            ),
            flush=True,
        )
        if radius == MAXIMUM_PASSING_RADIUS:
            maximum_certificate = certificate

    if maximum_certificate is None:
        raise RuntimeError("maximum certificate was not generated")
    if not maximum_certificate["proof"]["certificate_pass"]:
        raise ArithmeticError("declared maximal tested radius did not pass")

    boundary_row = next(
        row
        for row in rows
        if row["label"] == "first_tested_boundary_failure"
    )
    if boundary_row["certificate_pass"]:
        raise ArithmeticError("declared failure bracket unexpectedly passed")

    ladder = {
        "schema": "RH.LocalIntervalGreen.RadiusLadder.v1.0",
        "node": "RH-LocalIntervalGreen-CellCover-20260725-v1.0",
        "child_alpha": "1/1",
        "axis_location_dimension": 58,
        "rows": rows,
        "certified_uniform_half_width": fraction_string(
            MAXIMUM_PASSING_RADIUS
        ),
        "first_tested_failure_above_certified_width": (
            fraction_string(FIRST_FAILED_BRACKET_RADIUS)
        ),
        "boundary_bracket_decimal": [
            format(float(MAXIMUM_PASSING_RADIUS), ".12g"),
            format(float(FIRST_FAILED_BRACKET_RADIUS), ".12g"),
        ],
        "parent_v0.9_uniform_half_width": "1/500000000000000",
        "exact_radius_improvement_factor": fraction_string(
            MAXIMUM_PASSING_RADIUS
            / Fraction(1, 500_000_000_000_000)
        ),
        "classification": {
            "universal_58cell_interval_certificate": True,
            "failed_rows_are_point_counterexamples": False,
            "actual_zeta_occupancy_family": False,
            "global_rh_certificate": False,
        },
    }
    cover_family = build_cover_family(witness)

    corner_witness = build_corner_witness(witness, floating)
    corner_started = time.perf_counter()
    corner_certificate = build_box_certificate(
        corner_witness,
        Fraction(0),
    )
    corner_elapsed = time.perf_counter() - corner_started
    if not corner_certificate["proof"]["certificate_pass"]:
        raise ArithmeticError(
            "deterministic failed-box corner point did not pass"
        )
    corner_certificate["diagnostic_role"] = {
        "exact_shift_radius": fraction_string(CORNER_POINT_RADIUS),
        "source_sign_pattern": (
            "parent v0.9 floating adversarial corner at width 0.016"
        ),
        "interpretation": (
            "A rigorously passing point inside the failed h=1e-3 "
            "universal box proves that box-enclosure failure is not "
            "itself a point counterexample."
        ),
    }

    write_json(
        OUTPUT / "local_green_cell_certificate_h178e-8.json",
        maximum_certificate,
    )
    write_json(
        OUTPUT / "local_green_radius_ladder.json",
        ladder,
    )
    write_json(
        OUTPUT / "local_green_cover_family.json",
        cover_family,
    )
    write_json(
        ROOT / "data" / "adversarial_corner_witness_h1e-3.json",
        corner_witness,
    )
    write_json(
        OUTPUT / "adversarial_corner_point_certificate_h1e-3.json",
        corner_certificate,
    )


if __name__ == "__main__":
    main()
