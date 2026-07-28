#!/usr/bin/env python3
"""Independent high-precision floating cross-check; not part of the certificate."""
from __future__ import annotations
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80
H = mp.mpf(1) / 20
SHIFTS = (-mp.mpf(1) / 20, mp.mpf(1) / 20)


def beta(m: int, x: mp.mpf) -> mp.mpf:
    total = mp.mpf(0)
    for k in range(m + 2):
        y = x + mp.mpf(m + 1) / 2 - k
        if y > 0:
            total += (-1) ** k * comb(m + 1, k) * y ** m
    return total / mp.factorial(m)


def corr(i: int, j: int, x: mp.mpf) -> mp.mpf:
    center = SHIFTS[i] - SHIFTS[j]
    return beta(7, (x - center) / H)


def entry(i: int, j: int) -> mp.mpf:
    center = SHIFTS[i] - SHIFTS[j]
    left, right = center - 4 * H, center + 4 * H
    radius = max(abs(left), abs(right))
    f0 = corr(i, j, 0)
    endpoint = mp.quad(lambda x: corr(i, j, x) * (mp.exp(x / 2) + mp.exp(-x / 2)), [left, right])
    constant = -(mp.log(4 * mp.pi) + mp.euler) * f0

    points = {mp.mpf(0), radius}
    for k in range(-4, 5):
        for q in (center + H * k, -center - H * k):
            if 0 < q < radius:
                points.add(q)
    points = sorted(points)

    def local_integrand(x: mp.mpf) -> mp.mpf:
        if abs(x) < mp.mpf('1e-35'):
            # symmetric F has F'(0)=0; limit is f(0)/2
            return f0 / 2
        numerator = mp.exp(x / 2) * (corr(i, j, x) + corr(i, j, -x)) - 2 * f0
        return numerator / (mp.exp(x) - mp.exp(-x))

    local = mp.quad(local_integrand, points)
    tail = -f0 * mp.log(mp.tanh(radius / 2))
    arch = -local + tail
    return endpoint + constant + arch


def to_mpf(qobj: dict) -> mp.mpf:
    return mp.mpf(qobj['num']) / mp.mpf(qobj['den'])


def main() -> None:
    base = Path(__file__).resolve().parent
    cert = json.loads((base / 'weil_matrix_2x2_interval.json').read_text(encoding='utf-8'))
    lines = ['INDEPENDENT_FLOATING_CROSSCHECK_ONLY']
    for i, j, name in ((0, 0, 'M11'), (0, 1, 'M12'), (1, 1, 'M22')):
        value = entry(i, j)
        lo = to_mpf(cert['matrix'][name]['lower'])
        hi = to_mpf(cert['matrix'][name]['upper'])
        ok = lo <= value <= hi
        lines.append(f"{name}={mp.nstr(value, 50)}")
        lines.append(f"{name}_inside_interval={ok}")
        if not ok:
            raise SystemExit(f'{name} escaped certificate interval')
    lines.append('CROSSCHECK_OK')
    (base / 'CROSSCHECK.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
