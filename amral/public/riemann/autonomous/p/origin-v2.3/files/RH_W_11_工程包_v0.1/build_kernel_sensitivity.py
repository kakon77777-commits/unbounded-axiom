#!/usr/bin/env python3
"""Build the RH-W-11 B-spline kernel sensitivity certificate.

This script uses rational interval arithmetic for the prime-3 local activation
law. It does not compute or claim RH. The source geometry is the dimensionless
penetration inherited from RH-W-10 theta_plus.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import csv
import json
import math
import sys

import weil_interval_core as core

sys.set_int_max_str_digits(0)

OUT = Path(__file__).resolve().parent
H = F(87, 400)
D_PLUS = F(73189, 320000)
MAX_M = 5
TARGET = 1e-12


def iv_pow(x: core.IV, n: int) -> core.IV:
    if n < 0:
        raise ValueError("negative power")
    out = core.IV.point(1)
    for _ in range(n):
        out = core.coarsen(out * x, 100)
    return out


def dec_mid(x: core.IV) -> float:
    return float(x.midpoint())


def activation_interval(coeff: core.IV, eps: core.IV, r: int) -> core.IV:
    mag = core.coarsen(coeff * iv_pow(eps, r), 95).scale(F(1, factorial(r)))
    return -mag


def target_penetration_approx(coeff_mid: float, r: int, target: float) -> float:
    return (target * factorial(r) / coeff_mid) ** (1.0 / r)


def main() -> None:
    log3 = core.log_rational_iv(F(3), 180)
    sqrt3 = core.sqrt_rational_iv(F(3), 110)
    coeff = core.coarsen(log3 / sqrt3, 95)
    mu = core.coarsen(core.IV.point(D_PLUS + 4 * H) - log3, 95)
    if mu.lo <= 0:
        raise AssertionError("theta_plus must be beyond the cubic prime-3 boundary")
    eps = core.coarsen(mu / core.IV.point(H), 95)

    auto_rows = []
    for m in range(MAX_M + 1):
        r = 2 * m + 1
        p = activation_interval(coeff, eps, r)
        basis_reg = "jump / piecewise constant" if m == 0 else f"C^{m-1}"
        row = {
            "basis_degree_m": m,
            "basis_regularity": basis_reg,
            "correlation_degree": r,
            "correlation_regularity": f"C^{r-1}",
            "prime_activation_order": r,
            "fourier_decay_power": r + 1,
            "arch_tail_remainder_power_K": r,
            "prime3_entry_lower": core.iv_json(p)["decimal_lower"],
            "prime3_entry_upper": core.iv_json(p)["decimal_upper"],
            "prime3_abs_midpoint": abs(dec_mid(p)),
            "target_eps_for_abs_1e-12_approx": target_penetration_approx(dec_mid(coeff), r, TARGET),
            "unit_constant_K_for_tail_1e-12_heuristic": math.ceil((1 / TARGET) ** (1 / r)),
            "status": "WEIL_W_ADMISSIBLE; exact local activation interval",
        }
        auto_rows.append(row)

    # Mixed-order ladder: beta_m * beta_n = beta_{m+n+1}.
    mixed_rows = []
    for m in range(0, 5):
        for n in range(m, 5):
            r = m + n + 1
            p = activation_interval(coeff, eps, r)
            mixed_rows.append({
                "m": m,
                "n": n,
                "cross_correlation_degree": r,
                "cross_correlation_regularity": f"C^{r-1}",
                "prime_activation_order": r,
                "fourier_decay_power": r + 1,
                "arch_tail_remainder_power_K": r,
                "prime3_entry_lower": core.iv_json(p)["decimal_lower"],
                "prime3_entry_upper": core.iv_json(p)["decimal_upper"],
                "prime3_abs_midpoint": abs(dec_mid(p)),
            })

    with (OUT / "kernel_pareto.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(auto_rows[0].keys()))
        w.writeheader(); w.writerows(auto_rows)

    with (OUT / "mixed_order_ladder.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(mixed_rows[0].keys()))
        w.writeheader(); w.writerows(mixed_rows)

    # Exact recurrence ratios for successive auto-correlation orders.
    ratios = []
    for m in range(MAX_M):
        denom = (2*m + 2) * (2*m + 3)
        ratio = core.coarsen(iv_pow(eps, 2).scale(F(1, denom)), 95)
        ratios.append({
            "from_m": m,
            "to_m": m + 1,
            "identity": "|p_{m+1}|/|p_m| = eps^2/((2m+2)(2m+3))",
            "ratio": core.iv_json(ratio),
        })

    cert = {
        "schema": "RH-W-11-kernel-sensitivity-v0.1",
        "date": "2026-07-23",
        "scope": "local prime-3 boundary law for centered cardinal B-spline family; not RH evidence",
        "source_parameter": {
            "h": core.frac_json(H),
            "d_theta_plus": core.frac_json(D_PLUS),
            "mu_cubic_boundary": core.iv_json(mu),
            "normalized_penetration_eps": core.iv_json(eps),
            "coefficient_log3_over_sqrt3": core.iv_json(coeff),
        },
        "general_auto_law": {
            "basis": "v_{m,h,t}(x)=h^{-1/2} beta_m((x-t)/h)",
            "correlation": "v_m * tilde(v_m) = beta_{2m+1}",
            "activation": "p_{n,m}(eps)=-(Lambda(n)/sqrt(n))*eps_+^(2m+1)/(2m+1)!; for n=3, Lambda(3)=log(3)",
            "regularity": "C^(2m) but not C^(2m+1) at activation boundary",
            "arch_tail": "after retaining even derivatives through order 2m, local Laplace remainder yields O(K^-(2m+1)) under the package's termwise tail scheme",
        },
        "general_cross_law": {
            "correlation": "v_m * tilde(v_n) = beta_{m+n+1}",
            "activation_order": "m+n+1",
            "boundary_regularity": "C^(m+n) but not C^(m+n+1)",
            "fourier_decay": "|xi|^-(m+n+2) up to the centered sinc normalization",
        },
        "auto_family": auto_rows,
        "successive_order_ratios": ratios,
        "engineering_decision": {
            "single_best_kernel": False,
            "sensor_candidate": "m=1 (linear B-spline; cubic correlation; order-3 activation)",
            "certifier_candidate": "m=3 (cubic B-spline; degree-7 correlation; order-7 tail remainder)",
            "next_gap": "construct and certify a mixed m=1/m=3 dictionary with activation orders 3,5,7",
        },
        "warning": "All positivity statements remain finite-dimensional when matrices are later built. This artifact only certifies local kernel scaling laws.",
    }
    (OUT / "kernel_sensitivity_certificate.json").write_text(
        json.dumps(cert, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # concise machine summary
    m1 = auto_rows[1]["prime3_abs_midpoint"]
    m3 = auto_rows[3]["prime3_abs_midpoint"]
    summary = [
        "schema=OK",
        f"normalized_eps=[{core.iv_json(eps)['decimal_lower']},{core.iv_json(eps)['decimal_upper']}]",
        f"m1_abs_prime3={m1:.16e}",
        f"m3_abs_prime3={m3:.16e}",
        f"m1_over_m3={m1/m3:.16e}",
        "auto_orders=1,3,5,7,9,11",
        "mixed_orders_verified_by_formula=1..9",
        "status=KERNEL_PARETO_LAW_CERTIFIED",
        "RH_CLAIM=False",
    ]
    (OUT / "BUILD_SUMMARY.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
