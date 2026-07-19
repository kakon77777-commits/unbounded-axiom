"""少年矩阵版与 L,U 角色符号版的逐轮精确比较。"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import csv


@dataclass(frozen=True)
class MatrixState:
    a: int
    b: int
    c: int
    d: int

    def square_expanded(self) -> "MatrixState":
        a, b, c, d = self.a, self.b, self.c, self.d
        return MatrixState(
            a=a * a + b * c,
            b=a * b + b * d,
            c=a * c + d * c,
            d=b * c + d * d,
        )

    def square_cse(self) -> "MatrixState":
        """公共子式消除后的同一矩阵平方。"""
        a, b, c, d = self.a, self.b, self.c, self.d
        diagonal_sum = a + d
        bc = b * c
        return MatrixState(
            a=a * a + bc,
            b=b * diagonal_sum,
            c=c * diagonal_sum,
            d=bc + d * d,
        )

    def role_bounds(self, n: int) -> tuple[Fraction, Fraction]:
        denominator = self.c + self.d
        lower = Fraction(
            self.a + self.b - self.c - self.d,
            denominator,
        )
        upper = Fraction(n, 1) / lower
        return lower, upper


@dataclass(frozen=True)
class BoundState:
    lower: Fraction
    upper: Fraction

    def step(self, n: int) -> "BoundState":
        shared_sum = self.lower + self.upper
        return BoundState(
            lower=Fraction(2 * n, 1) / shared_sum,
            upper=shared_sum / 2,
        )


def initial_matrix(n: int) -> MatrixState:
    return MatrixState(n + 3, 2 * n - 2, 2, n - 1)


def initial_bounds(n: int) -> BoundState:
    return BoundState(
        lower=Fraction(2 * n, n + 1),
        upper=Fraction(n + 1, 2),
    )


def generate_rows(ns=(2, 3, 10), rounds=6):
    rows = []
    for n in ns:
        matrix = initial_matrix(n)
        role = initial_bounds(n)
        for k in range(rounds):
            m_l, m_u = matrix.role_bounds(n)
            assert m_l == role.lower
            assert m_u == role.upper
            assert role.lower * role.upper == n
            assert matrix.square_expanded() == matrix.square_cse()

            rows.append(
                {
                    "n": n,
                    "round": k,
                    "matrix_lower": str(m_l),
                    "role_lower": str(role.lower),
                    "matrix_upper": str(m_u),
                    "role_upper": str(role.upper),
                    "width": str(role.upper - role.lower),
                    "lower_float": f"{float(role.lower):.17g}",
                    "upper_float": f"{float(role.upper):.17g}",
                    "width_float": f"{float(role.upper-role.lower):.17g}",
                    "exact_match": True,
                }
            )
            matrix = matrix.square_expanded()
            role = role.step(n)
    return rows


def main() -> None:
    rows = generate_rows()
    out_dir = Path(__file__).resolve().parents[1] / "results"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / "matrix_vs_role.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("=== 矩阵版 vs 角色符号版 ===")
    for row in rows:
        if row["n"] == 2:
            print(
                f"k={row['round']}: "
                f"L={row['lower_float']}, "
                f"U={row['upper_float']}, "
                f"width={row['width_float']}, "
                f"exact={row['exact_match']}"
            )
    print(f"CSV: {path}")


if __name__ == "__main__":
    main()
