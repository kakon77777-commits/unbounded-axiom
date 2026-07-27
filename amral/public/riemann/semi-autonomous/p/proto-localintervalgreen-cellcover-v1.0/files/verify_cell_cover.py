from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from local_green.box_certificate import (
    canonical_json_hash,
    verify_box_certificate,
)


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUTPUT = ROOT / "outputs"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_fraction(value: str) -> Fraction:
    numerator, denominator = value.split("/")
    return Fraction(int(numerator), int(denominator))


def verify_cover_family(
    witness: dict[str, Any],
    family: dict[str, Any],
    certified_radius: Fraction,
) -> dict[str, Any]:
    cells = family["maximal_product_box"]["cells"]
    expected = []
    for band_index, support in enumerate(witness["axis_supports"]):
        for atom_index, atom in enumerate(support):
            center = Fraction(
                atom["x"]["numerator"],
                atom["x"]["denominator"],
            )
            expected.append(
                {
                    "atom_id": f"b{band_index}_a{atom_index}",
                    "band_index": band_index,
                    "center": center,
                    "lo": center - certified_radius,
                    "hi": center + certified_radius,
                }
            )
    checks = {
        "coordinate_count_58": (
            family["coordinate_count"] == len(cells) == 58
        ),
        "band_counts": (
            family["band_atom_counts"] == [22, 5, 14, 9, 8]
        ),
        "uniform_radius_matches_certificate": (
            parse_fraction(
                family["maximal_product_box"][
                    "uniform_half_width"
                ]
            )
            == certified_radius
        ),
        "all_exact_cells_match": all(
            row["atom_id"] == target["atom_id"]
            and row["band_index"] == target["band_index"]
            and parse_fraction(row["center"]) == target["center"]
            and parse_fraction(row["closed_cell"]["lo"])
            == target["lo"]
            and parse_fraction(row["closed_cell"]["hi"])
            == target["hi"]
            for row, target in zip(cells, expected)
        ),
        "coverage_flags_true": all(
            family["coverage"][key] is True
            for key in (
                "all_58_locations_vary_independently",
                "maximal_product_box_covered",
                "downward_closed_subbox_family_covered",
            )
        ),
        "actual_zeta_flag_false": (
            family["classification"][
                "actual_zeta_occupancy_family"
            ]
            is False
        ),
        "global_flag_false": (
            family["classification"]["global_rh_certificate"]
            is False
        ),
    }
    return {
        "checks": checks,
        "verification_pass": all(checks.values()),
    }


