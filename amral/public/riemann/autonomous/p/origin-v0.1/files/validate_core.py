"""Reproduce a few classical numerical checks used by RH_AI_研究起點_v0.1.

These checks are regression tests for the computational environment.
They are not evidence for the Riemann hypothesis.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 50


def theta(t: mp.mpf) -> mp.mpf:
    return mp.nsum(lambda n: mp.exp(-mp.pi * n * n * t), [-mp.inf, mp.inf])


def psi(t: mp.mpf) -> mp.mpf:
    return mp.nsum(lambda n: mp.exp(-mp.pi * n * n * t), [1, mp.inf])


def completed_zeta_mellin(s: mp.mpc) -> mp.mpc:
    integrand = lambda t: (
        t ** (s / 2 - 1) + t ** ((1 - s) / 2 - 1)
    ) * psi(t)
    return mp.quad(integrand, [1, mp.inf]) - 1 / s - 1 / (1 - s)


def log_gaussian_weight(n: int, lam: mp.mpf) -> mp.mpf:
    return mp.exp(-(lam / 4) * mp.log(n) ** 2)


def winding_number_zeta(samples_per_side: int = 200) -> mp.mpf:
    """Approximate the winding number of zeta around a rectangle.

    This is a floating-point regression check, not an interval-arithmetic
    certificate. The rectangle is [0,1] + i[1,30].
    """
    vertices = [
        mp.mpc(0, 1),
        mp.mpc(1, 1),
        mp.mpc(1, 30),
        mp.mpc(0, 30),
    ]
    points: list[mp.mpc] = []
    for i, a in enumerate(vertices):
        b = vertices[(i + 1) % 4]
        for j in range(samples_per_side):
            u = mp.mpf(j) / samples_per_side
            points.append(a + (b - a) * u)
    points.append(vertices[0])

    values = [mp.zeta(z) for z in points]
    total_phase = mp.mpf("0")
    for left, right in zip(values, values[1:]):
        delta = mp.arg(right) - mp.arg(left)
        while delta <= -mp.pi:
            delta += 2 * mp.pi
        while delta > mp.pi:
            delta -= 2 * mp.pi
        total_phase += delta
    return total_phase / (2 * mp.pi)


def main() -> None:
    print("[1] Jacobi theta transformation")
    for t in map(mp.mpf, ["0.3", "0.7", "1.5", "3.0"]):
        error = abs(theta(1 / t) - mp.sqrt(t) * theta(t))
        print(f"t={t}: error={mp.nstr(error, 8)}")

    print("\n[2] Mellin-theta representation")
    samples = [
        mp.mpc(2),
        mp.mpc(3),
        mp.mpc("4.5"),
        mp.mpc("0.5", "14.134725141734693790457251983562"),
    ]
    for s in samples:
        lhs = completed_zeta_mellin(s)
        rhs = mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
        print(f"s={s}: error={mp.nstr(abs(lhs-rhs), 8)}")

    print("\n[3] Log-Gaussian non-multiplicativity")
    lam = mp.mpf("0.01")
    g2 = log_gaussian_weight(2, lam)
    g3 = log_gaussian_weight(3, lam)
    g6 = log_gaussian_weight(6, lam)
    delta = abs(g6 - g2 * g3)
    ratio = g6 / (g2 * g3)
    closed = mp.exp(-(lam / 2) * mp.log(2) * mp.log(3))
    print(f"delta={mp.nstr(delta, 14)}")
    print(f"ratio error={mp.nstr(abs(ratio-closed), 8)}")

    print("\n[4] Argument-principle winding count")
    count = winding_number_zeta(samples_per_side=200)
    print(f"count={mp.nstr(count, 20)}")


if __name__ == "__main__":
    main()
