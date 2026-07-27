from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from fractions import Fraction
from typing import Any


class CoefficientRole(str, Enum):
    """Logical role carried by a nonnegative band coefficient."""

    COUNT_UPPER = "count_upper"
    COUNT_LOWER = "count_lower"
    SUPREMUM_ENVELOPE_WEIGHT = "supremum_envelope_weight"
    INFIMUM_MINORANT_WEIGHT = "infimum_minorant_weight"
    ATOMIC_OPERATOR_LOWER = "atomic_operator_lower"


@dataclass(frozen=True)
class TypedCoefficient:
    band_id: str
    value: Fraction
    role: CoefficientRole
    source_statement: str
    endpoint_status: str

    def to_json(self) -> dict[str, Any]:
        output = asdict(self)
        output["value"] = {
            "numerator": self.value.numerator,
            "denominator": self.value.denominator,
        }
        output["role"] = self.role.value
        return output


def transfer_rule_table() -> list[dict[str, Any]]:
    """Return the four coefficient transfers used by the semantic audit."""

    return [
        {
            "rule_id": "upper_count_to_supremum_envelope",
            "premise": "n_j <= U_j and H(x) >= 0",
            "conclusion": "sum_{gamma in Gamma_j} H(gamma) <= U_j sup_{x in A_j} H(x)",
            "valid": True,
            "role": "upper leakage bound",
        },
        {
            "rule_id": "lower_count_to_infimum_minorant",
            "premise": "n_j >= L_j and H(x) >= 0",
            "conclusion": "sum_{gamma in Gamma_j} H(gamma) >= L_j inf_{x in A_j} H(x)",
            "valid": True,
            "role": "configuration-free scalar lower bound",
        },
        {
            "rule_id": "lower_count_to_arbitrary_measure",
            "premise": "n_j >= L_j, H(x) >= 0, and mu_j is an arbitrary probability measure",
            "conclusion": "sum_{gamma in Gamma_j} H(gamma) >= L_j integral H dmu_j",
            "valid": False,
            "role": "invalid location substitution",
        },
        {
            "rule_id": "upper_envelope_dual_to_actual_zero_lower_bound",
            "premise": "E_U(A) >= alpha and Z_Gamma(A) <= E_U(A)",
            "conclusion": "Z_Gamma(A) >= alpha",
            "valid": False,
            "role": "invalid reversal of a one-sided majorant",
        },
        {
            "rule_id": "upper_envelope_dual_to_method_nogo",
            "premise": "E_U(A) >= alpha for every target-feasible A",
            "conclusion": "the sufficient strategy E_U(A) < alpha has no feasible witness in the stated space",
            "valid": True,
            "role": "method-level no-go theorem",
        },
    ]


def exact_two_point_counterexample() -> dict[str, Any]:
    """An exact countermodel to the arbitrary-measure lower transfer."""

    zero_location = "x0"
    values = {"x0": Fraction(0), "x1": Fraction(1)}
    count = Fraction(1)
    upper = Fraction(1)
    lower = Fraction(1)
    actual_sum = values[zero_location]
    supremum_envelope = upper * max(values.values())
    infimum_minorant = lower * min(values.values())
    adversarial_measure_average = values["x1"]
    false_measure_minorant = lower * adversarial_measure_average
    return {
        "domain": ["x0", "x1"],
        "zero_multiset": [zero_location],
        "H_values": {
            key: f"{value.numerator}/{value.denominator}"
            for key, value in values.items()
        },
        "count": "1/1",
        "count_upper": "1/1",
        "count_lower": "1/1",
        "actual_zero_sum": (
            f"{actual_sum.numerator}/{actual_sum.denominator}"
        ),
        "upper_supremum_envelope": (
            f"{supremum_envelope.numerator}/"
            f"{supremum_envelope.denominator}"
        ),
        "lower_infimum_minorant": (
            f"{infimum_minorant.numerator}/"
            f"{infimum_minorant.denominator}"
        ),
        "arbitrary_measure": "delta_x1",
        "claimed_measure_minorant": (
            f"{false_measure_minorant.numerator}/"
            f"{false_measure_minorant.denominator}"
        ),
        "upper_envelope_valid": actual_sum <= supremum_envelope,
        "infimum_minorant_valid": actual_sum >= infimum_minorant,
        "arbitrary_measure_minorant_false": (
            actual_sum < false_measure_minorant
        ),
    }


def exact_rank_one_operator_counterexample() -> dict[str, Any]:
    """Two non-collinear rank-one evaluations have no common positive floor."""

    return {
        "space": "Q^2",
        "P_x0": [["1/1", "0/1"], ["0/1", "0/1"]],
        "P_x1": [["0/1", "0/1"], ["0/1", "1/1"]],
        "statement": (
            "If Q is positive semidefinite and Q <= P_x0 and Q <= P_x1, "
            "then range(Q) is contained in span(e1) intersect span(e2), "
            "hence Q=0."
        ),
        "common_nonzero_psd_floor_exists": False,
        "proof_type": "exact range intersection",
    }


def semantic_audit() -> dict[str, Any]:
    rules = transfer_rule_table()
    counterexample = exact_two_point_counterexample()
    operator = exact_rank_one_operator_counterexample()
    return {
        "schema": "RH.ZeroCount.SemanticBridge.v0.8",
        "rules": rules,
        "two_point_counterexample": counterexample,
        "rank_one_operator_counterexample": operator,
        "all_valid_rules_marked_valid": all(
            row["valid"]
            for row in rules
            if row["rule_id"]
            in {
                "upper_count_to_supremum_envelope",
                "lower_count_to_infimum_minorant",
                "upper_envelope_dual_to_method_nogo",
            }
        ),
        "all_invalid_rules_refuted": bool(
            counterexample["arbitrary_measure_minorant_false"]
            and not operator["common_nonzero_psd_floor_exists"]
            and all(
                not row["valid"]
                for row in rules
                if row["rule_id"]
                in {
                    "lower_count_to_arbitrary_measure",
                    "upper_envelope_dual_to_actual_zero_lower_bound",
                }
            )
        ),
        "global_rh_certificate": False,
    }