def main() -> None:
    witness_path = DATA / "parent_v0.7_rational_atomic_witness.json"
    parent_certificate_path = (
        DATA / "parent_v0.7_interval_atomic_certificate.json"
    )
    witness = read_json(witness_path)
    parent_certificate = read_json(parent_certificate_path)
    certificate = read_json(
        OUTPUT / "local_green_cell_certificate_h178e-8.json"
    )
    certificate_verification = verify_box_certificate(
        witness,
        certificate,
    )
    write_json(
        OUTPUT / "local_green_cell_verification_h178e-8.json",
        certificate_verification,
    )

    corner_witness = read_json(
        DATA / "adversarial_corner_witness_h1e-3.json"
    )
    corner_certificate = read_json(
        OUTPUT / "adversarial_corner_point_certificate_h1e-3.json"
    )
    corner_verification = verify_box_certificate(
        corner_witness,
        corner_certificate,
    )
    write_json(
        OUTPUT / "adversarial_corner_point_verification_h1e-3.json",
        corner_verification,
    )

    ladder = read_json(OUTPUT / "local_green_radius_ladder.json")
    rows = {row["label"]: row for row in ladder["rows"]}
    certified_radius = parse_fraction(
        ladder["certified_uniform_half_width"]
    )
    family = read_json(OUTPUT / "local_green_cover_family.json")
    family_verification = verify_cover_family(
        witness,
        family,
        certified_radius,
    )
    write_json(
        OUTPUT / "local_green_cover_family_verification.json",
        family_verification,
    )

    parent_checks = {
        "canonical_witness_hash_matches_parent": (
            canonical_json_hash(witness)
            == parent_certificate["input"][
                "canonical_witness_sha256"
            ]
        ),
        "parent_abstract_certificate_true": (
            parent_certificate["classification"][
                "abstract_continuous_interval_certificate"
            ]
            is True
        ),
        "parent_strict_positivity_true": (
            parent_certificate["classification"][
                "abstract_operator_strictly_positive"
            ]
            is True
        ),
        "parent_global_flag_false": (
            parent_certificate["classification"][
                "global_rh_certificate"
            ]
            is False
        ),
    }
    ladder_checks = {
        "requested_1e-8_pass": rows["requested_1e-8"][
            "certificate_pass"
        ],
        "requested_1e-6_pass": rows["requested_1e-6"][
            "certificate_pass"
        ],
        "strongest_tested_pass": rows["strongest_tested_pass"][
            "certificate_pass"
        ],
        "boundary_failure_is_sylvester": (
            rows["first_tested_boundary_failure"][
                "certificate_pass"
            ]
            is False
            and rows["first_tested_boundary_failure"]["failure_class"]
            == "sylvester_lower_bound_failure"
        ),
        "requested_1e-4_is_neumann_inconclusive": (
            rows["requested_1e-4"]["certificate_pass"] is False
            and rows["requested_1e-4"]["failure_class"]
            == "neumann_inverse_failure"
        ),
        "requested_1e-3_is_neumann_inconclusive": (
            rows["requested_1e-3"]["certificate_pass"] is False
            and rows["requested_1e-3"]["failure_class"]
            == "neumann_inverse_failure"
        ),
        "exact_improvement_factor": (
            parse_fraction(
                ladder["exact_radius_improvement_factor"]
            )
            == 890_000_000
        ),
    }
    corner_checks = {
        "point_certificate_pass": corner_verification[
            "certificate_pass"
        ],
        "point_verification_pass": corner_verification[
            "verification_pass"
        ],
        "point_shift_is_1e-3": (
            parse_fraction(
                corner_certificate["diagnostic_role"][
                    "exact_shift_radius"
                ]
            )
            == Fraction(1, 1_000)
        ),
        "point_does_not_claim_universal_box": (
            corner_witness["v1.0_corner_point_provenance"][
                "classification"
            ]["universal_box_statement"]
            is False
        ),
    }
    checks = {
        "maximum_certificate_verifies": certificate_verification[
            "verification_pass"
        ],
        "maximum_certificate_passes": certificate_verification[
            "certificate_pass"
        ],
        "cover_family_verifies": family_verification[
            "verification_pass"
        ],
        "parent_dependency_verifies": all(parent_checks.values()),
        "radius_ladder_verifies": all(ladder_checks.values()),
        "corner_diagnostic_verifies": all(corner_checks.values()),
        "maximum_certificate_actual_zeta_false": (
            certificate["classification"][
                "actual_zeta_occupancy_family"
            ]
            is False
        ),
        "maximum_certificate_global_false": (
            certificate["classification"][
                "global_rh_certificate"
            ]
            is False
        ),
    }
    result = {
        "schema": "RH.LocalIntervalGreen.OutputVerification.v1.0",
        "checks": checks,
        "parent_checks": parent_checks,
        "ladder_checks": ladder_checks,
        "corner_checks": corner_checks,
        "input_file_sha256": {
            witness_path.name: sha256(witness_path),
            parent_certificate_path.name: sha256(
                parent_certificate_path
            ),
        },
        "verification_pass": all(checks.values()),
        "actual_zeta_occupancy_family": False,
        "global_rh_certificate": False,
    }
    write_json(OUTPUT / "output_verification.json", result)
    if not result["verification_pass"]:
        raise SystemExit(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
