from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "outputs" / "lineage_semantic_audit.json"


def main() -> None:
    rows = [
        {
            "node": "v0.1",
            "object": "continuous axis-energy proxy",
            "valid_reading": "candidate-generation leakage proxy",
            "invalid_reading": "certified zero-side lower bound",
            "semantic_status": "correctly caveated",
        },
        {
            "node": "v0.2",
            "object": "U_j sup H plus tail",
            "valid_reading": "zero-position-free upper envelope",
            "invalid_reading": "actual zero sum",
            "semantic_status": "valid method-level majorant",
        },
        {
            "node": "v0.3",
            "object": "dual lower bound on the v0.2 envelope objective",
            "valid_reading": (
                "no-go certificate for making that conservative "
                "envelope smaller than one"
            ),
            "invalid_reading": (
                "positive lower bound for the actual critical-line "
                "zero contribution"
            ),
            "semantic_status": "finite dual algebra valid; transfer limited",
        },
        {
            "node": "v0.4-v0.6",
            "object": "atomic measure dual of the epigraph envelope",
            "valid_reading": "abstract primal/dual obstruction",
            "invalid_reading": (
                "arbitrary atomic measure dominated by unknown zeta "
                "zero locations"
            ),
            "semantic_status": "weak duality valid in the abstract model",
        },
        {
            "node": "v0.7",
            "object": "interval Green-kernel operator positivity",
            "valid_reading": (
                "Layer-A positivity and, conditionally, an upper-"
                "envelope method no-go theorem"
            ),
            "invalid_reading": "actual zero-side positive obstruction",
            "semantic_status": (
                "interval algebra valid; coefficient blocker refined "
                "rather than discarded"
            ),
        },
    ]
    tail = {
        "envelope_success_direction": (
            "To prove an upper leakage budget E_model >= actual tail, "
            "the model coefficient must be an upper coefficient."
        ),
        "method_nogo_direction": (
            "To prove E_true >= alpha by first proving E_small >= "
            "alpha, it is enough that the certified model coefficient "
            "is no larger than the theorem-backed envelope coefficient."
        ),
        "v0.7_lower_decimal_role": (
            "potentially correct for the method-no-go direction, "
            "pending a directed source theorem"
        ),
        "zeta_facing_tail_theorem_certified": False,
    }
    target_patch = {
        "real_height_interval": [20.395, 20.42],
        "status": "prototype geometry only",
        "external_fact": (
            "Platt and Trudgian rigorously verified RH for all "
            "nontrivial zeros through height 3e12."
        ),
        "source": {
            "arxiv": "2004.09765",
            "doi": "10.1112/blms.12460",
        },
        "actual_unresolved_zeta_target": False,
        "role_in_v0_8": (
            "calibration patch for coefficient semantics and "
            "functional-analytic convergence"
        ),
    }
    output = {
        "schema": "RH.Lineage.SemanticAudit.v0.8",
        "rows": rows,
        "tail_direction_audit": tail,
        "target_patch_relevance": target_patch,
        "main_revision": (
            "The upper coefficients are not intrinsically wrong. They "
            "are correct for a conservative supremum envelope and wrong "
            "only when retyped as lower mass for the actual zero sum."
        ),
        "abstract_v0_7_certificate_retained": True,
        "actual_zero_side_obstruction_proved": False,
        "upper_envelope_method_nogo_fully_certified": False,
        "global_rh_certificate": False,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
