"""二、三、四阶 L,U 角色符号迭代。"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import csv


@dataclass(frozen=True)
class Bounds:
    lower: Fraction
    upper: Fraction

    @property
    def width(self) -> Fraction:
        return self.upper - self.lower

    def assert_invariant(self, n: int) -> None:
        assert self.lower > 0
        assert self.upper > 0
        assert self.lower * self.upper == n


def initial(n: int) -> Bounds:
    if n <= 0:
        raise ValueError("n 必须为正整数")
    return Bounds(Fraction(2 * n, n + 1), Fraction(n + 1, 2))


def order2(x: Bounds) -> Bounds:
    l, u = x.lower, x.upper
    s = l + u
    return Bounds(2 * l * u / s, s / 2)


def order3(x: Bounds) -> Bounds:
    l, u = x.lower, x.upper
    return Bounds(
        l * (l + 3 * u) / (3 * l + u),
        u * (3 * l + u) / (l + 3 * u),
    )


def order4(x: Bounds) -> Bounds:
    l, u = x.lower, x.upper
    q = l * l + 6 * l * u + u * u
    s = l + u
    return Bounds(
        4 * l * u * s / q,
        q / (4 * s),
    )


def rho(x: Bounds, n: int, precision: int = 100) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision
        root = Decimal(n).sqrt()
        l = Decimal(x.lower.numerator) / Decimal(x.lower.denominator)
        return (root - l) / (root + l)


def generate_rows(ns=(2, 3, 10), rounds=5):
    methods = {2: order2, 3: order3, 4: order4}
    rows = []
    for n in ns:
        for order, update in methods.items():
            state = initial(n)
            for k in range(rounds):
                state.assert_invariant(n)
                current_rho = rho(state, n)
                rows.append(
                    {
                        "n": n,
                        "order": order,
                        "round": k,
                        "lower": str(state.lower),
                        "upper": str(state.upper),
                        "width": str(state.width),
                        "lower_float": f"{float(state.lower):.17g}",
                        "upper_float": f"{float(state.upper):.17g}",
                        "width_float": f"{float(state.width):.17g}",
                        "rho": str(current_rho),
                    }
                )
                next_state = update(state)
                next_state.assert_invariant(n)
                next_rho = rho(next_state, n)
                with localcontext() as ctx:
                    ctx.prec = 80
                    assert abs(next_rho - current_rho**order) < Decimal("1e-70")
                state = next_state

    for n in ns + (97,):
        start = initial(n)
        assert order4(start) == order2(order2(start))
    return rows


def main() -> None:
    rows = generate_rows()
    out_dir = Path(__file__).resolve().parents[1] / "results"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / "higher_order.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("=== 二、三、四阶角色迭代 ===")
    for row in rows:
        if row["round"] == 3:
            print(
                f"n={row['n']}, p={row['order']}: "
                f"width={row['width_float']}"
            )
    print("R4 = R2 ∘ R2: exact PASS")
    print(f"CSV: {path}")


if __name__ == "__main__":
    main()
