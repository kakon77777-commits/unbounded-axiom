#!/usr/bin/env python3
"""Pure-rational verifier for the RH-W-09 15x15 certificate."""
from fractions import Fraction as F
from pathlib import Path
import json

GRID = 10**32


def frac(obj):
    return F(int(obj["num"]), int(obj["den"]))


def interval(obj):
    return frac(obj["lower"]), frac(obj["upper"])


def grid_center(lo, hi):
    midpoint = (lo + hi) / 2
    q = midpoint.numerator * GRID // midpoint.denominator
    left = F(q, GRID)
    right = F(q + 1, GRID)
    return left if abs(midpoint - left) <= abs(right - midpoint) else right


def ldlt(A):
    n = len(A)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        L[i][i] = F(1)
        pivot = A[i][i] - sum(L[i][k] * L[i][k] * pivots[k] for k in range(i))
        if pivot <= 0:
            return False, pivots + [pivot]
        pivots.append(pivot)
        for j in range(i + 1, n):
            L[j][i] = (
                A[j][i] - sum(L[j][k] * L[i][k] * pivots[k] for k in range(i))
            ) / pivot
    return True, pivots


def main():
    path = Path(__file__).with_name("theta_minus_15x15_interval.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["schema"] == "RH-W-09-continuation-certificate-v0.1"
    assert payload["status"] == "CERTIFIED_POSITIVE_GENERALIZED_MARGIN"
    assert payload["rigor_contract"]["floating_point_in_proof_path"] is False
    assert payload["basis"]["dimension"] == 15
    assert frac(payload["basis"]["h"]) == F(87, 400)
    assert frac(payload["basis"]["spacing"]) == F(117, 512)
    assert payload["support"]["exclusion_n"] == 59
    expected_pp = [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53]
    assert sorted(map(int, payload["prime_powers"].keys())) == expected_pp

    gap_lo, gap_hi = interval(payload["activation_boundary"]["positive_gap_log3_minus_boundary"])
    assert gap_lo > 0 and payload["activation_boundary"]["n3_at_negative_sample_is_inactive"] is True

    M = [[interval(x) for x in row] for row in payload["matrix"]]
    G = [[frac(x) for x in row] for row in payload["gram"]]
    n = len(M)
    assert n == 15 and all(len(row) == n for row in M)
    C = [[grid_center(*M[i][j]) for j in range(n)] for i in range(n)]
    row_radius = max(
        sum(max(abs(C[i][j] - M[i][j][0]), abs(M[i][j][1] - C[i][j])) for j in range(n))
        for i in range(n)
    )
    cert = payload["certificate"]
    assert int(cert["grid_denominator"]) == GRID
    assert row_radius == frac(cert["row_radius"])
    delta = frac(cert["delta"])
    assert delta == F(1, 10**9)
    A = [
        [C[i][j] - delta * G[i][j] - (row_radius if i == j else F(0)) for j in range(n)]
        for i in range(n)
    ]
    ok, pivots = ldlt(A)
    assert ok and all(x > 0 for x in pivots)
    assert pivots == [frac(x) for x in cert["pivots"]]

    print("schema=OK")
    print("dimension=15")
    print("prime_power_enumeration=OK")
    print("lag1_n3_boundary_gap_positive=OK")
    print(f"row_radius={row_radius}")
    print(f"generalized_margin_delta={delta}")
    print(f"ldlt_pivots_positive={len(pivots)}")
    print("status=CERTIFIED_POSITIVE_GENERALIZED_MARGIN")
    print("RH_CLAIM=False")


if __name__ == "__main__":
    main()
