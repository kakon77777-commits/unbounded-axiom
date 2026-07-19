"""高精度验证 lchuh5478 视频中展示的三条 pi 公式。

仅使用 Python 标准库 Decimal。
参考 pi 由 Machin 公式生成，而不是调用 math.pi。
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from pathlib import Path
import csv


def atan_series(x: Decimal, precision: int) -> Decimal:
    """对 |x|<1 使用 arctan(x)=x-x^3/3+x^5/5-...。"""
    with localcontext() as ctx:
        ctx.prec = precision + 20
        x2 = x * x
        term_power = x
        total = x
        k = 1
        threshold = Decimal(10) ** (-(precision + 8))
        sign = -1
        while True:
            term_power *= x2
            term = term_power / Decimal(2 * k + 1)
            if abs(term) < threshold:
                break
            total = total + term if sign > 0 else total - term
            sign *= -1
            k += 1
        ctx.prec = precision
        return +total


def machin_pi(precision: int) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision + 20
        value = (
            Decimal(16) * atan_series(Decimal(1) / Decimal(5), precision + 10)
            - Decimal(4) * atan_series(Decimal(1) / Decimal(239), precision + 10)
        )
        ctx.prec = precision
        return +value


def geometric_4k_sum(q: Decimal, precision: int) -> tuple[Decimal, int]:
    """计算 sum_{i>=0} 1/((4i+1) q^i)。"""
    with localcontext() as ctx:
        ctx.prec = precision + 20
        total = Decimal(0)
        q_power = Decimal(1)
        threshold = Decimal(10) ** (-(precision + 10))
        i = 0
        while True:
            term = Decimal(1) / (Decimal(4 * i + 1) * q_power)
            total += term
            if abs(term) < threshold:
                break
            q_power *= q
            i += 1
            if i > 1_000_000:
                raise RuntimeError("级数未按预期收敛")
        ctx.prec = precision
        return +total, i + 1


def formula_values(precision: int = 100) -> list[dict[str, object]]:
    with localcontext() as ctx:
        ctx.prec = precision + 30
        two = Decimal(2)
        three = Decimal(3)
        sqrt2 = two.sqrt()
        sqrt3 = three.sqrt()

        specs = [
            {
                "name": "pi_formula_1",
                "coefficient": Decimal(4) * sqrt3,
                "q": Decimal(9),
                "log_arg": Decimal(26) + Decimal(15) * sqrt3,
            },
            {
                "name": "pi_formula_2",
                "coefficient": Decimal(16) * (sqrt2 - Decimal(1)),
                "q": Decimal(17) + Decimal(12) * sqrt2,
                "log_arg": Decimal(17) + Decimal(12) * sqrt2,
            },
            {
                "name": "pi_formula_3",
                "coefficient": Decimal(24) * (Decimal(2) - sqrt3),
                "q": Decimal(97) + Decimal(56) * sqrt3,
                "log_arg": Decimal(27),
            },
        ]

        reference = machin_pi(precision + 10)
        rows = []
        for spec in specs:
            series, terms = geometric_4k_sum(spec["q"], precision + 10)
            value = spec["coefficient"] * series - spec["log_arg"].ln()
            error = value - reference
            rows.append(
                {
                    "formula": spec["name"],
                    "terms": terms,
                    "value": value,
                    "reference_pi": reference,
                    "signed_error": error,
                    "absolute_error": abs(error),
                }
            )
        return rows


def main() -> None:
    rows = formula_values(100)
    out_dir = Path(__file__).resolve().parents[1] / "results"
    out_dir.mkdir(exist_ok=True)
    csv_path = out_dir / "pi_verification.csv"

    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "formula",
                "terms",
                "value",
                "reference_pi",
                "signed_error",
                "absolute_error",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({k: str(v) for k, v in row.items()})

    print("=== 三条 pi 公式高精度验证 ===")
    for row in rows:
        print(row["formula"])
        print(f"  terms        = {row['terms']}")
        print(f"  abs(error)   = {row['absolute_error']}")
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    main()
