#!/usr/bin/env python3
"""Small exact verifier for the emitted 2x2 interval certificate."""
from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path


def q(obj: dict) -> F:
    return F(int(obj['num']), int(obj['den']))


def iv(obj: dict) -> tuple[F, F]:
    lo, hi = q(obj['lower']), q(obj['upper'])
    if lo > hi:
        raise ValueError('reversed interval')
    return lo, hi


def add(a: tuple[F, F], b: tuple[F, F]) -> tuple[F, F]:
    return a[0] + b[0], a[1] + b[1]


def sub(a: tuple[F, F], b: tuple[F, F]) -> tuple[F, F]:
    return a[0] - b[1], a[1] - b[0]


def main() -> None:
    path = Path(__file__).resolve().parent / 'weil_matrix_2x2_interval.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    if data['scope_warning'] != 'Finite-dimensional positivity does not imply RH.':
        raise SystemExit('missing scope warning')
    if data['rigor_contract']['floating_point_in_proof_path'] is not False:
        raise SystemExit('floating point entered proof path')

    m11 = iv(data['matrix']['M11'])
    m12 = iv(data['matrix']['M12'])
    m22 = iv(data['matrix']['M22'])
    if m11 != m22:
        raise SystemExit('translation symmetry M11=M22 failed')

    even = add(m11, m12)
    odd = sub(m11, m12)
    if even[0] <= 0 or odd[0] <= 0:
        raise SystemExit('2D positivity not certified')

    g11 = q(data['gram_exact']['G11'])
    g12 = q(data['gram_exact']['G12'])
    det = q(data['gram_exact']['determinant'])
    if not (g11 > 0 and det == g11 * g11 - g12 * g12 and det > 0):
        raise SystemExit('Gram certificate failed')

    print('CERTIFICATE_OK')
    print(f'even_lower={even[0]}')
    print(f'odd_lower={odd[0]}')
    print('RH_CLAIM=False')

if __name__ == '__main__':
    main()
