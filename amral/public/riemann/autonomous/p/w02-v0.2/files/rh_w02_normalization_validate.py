"""Fast numerical regression for RH-W-02 normalization.

Checks compact-core moment cancellation, the equality between the Clay
correlation integral and multiplicative convolution with Hermitian involution,
Mellin factorization, and a finite-zero covariance identity. It does not
compute the full arithmetic explicit formula and does not prove RH.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import mpmath as mp

mp.mp.dps = 30
A = 1.3
C = 0.17


def compact_generator(u: np.ndarray) -> np.ndarray:
    q = u / A
    b = np.zeros_like(u)
    bu = np.zeros_like(u)
    buu = np.zeros_like(u)
    mask = np.abs(q) < 1.0
    qm = q[mask]
    den = 1.0 - qm * qm
    bm = np.exp(-1.0 / den)
    fq = -2.0 * qm / den**2
    fqq = -2.0 / den**2 - 8.0 * qm * qm / den**3
    b[mask] = bm
    bu[mask] = bm * fq / A
    buu[mask] = bm * (fqq + fq * fq) / (A * A)

    p = 1.0 + C * np.cos(2.0 * u)
    pu = -2.0 * C * np.sin(2.0 * u)
    puu = -4.0 * C * np.cos(2.0 * u)
    hp = bu * p + b * pu
    hpp = buu * p + 2.0 * bu * pu + b * puu
    return hpp + hp


def mellin_from_grid(u: np.ndarray, G: np.ndarray, s: complex) -> complex:
    return np.trapezoid(G * np.exp(complex(s) * u), u)


def interp_G(z: np.ndarray, u: np.ndarray, G: np.ndarray) -> np.ndarray:
    return np.interp(z, u, G, left=0.0, right=0.0)


def correlation_direct(v: float, u: np.ndarray, G: np.ndarray) -> complex:
    # C_g(e^v)=int G(u+v) conjugate(G(u)) e^u du.
    return np.trapezoid(interp_G(u + v, u, G) * np.conj(G) * np.exp(u), u)


def correlation_convolution(v: float, u: np.ndarray, G: np.ndarray) -> complex:
    # (g*g*)(e^v)=int G(u) e^{u-v} conjugate(G(u-v)) du.
    return np.trapezoid(G * np.exp(u-v) * np.conj(interp_G(u-v, u, G)), u)


def main() -> None:
    u = np.linspace(-A, A, 12001)
    G = compact_generator(u)

    g0 = mellin_from_grid(u, G, 0)
    g1 = mellin_from_grid(u, G, 1)

    test_v = np.array([-1.7, -0.9, 0.0, 0.85, 1.75])
    corr_errors = [
        abs(correlation_direct(float(v), u, G) - correlation_convolution(float(v), u, G))
        for v in test_v
    ]

    vgrid = np.linspace(-2*A, 2*A, 1601)
    Cv = np.array([correlation_direct(float(v), u, G) for v in vgrid])
    test_s = [0.37+1.2j, 0.5+4.0j, 0.82-0.7j]
    factor_errors = []
    for s in test_s:
        lhs = np.trapezoid(Cv * np.exp(s*vgrid), vgrid)
        rhs = mellin_from_grid(u, G, s) * np.conj(mellin_from_grid(u, G, 1-np.conj(s)))
        factor_errors.append(abs(lhs-rhs))

    finite_w = 0j
    finite_sq = 0.0
    for n in range(1, 9):
        rho = complex(mp.zetazero(n))
        val = mellin_from_grid(u, G, rho)
        reflected = mellin_from_grid(u, G, 1-np.conj(rho))
        finite_w += val * np.conj(reflected)
        finite_sq += abs(val)**2
    zero_sum_error = abs(finite_w-finite_sq)

    checks = {
        'mellin_g_0_abs': abs(g0),
        'mellin_g_1_abs': abs(g1),
        'max_correlation_identity_error': max(corr_errors),
        'max_mellin_factorization_error': max(factor_errors),
        'finite_zero_covariance_error': zero_sum_error,
        'finite_zero_sum_real': finite_w.real,
    }

    assert checks['mellin_g_0_abs'] < 2e-10, checks
    assert checks['mellin_g_1_abs'] < 2e-10, checks
    assert checks['max_correlation_identity_error'] < 2e-8, checks
    assert checks['max_mellin_factorization_error'] < 4e-6, checks
    assert checks['finite_zero_covariance_error'] < 1e-13, checks
    assert checks['finite_zero_sum_real'] >= 0, checks

    lines = [
        'RH-W-02 normalization regression',
        *(f'{k}={v:.12e}' for k,v in checks.items()),
        'SCOPE=algebraic_and_finite_zero_regression_only',
        'ALL_CHECKS_OK',
    ]
    text = '\n'.join(lines) + '\n'
    print(text, end='')
    Path(__file__).with_name('VALIDATION_v0.2.txt').write_text(text, encoding='utf-8')


if __name__ == '__main__':
    main()
