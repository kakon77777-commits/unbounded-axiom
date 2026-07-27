from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from typing import Any

from .dirichlet_green import interval_proof_json, schur_interval
from .rational_interval import QInterval, as_fraction, fraction_text


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def root_box(model: dict[str, Any]) -> list[QInterval]:
    return [
        QInterval(
            as_fraction(row["interval"]["lo"]),
            as_fraction(row["interval"]["hi"]),
        )
        for row in model["occupancy_cells"]
    ]


def box_json(box: list[QInterval]) -> list[dict[str, str]]:
    return [value.to_json() for value in box]


def split_box(
    box: list[QInterval],
) -> tuple[int, Fraction, list[QInterval], list[QInterval]]:
    dimension = max(
        range(len(box)),
        key=lambda index: (box[index].width, -index),
    )
    midpoint = box[dimension].midpoint
    left = list(box)
    right = list(box)
    left[dimension] = QInterval(box[dimension].lo, midpoint)
    right[dimension] = QInterval(midpoint, box[dimension].hi)
    return dimension, midpoint, left, right


def generate_cover(
    model: dict[str, Any],
    max_depth: int = 12,
) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    leaves: list[dict[str, Any]] = []
    unresolved: list[str] = []

    def visit(box: list[QInterval], path: str, depth: int) -> None:
        proof = schur_interval(box, model)
        record: dict[str, Any] = {
            "path": path,
            "depth": depth,
            "box": box_json(box),
            "proof": interval_proof_json(proof),
        }
        if proof["sylvester_positive"]:
            record["status"] = "certified_leaf"
            nodes.append(record)
            leaves.append(record)
            return
        if depth >= max_depth:
            record["status"] = "unresolved_leaf"
            nodes.append(record)
            unresolved.append(path)
            return
        dimension, midpoint, left, right = split_box(box)
        record.update(
            {
                "status": "split_inconclusive",
                "split_dimension": dimension,
                "split_midpoint": fraction_text(midpoint),
                "children": [path + "0", path + "1"],
            }
        )
        nodes.append(record)
        visit(left, path + "0", depth + 1)
        visit(right, path + "1", depth + 1)

    visit(root_box(model), "", 0)
    nodes.sort(key=lambda row: (len(row["path"]), row["path"]))
    leaves.sort(key=lambda row: row["path"])
    minimum_first = min(
        as_fraction(row["proof"]["first_leading_minor"]["lo"])
        for row in leaves
    )
    minimum_determinant = min(
        as_fraction(row["proof"]["schur_determinant"]["lo"])
        for row in leaves
    )
    return {
        "schema": "RH.Occupancy.DirichletGreenCoverCertificate.v0.9",
        "node": "RH-Occupancy-OperatorFamily-20260725-v0.9",
        "model_sha256": canonical_json_hash(model),
        "statement": {
            "kernel": model["kernel"],
            "operator": (
                "I + sum_r lambda_r k_xr tensor k_xr "
                "- sum_a beta_a k_ya tensor k_ya"
            ),
            "quantifier": (
                "for every independent location x_r in its certified "
                "closed occupancy hull"
            ),
        },
        "root_box": box_json(root_box(model)),
        "algorithm": {
            "arithmetic": "exact Fraction interval arithmetic",
            "split_rule": "widest coordinate; lowest index on ties; midpoint",
            "max_depth": max_depth,
            "schur_rank": 2,
            "sylvester_rule": "S_11 lower > 0 and det(S) lower > 0",
        },
        "nodes": nodes,
        "leaf_paths": [row["path"] for row in leaves],
        "statistics": {
            "node_count": len(nodes),
            "certified_leaf_count": len(leaves),
            "unresolved_leaf_count": len(unresolved),
            "maximum_leaf_depth": max(row["depth"] for row in leaves),
            "minimum_first_minor_lower": fraction_text(minimum_first),
            "minimum_determinant_lower": fraction_text(
                minimum_determinant
            ),
            "root_box_directly_certified": bool(
                nodes[0]["status"] == "certified_leaf"
            ),
        },
        "classification": {
            "exact_rational_cover_certificate": not unresolved,
            "universal_uncertain_location_operator_family": (
                not unresolved
            ),
            "occupancy_premise_source": "synthetic_axiom",
            "zeta_facing_occupancy_certificate": False,
            "global_rh_certificate": False,
        },
    }


def verify_cover(
    model: dict[str, Any],
    certificate: dict[str, Any],
) -> dict[str, Any]:
    max_depth = int(certificate["algorithm"]["max_depth"])
    regenerated = generate_cover(model, max_depth=max_depth)
    paths = certificate["leaf_paths"]
    checks = {
        "schema": (
            certificate.get("schema")
            == "RH.Occupancy.DirichletGreenCoverCertificate.v0.9"
        ),
        "model_hash": (
            certificate.get("model_sha256")
            == canonical_json_hash(model)
        ),
        "exact_regeneration": certificate == regenerated,
        "leaf_paths_unique": len(paths) == len(set(paths)),
        "leaf_paths_prefix_free": all(
            not (
                left != right
                and right.startswith(left)
            )
            for left in paths
            for right in paths
        ),
        "adaptive_split_required": (
            not certificate["statistics"]["root_box_directly_certified"]
            and certificate["statistics"]["certified_leaf_count"] > 1
        ),
        "no_unresolved_leaves": (
            certificate["statistics"]["unresolved_leaf_count"] == 0
        ),
        "strict_leaf_sylvester": all(
            row["proof"]["sylvester_positive"]
            for row in certificate["nodes"]
            if row["status"] == "certified_leaf"
        ),
        "zeta_flag_false": (
            certificate["classification"][
                "zeta_facing_occupancy_certificate"
            ]
            is False
        ),
        "global_flag_false": (
            certificate["classification"]["global_rh_certificate"]
            is False
        ),
    }
    return {
        "schema": "RH.Occupancy.DirichletGreenCoverVerification.v0.9",
        "checks": checks,
        "verification_pass": all(checks.values()),
        "recomputed_leaf_count": regenerated["statistics"][
            "certified_leaf_count"
        ],
        "recomputed_maximum_depth": regenerated["statistics"][
            "maximum_leaf_depth"
        ],
        "recomputed_minimum_determinant_lower": regenerated[
            "statistics"
        ]["minimum_determinant_lower"],
        "global_rh_certificate": False,
    }

