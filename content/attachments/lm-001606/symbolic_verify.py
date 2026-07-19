"""SymPy 符号验证。"""

import sympy as sp


def main() -> None:
    n, x, l, u = sp.symbols("n x l u", positive=True)
    r = sp.sqrt(n)
    projective_error = lambda z: (r - z) / (r + z)

    r2 = 2 * n * x / (n + x**2)
    r3 = x * (3 * n + x**2) / (n + 3 * x**2)
    r4 = 4 * n * x * (n + x**2) / (
        n**2 + 6 * n * x**2 + x**4
    )

    for p, expr in ((2, r2), (3, r3), (4, r4)):
        assert sp.factor(projective_error(expr) - projective_error(x) ** p) == 0
        print(f"rho(R_{p}(x)) = rho(x)^{p}: PASS")

    pair2 = (
        2 * l * u / (l + u),
        (l + u) / 2,
    )
    pair3 = (
        l * (l + 3 * u) / (3 * l + u),
        u * (3 * l + u) / (l + 3 * u),
    )
    pair4 = (
        4 * l * u * (l + u) / (l**2 + 6 * l * u + u**2),
        (l**2 + 6 * l * u + u**2) / (4 * (l + u)),
    )

    for p, (low, high) in ((2, pair2), (3, pair3), (4, pair4)):
        assert sp.factor(low * high - l * u) == 0
        print(f"p={p}, L' U' = L U: PASS")

    assert sp.factor(r2.subs({x: l, n: l * u}) - pair2[0]) == 0
    assert sp.factor(r3.subs({x: l, n: l * u}) - pair3[0]) == 0
    assert sp.factor(r4.subs({x: l, n: l * u}) - pair4[0]) == 0
    print("单变量与角色符号形式：PASS")

    assert sp.factor(r2.subs(x, r2) - r4) == 0
    print("R4 = R2 composed with R2: PASS")


if __name__ == "__main__":
    main()
