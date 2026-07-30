from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from rh_w01_generator import (
    BumpParams,
    correlation_additive,
    correlation_multiplicative,
    log_generator,
    mellin_correlation,
    mellin_g,
    mellin_seed,
)

ROOT = Path(__file__).resolve().parent
TOL_STRICT = 5e-10
TOL_CORR_MELLIN = 1e-6


def assert_close(name: str, left: complex, right: complex, tol: float) -> float:
    err = abs(left - right)
    if not math.isfinite(err) or err > tol:
        raise AssertionError(f"{name}: error={err:.3e} > {tol:.3e}; {left=} {right=}")
    print(f"PASS {name}: error={err:.3e}")
    return err


def main() -> None:
    p = BumpParams()
    lo, hi = p.log_support

    # Exact identities are proven in the Markdown; numerical checks are regressions only.
    m0 = mellin_g(0j, p)
    m1 = mellin_g(1 + 0j, p)
    assert_close("vanishing Mellin moment s=0", m0, 0j, TOL_STRICT)
    assert_close("vanishing Mellin moment s=1", m1, 0j, TOL_STRICT)

    for s in (0.5 + 1j, 0.2 + 3j, 1.4 - 2.2j):
        left = mellin_g(s, p)
        right = s * (s - 1) * mellin_seed(s, p)
        assert_close(f"Mellin factorization s={s}", left, right, TOL_STRICT)

    for x in (math.exp(-1), 0.5, 1.0, 2.0, math.e):
        fm = correlation_multiplicative(x, p)
        fa = correlation_additive(x, p)
        assert_close(f"multiplicative/additive correlation x={x:.6g}", fm, fa, TOL_STRICT)

        hermitian = correlation_multiplicative(1.0 / x, p) / x
        assert_close(f"Hermitian symmetry x={x:.6g}", hermitian, np.conj(fm), TOL_STRICT)

    f1 = correlation_multiplicative(1.0, p)
    if abs(f1.imag) > TOL_STRICT or f1.real < -TOL_STRICT:
        raise AssertionError(f"f_g(1) must be real nonnegative, got {f1}")
    print(f"PASS f_g(1) real/nonnegative: {f1.real:.12g}")

    support_lo, support_hi = p.correlation_x_support
    outside = [support_lo * 0.9, support_hi * 1.1]
    for x in outside:
        value = correlation_additive(x, p)
        assert_close(f"support exclusion x={x:.6g}", value, 0j, 0.0)

    for t in (0.0, 1.0, 3.0):
        s = 0.5 + 1j * t
        left = mellin_correlation(s, p)
        mg = mellin_g(s, p)
        right = mg * np.conj(mellin_g(1 - np.conj(s), p))
        assert_close(f"Mellin correlation t={t:g}", left, right, TOL_CORR_MELLIN)

    with open(ROOT / "candidate_GBUMP_001.json", encoding="utf-8") as fh:
        candidate = json.load(fh)
    required = {
        "candidate_id",
        "family",
        "formula",
        "domain",
        "parameter_constraints",
        "regularity_proof",
        "vanishing_mellin_0",
        "vanishing_mellin_1",
        "correlation_exists",
        "correlation_in_W",
        "sign_convention",
        "unproved_items",
    }
    missing = sorted(required - set(candidate))
    if missing:
        raise AssertionError(f"candidate metadata missing: {missing}")
    print("PASS candidate metadata required fields")

    print("VALID RH-W-01 v0.2 GBUMP engineering package")


if __name__ == "__main__":
    main()
