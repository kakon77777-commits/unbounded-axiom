#!/usr/bin/env python3
"""Build a prime-active rational interval enclosure for a 2x2 true-zeta Weil matrix.

The verification layer uses only Python integers and fractions.Fraction.
Transcendental constants are enclosed by rational series with explicit tails.
No floating-point number participates in the proof path.

This is a finite-dimensional positivity computation, not a proof of RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from decimal import Decimal, Context, localcontext
from math import comb, factorial, isqrt
import hashlib
import sys
sys.set_int_max_str_digits(0)
import json
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class IV:
    lo: F
    hi: F

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("invalid interval")

    @staticmethod
    def point(x: F | int) -> "IV":
        y = x if isinstance(x, F) else F(x)
        return IV(y, y)

    def __add__(self, other: "IV") -> "IV":
        return IV(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "IV":
        return IV(-self.hi, -self.lo)

    def __sub__(self, other: "IV") -> "IV":
        return self + (-other)

    def __mul__(self, other: "IV") -> "IV":
        vals = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return IV(min(vals), max(vals))

    def reciprocal(self) -> "IV":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return IV(F(1, 1) / self.hi, F(1, 1) / self.lo) if self.lo > 0 else IV(F(1, 1) / self.hi, F(1, 1) / self.lo)

    def __truediv__(self, other: "IV") -> "IV":
        return self * other.reciprocal()

    def scale(self, q: F) -> "IV":
        return self * IV.point(q)

    def width(self) -> F:
        return self.hi - self.lo

    def midpoint(self) -> F:
        return (self.lo + self.hi) / 2

    def decimal(self, digits: int = 18) -> Tuple[str, str]:
        def d(q: F) -> str:
            # display only; not used by verifier
            return f"{float(q):.{digits}g}"
        return d(self.lo), d(self.hi)



def coarsen(x: IV, digits: int = 50) -> IV:
    """Outward-round an interval to a fixed decimal rational grid."""
    D = 10 ** digits
    lo_num = x.lo.numerator * D // x.lo.denominator
    # Python // is floor, including for negative values.
    hi_num = -((-x.hi.numerator * D) // x.hi.denominator)
    return IV(F(lo_num, D), F(hi_num, D))

def iv_sum(items: Iterable[IV]) -> IV:
    out = IV.point(0)
    for item in items:
        out = out + item
    return out


# ---------- rigorous elementary functions ----------

def _decimal_to_fraction(d: Decimal) -> F:
    sign, digits, exponent = d.as_tuple()
    coeff = 0
    for digit in digits:
        coeff = coeff * 10 + digit
    if sign:
        coeff = -coeff
    return F(coeff * (10 ** exponent), 1) if exponent >= 0 else F(coeff, 10 ** (-exponent))


def exp_iv(x: F, precision: int = 90) -> IV:
    """Enclose exp(x) using CPython Decimal's correctly rounded exp.

    All arguments produced by this package have terminating decimal expansions
    (denominators divide a power of 10), so the Decimal input is exact.  The
    correctly rounded result is expanded to its adjacent representable values.
    """
    ctx = Context(prec=precision)
    with localcontext(ctx):
        dx = Decimal(x.numerator) / Decimal(x.denominator)
        # Guard the contract: input conversion must be exact at this precision.
        if _decimal_to_fraction(dx) != x:
            raise ArithmeticError("non-terminating or inexact Decimal input")
        y = dx.exp(context=ctx)
        lo = ctx.next_minus(y)
        hi = ctx.next_plus(y)
    return coarsen(IV(_decimal_to_fraction(lo), _decimal_to_fraction(hi)), 70)


def log_rational_iv(x: F, terms: int = 80) -> IV:
    """Rational enclosure of log(x), x rational positive, via atanh series."""
    if x <= 0:
        raise ValueError("log domain")
    k = 0
    m = x
    while m >= 2:
        m /= 2
        k += 1
    while m < 1:
        m *= 2
        k -= 1

    def log_unit(y: F) -> IV:
        z = (y - 1) / (y + 1)
        z2 = z * z
        power = z
        s = F(0)
        for n in range(terms + 1):
            s += power / (2 * n + 1)
            power *= z2
        lower = 2 * s
        next_power = power
        tail = 2 * next_power / ((2 * terms + 3) * (1 - z2))
        return IV(lower, lower + tail)

    log2 = log_unit(F(2))
    logm = log_unit(m)
    return coarsen(logm + log2.scale(F(k)), 60)


def atan_unit_iv(q: F, terms: int = 80) -> IV:
    """Alternating-series enclosure for arctan(q), 0<=q<=1."""
    if not (0 <= q <= 1):
        raise ValueError("atan_unit range")
    s = F(0)
    power = q
    for n in range(terms + 1):
        term = power / (2 * n + 1)
        s += term if n % 2 == 0 else -term
        power *= q * q
    next_term = power / (2 * terms + 3)
    if (terms + 1) % 2 == 0:
        # next sign positive
        return IV(s, s + next_term)
    return IV(s - next_term, s)


def pi_iv() -> IV:
    # Machin: pi/4 = 4 atan(1/5) - atan(1/239)
    return (atan_unit_iv(F(1, 5), 70).scale(F(16))
            - atan_unit_iv(F(1, 239), 24).scale(F(4)))


def log4pi_iv() -> IV:
    p = pi_iv().scale(F(4))
    return IV(log_rational_iv(p.lo, 100).lo, log_rational_iv(p.hi, 100).hi)


def euler_gamma_iv(n: int = 100) -> IV:
    """Uses 1/(2n+1) < H_n-log(n)-gamma < 1/(2n)."""
    H = sum((F(1, k) for k in range(1, n + 1)), F(0))
    ln = log_rational_iv(F(n), 100)
    lo = H - ln.hi - F(1, 2 * n)
    hi = H - ln.lo - F(1, 2 * n + 1)
    return IV(lo, hi)


# ---------- rational polynomials ----------
# coefficients are low degree first

def poly_add(a: Sequence[F], b: Sequence[F]) -> List[F]:
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a: Sequence[F], q: F) -> List[F]:
    return [q * c for c in a]


def linear_power(alpha: F, beta: F, degree: int) -> List[F]:
    # (alpha*x + beta)^degree
    return [F(comb(degree, j)) * alpha**j * beta**(degree - j) for j in range(degree + 1)]


def poly_eval(p: Sequence[F], x: F) -> F:
    s = F(0)
    for c in reversed(p):
        s = s * x + c
    return s


def poly_derivative(p: Sequence[F], order: int = 1) -> List[F]:
    out = list(p)
    for _ in range(order):
        out = [F(i) * out[i] for i in range(1, len(out))] or [F(0)]
    return out


def integrate_poly_exp_iv(p: Sequence[F], lam: F, left: F, right: F) -> IV:
    """Exact polynomial-exponential antiderivative with rigorous exp enclosures."""
    if left == right:
        return IV.point(0)
    if lam == 0:
        total = F(0)
        for i, c in enumerate(p):
            total += c * (right ** (i + 1) - left ** (i + 1)) / (i + 1)
        return IV.point(total)

    deg = len(p) - 1
    r = [F(0)] * (deg + 1)
    r[deg] = p[deg] / lam
    for k in range(deg - 1, -1, -1):
        r[k] = (p[k] - F(k + 1) * r[k + 1]) / lam
    Ru = poly_eval(r, right)
    Rl = poly_eval(r, left)
    return coarsen(exp_iv(lam * right).scale(Ru) - exp_iv(lam * left).scale(Rl), 55)


def sqrt_rational_iv(x: F, digits: int = 80) -> IV:
    """Exact rational enclosure of sqrt(x) using integer square roots."""
    if x < 0:
        raise ValueError("sqrt domain")
    D = 10 ** digits
    A = x.numerator * D * D
    q = x.denominator
    n = isqrt(A // q)
    while (n + 1) * (n + 1) * q <= A:
        n += 1
    while n * n * q > A:
        n -= 1
    if n * n * q == A:
        return IV.point(F(n, D))
    return IV(F(n, D), F(n + 1, D))


def poly_eval_iv(p: Sequence[F], x: IV) -> IV:
    out = IV.point(0)
    for c in reversed(p):
        out = out * x + IV.point(c)
    return out

# ---------- centered cardinal B-spline beta_7 ----------
DEGREE = 7
H = F(1, 10)
SHIFTS = (F(-1, 4), F(1, 4))


def beta7_affine_piece(center: F, sign: int, midpoint: F) -> List[F]:
    """Polynomial for beta7((sign*x-center)/H) on interval containing midpoint."""
    zmid = (sign * midpoint - center) / H
    out = [F(0)] * (DEGREE + 1)
    for k in range(DEGREE + 2):
        shift = F(4 - k)
        if zmid + shift > 0:
            # ((sign*x-center)/H + shift)^7
            alpha = F(sign) / H
            beta = -center / H + shift
            term = linear_power(alpha, beta, DEGREE)
            coeff = F((-1) ** k * comb(DEGREE + 1, k), factorial(DEGREE))
            out = poly_add(out, poly_scale(term, coeff))
    return out


def f_piece(center: F, midpoint: F, sign: int = 1) -> List[F]:
    return beta7_affine_piece(center, sign, midpoint)


def support(center: F) -> Tuple[F, F]:
    return center - 4 * H, center + 4 * H


def knots_for_f(center: F) -> List[F]:
    return [center + H * k for k in range(-4, 5)]


def integrate_f_exp(center: F, lam: F) -> IV:
    ks = knots_for_f(center)
    total = IV.point(0)
    for left, right in zip(ks[:-1], ks[1:]):
        mid = (left + right) / 2
        p = f_piece(center, mid, 1)
        total = total + integrate_poly_exp_iv(p, lam, left, right)
    return total


def f_value(center: F, x: F) -> F:
    left, right = support(center)
    if x < left or x > right:
        return F(0)
    # At knots the truncated-power definition is unambiguous.
    out = F(0)
    z = (x - center) / H
    for k in range(DEGREE + 2):
        y = z + F(4 - k)
        if y > 0:
            out += F((-1) ** k * comb(DEGREE + 1, k), factorial(DEGREE)) * y**DEGREE
    return out


def f_interval(center: F, x: IV) -> IV:
    """Rigorous interval evaluation of one beta_7 correlation sample.

    The supplied interval must lie within one polynomial knot interval.  This
    is checked, not assumed.
    """
    left, right = support(center)
    if x.hi < left or x.lo > right:
        return IV.point(0)
    if x.lo < left or x.hi > right:
        raise ArithmeticError("sample interval crosses support boundary")
    knots = knots_for_f(center)
    containing = [(a, b) for a, b in zip(knots[:-1], knots[1:]) if a <= x.lo and x.hi <= b]
    if len(containing) != 1:
        raise ArithmeticError("sample interval crosses a spline knot")
    a, b = containing[0]
    mid = (a + b) / 2
    p = f_piece(center, mid, 1)
    return coarsen(poly_eval_iv(p, x), 60)


def even_sum_pieces(center: F) -> Tuple[F, List[Tuple[F, F, List[F]]]]:
    left, right = support(center)
    radius = max(abs(left), abs(right))
    knots = {F(0), radius}
    for q in knots_for_f(center):
        if 0 < q < radius:
            knots.add(q)
        if 0 < -q < radius:
            knots.add(-q)
    ordered = sorted(knots)
    pieces = []
    for a, b in zip(ordered[:-1], ordered[1:]):
        mid = (a + b) / 2
        p_pos = f_piece(center, mid, 1) if support(center)[0] < mid < support(center)[1] else [F(0)]
        # f(-x) = beta7((-x-center)/H)
        neg_mid = -mid
        p_neg = f_piece(center, mid, -1) if support(center)[0] < neg_mid < support(center)[1] else [F(0)]
        pieces.append((a, b, poly_add(p_pos, p_neg)))
    return radius, pieces


def laplace_even_sum(center: F, a: F, pieces: Sequence[Tuple[F, F, Sequence[F]]]) -> IV:
    return iv_sum(integrate_poly_exp_iv(p, -a, left, right) for left, right, p in pieces)


def derivative_data(center: F, pieces: Sequence[Tuple[F, F, Sequence[F]]]) -> Tuple[F, F, F, F]:
    first = pieces[0][2]
    f0 = poly_eval(first, F(0))
    f2 = poly_eval(poly_derivative(first, 2), F(0))
    f4 = poly_eval(poly_derivative(first, 4), F(0))
    b6 = F(0)
    for left, right, p in pieces:
        d6 = poly_derivative(p, 6)
        b6 = max(b6, abs(poly_eval(d6, left)), abs(poly_eval(d6, right)))
    return f0, f2, f4, b6


def pseries_upper(K: int, p: int) -> F:
    # sum_{k=K}^inf k^-p <= K^-p + integral_K^inf x^-p dx
    return F(1, K**p) + F(1, (p - 1) * K ** (p - 1))


def arch_series_iv(center: F, K: int = 100) -> Tuple[IV, dict]:
    """Enclose the archimedean term with an exact leading-tail summation.

    For a_k=2k+1/2 and b_k=2k+1,
      I(a_k)-F(0)/b_k
      = F0(1/a_k-1/b_k)+F2/a_k^3+F4/a_k^5+R6.
    The full leading series has the closed value
      sum_{k>=0}(1/a_k-1/b_k)=pi/4+log(2)/2,
    so its tail is enclosed by subtracting the exact rational partial sum.
    This removes the O(1/K) width that dominated the earlier certificate.
    """
    radius, pieces = even_sum_pieces(center)
    f_at_zero = f_value(center, F(0))
    F0, F2, F4, B6 = derivative_data(center, pieces)
    assert F0 == 2 * f_at_zero

    partial = IV.point(0)
    s0_partial = F(0)
    for k in range(K):
        aa = F(4 * k + 1, 2)  # 2k+1/2
        bb = F(2 * k + 1)
        I = laplace_even_sum(center, aa, pieces)
        term = I - IV.point(F0 / bb)
        partial = coarsen(partial + term, 50)
        s0_partial += F(1, aa) - F(1, bb)

    # Exact enclosure of the leading tail.
    s0_total = pi_iv().scale(F(1,4)) + log_rational_iv(F(2), 120).scale(F(1,2))
    s0_tail = s0_total - IV.point(s0_partial)
    tail_leading = s0_tail.scale(F0)

    # Higher derivative tails; a_k >= 2k for k>=K.
    b3 = pseries_upper(K, 3) * F(1,8)
    b5 = pseries_upper(K, 5) * F(1,32)
    b7 = pseries_upper(K, 7) * F(1,128)
    tail_higher = IV(-abs(F2)*b3, abs(F2)*b3) + IV(-abs(F4)*b5, abs(F4)*b5) + IV(-B6*b7, B6*b7)
    tail_iv = tail_leading + tail_higher

    series_total = partial + tail_iv
    arch = coarsen(-series_total, 45)
    audit = {
        "radius": frac_json(radius),
        "series_terms": K,
        "F0": frac_json(F0),
        "F2": frac_json(F2),
        "F4": frac_json(F4),
        "B6_sup": frac_json(B6),
        "leading_tail_closed_form": "pi/4 + log(2)/2 minus rational partial",
        "leading_tail": iv_json(tail_leading),
        "higher_tail_abs_bound": frac_json(abs(F2)*b3 + abs(F4)*b5 + B6*b7),
        "tail_interval": iv_json(tail_iv),
        "partial": iv_json(partial),
        "arch": iv_json(arch),
    }
    return arch, audit


def frac_json(q: F) -> dict:
    return {"num": str(q.numerator), "den": str(q.denominator)}


def iv_json(x: IV) -> dict:
    lo, hi = x.decimal(20)
    return {
        "lower": frac_json(x.lo),
        "upper": frac_json(x.hi),
        "decimal_lower": lo,
        "decimal_upper": hi,
    }


def matrix_entry(i: int, j: int, K: int = 200) -> Tuple[IV, dict]:
    center = SHIFTS[i] - SHIFTS[j]
    f0 = f_value(center, F(0))
    endpoint_integral = coarsen(integrate_f_exp(center, F(1, 2)) + integrate_f_exp(center, F(-1, 2)), 45)
    constant = coarsen(-(log4pi_iv() + euler_gamma_iv(100)).scale(f0), 45)
    arch, arch_audit = arch_series_iv(center, K)

    left, right = support(center)
    radius = max(abs(left), abs(right))
    log2 = log_rational_iv(F(2), 120)
    log3 = log_rational_iv(F(3), 120)
    if not log3.lo > radius:
        raise AssertionError("n>=3 prime-power exclusion not certified")

    sqrt2 = sqrt_rational_iv(F(2), 90)
    coeff2 = log2 / sqrt2
    if radius < log2.lo:
        f_plus = IV.point(0)
        f_minus = IV.point(0)
        prime = IV.point(0)
        active2 = False
    else:
        f_plus = f_interval(center, log2)
        f_minus = f_interval(center, -log2)
        prime = coarsen(-(coeff2 * (f_plus + f_minus)), 50)
        active2 = not (f_plus.lo == f_plus.hi == 0 and f_minus.lo == f_minus.hi == 0)

    prime_free_total = coarsen(endpoint_integral + constant + arch, 40)
    total = coarsen(prime_free_total + prime, 40)
    audit = {
        "basis_indices": [i, j],
        "correlation_center": frac_json(center),
        "support": [frac_json(left), frac_json(right)],
        "f_at_zero": frac_json(f0),
        "endpoint_integral": iv_json(endpoint_integral),
        "constant_term": iv_json(constant),
        "archimedean_term": iv_json(arch),
        "prime_free_total": iv_json(prime_free_total),
        "prime_term": iv_json(prime),
        "prime_audit": {
            "max_abs_support": frac_json(radius),
            "log2": iv_json(log2),
            "log3": iv_json(log3),
            "sqrt2": iv_json(sqrt2),
            "coefficient_log2_over_sqrt2": iv_json(coeff2),
            "f_at_plus_log2": iv_json(f_plus),
            "f_at_minus_log2": iv_json(f_minus),
            "n2_active": active2,
            "n_ge_3_excluded": True,
            "reason": "support lies strictly inside (-log 3, log 3); therefore only n=2 can contribute, and it is evaluated by interval polynomial arithmetic",
        },
        "arch_audit": arch_audit,
        "total": iv_json(total),
    }
    return total, audit


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> None:
    outdir = Path(__file__).resolve().parent
    entries = {}
    audits = []
    for i, j in ((0, 0), (0, 1), (1, 1)):
        val, audit = matrix_entry(i, j, 200)
        entries[f"M{i+1}{j+1}"] = iv_json(val)
        audits.append(audit)

    # exact translation symmetry M11=M22
    m11 = IV(
        F(int(entries["M11"]["lower"]["num"]), int(entries["M11"]["lower"]["den"])),
        F(int(entries["M11"]["upper"]["num"]), int(entries["M11"]["upper"]["den"])),
    )
    m12 = IV(
        F(int(entries["M12"]["lower"]["num"]), int(entries["M12"]["lower"]["den"])),
        F(int(entries["M12"]["upper"]["num"]), int(entries["M12"]["upper"]["den"])),
    )
    m22 = IV(
        F(int(entries["M22"]["lower"]["num"]), int(entries["M22"]["lower"]["den"])),
        F(int(entries["M22"]["upper"]["num"]), int(entries["M22"]["upper"]["den"])),
    )
    if m11.lo != m22.lo or m11.hi != m22.hi:
        raise AssertionError("translation symmetry mismatch")

    even = m11 + m12
    odd = m11 - m12
    positive_2d = even.lo > 0 and odd.lo > 0

    def parse_iv(obj: dict) -> IV:
        return IV(F(int(obj["lower"]["num"]), int(obj["lower"]["den"])),
                  F(int(obj["upper"]["num"]), int(obj["upper"]["den"])))
    m12_prime = parse_iv(audits[1]["prime_term"])
    m12_prime_free = parse_iv(audits[1]["prime_free_total"])
    even_prime_free = m11 + m12_prime_free
    odd_prime_free = m11 - m12_prime_free

    G11 = f_value(F(0), F(0))
    G12 = f_value(SHIFTS[0] - SHIFTS[1], F(0))
    gram_det = G11 * G11 - G12 * G12

    result = {
        "schema": "RH-W-06-real-weil-matrix-v0.1",
        "date": "2026-07-23",
        "status": "CERTIFIED_POSITIVE_ON_THIS_2D_SUBSPACE" if positive_2d else "INCONCLUSIVE",
        "scope_warning": "Finite-dimensional positivity does not imply RH.",
        "basis": {
            "definition": "v_i(x)=h^(-1/2) beta_3((x-t_i)/h); common factor cancels in correlations as encoded",
            "h": frac_json(H),
            "shifts": [frac_json(x) for x in SHIFTS],
            "individual_support_radius": frac_json(2 * H),
            "ambient_a": frac_json(F(9, 20)),
            "correlation_formula": "f_ij(x)=beta_7((x-(t_i-t_j))/h)",
        },
        "normalization": {
            "source_formula": "Suzuki 2026 Eq. at Introduction / Bombieri-Clay explicit formula in additive coordinates",
            "prime_terms": "only n=2 can contribute; n>=3 excluded by support<log(3)",
            "series_terms": 200,
        },
        "matrix": entries,
        "symmetry_modes": {
            "even_vector_[1,1]": iv_json(even),
            "odd_vector_[1,-1]": iv_json(odd),
        },
        "prime2_coupling_effect": {
            "M12_prime_free": iv_json(m12_prime_free),
            "M12_prime_term": iv_json(m12_prime),
            "M12_with_prime2": iv_json(m12),
            "even_mode_without_prime2": iv_json(even_prime_free),
            "even_mode_with_prime2": iv_json(even),
            "odd_mode_without_prime2": iv_json(odd_prime_free),
            "odd_mode_with_prime2": iv_json(odd),
            "interpretation": "the n=2 term is an off-diagonal negative coupling; it lowers the even mode and raises the odd mode",
        },
        "gram_exact": {
            "G11": frac_json(G11),
            "G12": frac_json(G12),
            "G22": frac_json(G11),
            "determinant": frac_json(gram_det),
            "positive_definite": G11 > 0 and gram_det > 0,
        },
        "component_audits": audits,
        "rigor_contract": {
            "floating_point_in_proof_path": False,
            "transcendentals": "rational atanh/arctan series, integer-square-root enclosure, and documented Decimal.exp outward enclosure",
            "arch_tail": "six integrations by parts plus rational p-series majorant",
            "prime_completeness": "support<log(3) and explicit n=2 interval evaluation",
            "remaining_gap": "The basis is only 2D and activates only n=2; higher-prime and higher-dimensional matrices remain open engineering.",
        },
    }

    matrix_path = outdir / "weil_matrix_prime2_2x2_interval.json"
    matrix_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "RH-W-06 rational interval build",
        f"status={result['status']}",
        f"M11={m11.decimal(16)}",
        f"M12={m12.decimal(16)}",
        f"M22={m22.decimal(16)}",
        f"even_mode={even.decimal(16)}",
        f"odd_mode={odd.decimal(16)}",
        f"gram_det={float(gram_det):.16g} (display only)",
        "FLOATING_POINT_IN_PROOF_PATH=False",
        "RH_CLAIM=False",
    ]
    (outdir / "VALIDATION.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
