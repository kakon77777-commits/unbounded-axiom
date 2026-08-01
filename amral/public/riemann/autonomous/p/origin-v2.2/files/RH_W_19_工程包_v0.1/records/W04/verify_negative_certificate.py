#!/usr/bin/env python3
"""Small exact verifier for RH-W-04 rational interval witness certificates.

It verifies only the interval arithmetic implication. It does not establish that
an externally supplied interval matrix encloses the true zeta Weil form.
"""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ALLOWED_RIGOR = {"EXACT_RATIONAL", "RIGOROUS_INTERVAL"}


def frac(x: Any) -> Fraction:
    if not isinstance(x, str):
        raise ValueError(f"rational values must be strings, got {type(x).__name__}")
    return Fraction(x)


def parse_matrix(raw: Any, n: int, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or len(raw) != n:
        raise ValueError(f"{name} must have {n} rows")
    out: list[list[Fraction]] = []
    for i, row in enumerate(raw):
        if not isinstance(row, list) or len(row) != n:
            raise ValueError(f"{name}[{i}] must have {n} columns")
        out.append([frac(v) for v in row])
    return out


def check_symmetric(A: list[list[Fraction]], name: str) -> None:
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                raise ValueError(f"{name} is not exactly symmetric at ({i},{j})")


def quadratic_interval(
    lower: list[list[Fraction]],
    upper: list[list[Fraction]],
    c: list[Fraction],
) -> tuple[Fraction, Fraction]:
    n = len(c)
    lo = Fraction(0)
    hi = Fraction(0)
    for i in range(n):
        for j in range(n):
            a = c[i] * c[j]
            if a >= 0:
                lo += a * lower[i][j]
                hi += a * upper[i][j]
            else:
                lo += a * upper[i][j]
                hi += a * lower[i][j]
    return lo, hi


def fmt(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator} ({float(q):.17g})"


def verify(path: Path) -> tuple[bool, dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("certificate_version") != "RH-W-04-v0.1":
        raise ValueError("unsupported certificate_version")
    if data.get("semantics") != "NEGATIVE_ONLY":
        raise ValueError("only NEGATIVE_ONLY semantics are accepted")
    n = data.get("dimension")
    if not isinstance(n, int) or n < 1:
        raise ValueError("dimension must be a positive integer")
    rigor = data.get("rigor_level")
    if rigor not in ALLOWED_RIGOR:
        return False, {
            "status": "REJECTED_NOT_RIGOROUS",
            "reason": f"rigor_level={rigor!r} is not a rigorous certificate level",
        }

    Mlo = parse_matrix(data.get("M_lower"), n, "M_lower")
    Mhi = parse_matrix(data.get("M_upper"), n, "M_upper")
    check_symmetric(Mlo, "M_lower")
    check_symmetric(Mhi, "M_upper")
    for i in range(n):
        for j in range(n):
            if Mlo[i][j] > Mhi[i][j]:
                raise ValueError(f"empty M interval at ({i},{j})")

    raw_c = data.get("witness")
    if not isinstance(raw_c, list) or len(raw_c) != n:
        raise ValueError(f"witness must have length {n}")
    c = [frac(v) for v in raw_c]
    if all(v == 0 for v in c):
        raise ValueError("witness must be nonzero")

    qlo, qhi = quadratic_interval(Mlo, Mhi, c)
    result: dict[str, Any] = {
        "status": "CERTIFIED_NEGATIVE" if qhi < 0 else "NOT_CERTIFIED",
        "q_lower": fmt(qlo),
        "q_upper": fmt(qhi),
        "negative_margin": fmt(-qhi),
    }

    if "G_lower" in data or "G_upper" in data:
        if "G_lower" not in data or "G_upper" not in data:
            raise ValueError("G_lower and G_upper must be supplied together")
        Glo = parse_matrix(data["G_lower"], n, "G_lower")
        Ghi = parse_matrix(data["G_upper"], n, "G_upper")
        check_symmetric(Glo, "G_lower")
        check_symmetric(Ghi, "G_upper")
        for i in range(n):
            for j in range(n):
                if Glo[i][j] > Ghi[i][j]:
                    raise ValueError(f"empty G interval at ({i},{j})")
        glo, ghi = quadratic_interval(Glo, Ghi, c)
        result["g_lower"] = fmt(glo)
        result["g_upper"] = fmt(ghi)
        result["denominator_certified_positive"] = glo > 0
        if qhi < 0 and glo > 0:
            # q/g <= q_upper/g_lower because q_upper < 0 and denominator >= g_lower > 0.
            result["rayleigh_upper"] = fmt(qhi / glo)

    # Metadata firewall for a future real-zeta certificate.
    if data.get("problem_id") == "RH_WEIL_ZETA":
        required = ["normalization_contract_sha256", "basis_manifest_sha256", "attachments"]
        missing = [key for key in required if not data.get(key)]
        if missing:
            return False, {
                **result,
                "status": "REJECTED_MISSING_ZETA_PROVENANCE",
                "missing": missing,
                "warning": "Arithmetic negativity was evaluated, but this is not accepted as a zeta-Weil certificate.",
            }

    return qhi < 0, result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path)
    args = ap.parse_args()
    try:
        ok, result = verify(args.certificate)
    except Exception as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, indent=2))
        return 2
    print(json.dumps(result, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
