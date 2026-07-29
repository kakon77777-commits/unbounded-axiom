import sympy as sp
from pathlib import Path

a, b, x, u, v, L = sp.symbols("a b x u v L", positive=True, real=True)

identities = {
    "gplm_product":
        sp.simplify((x / a) * (b / x) - b / a),
    "geometric_balance":
        sp.simplify((sp.sqrt(a * b) / a) - (b / sp.sqrt(a * b))),
    "straight_segment_squared_average":
        sp.expand(
            (((u + L / 2) ** 2 + v ** 2)
             + ((u - L / 2) ** 2 + v ** 2)) / 2
            - L ** 2 / 4
        ),
}

report = [
    "# Symbolic Identity Report",
    "",
    "The following expressions were simplified symbolically.",
    "",
]
for name, expr in identities.items():
    report.append(f"- **{name}**: `{sp.sstr(expr)}`")

report.extend([
    "",
    "Interpretation:",
    "",
    "- `gplm_product = 0` proves the two endpoint ratios have fixed product `b/a`.",
    "- `geometric_balance = 0` proves the geometric center equalizes the two ratios.",
    "- the straight-segment expression reduces to `u**2 + v**2`, which is nonnegative.",
])

Path(__file__).with_name("symbolic_report.md").write_text(
    "\n".join(report), encoding="utf-8"
)
print("\n".join(report))
