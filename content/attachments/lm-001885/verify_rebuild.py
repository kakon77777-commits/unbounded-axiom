from fractions import Fraction
from random import Random
from typing import List, Tuple
import json
from pathlib import Path

Q = Fraction
Point = Tuple[Q, Q]


def gplm_certificate(a: Q, b: Q, x: Q) -> dict:
    """Exact rational certificate for max(x/a,b/x)^2 >= b/a."""
    assert 0 < a <= b and x > 0
    u = x / a
    v = b / x
    m = max(u, v)
    return {
        "a": str(a),
        "b": str(b),
        "x": str(x),
        "left_ratio": str(u),
        "right_ratio": str(v),
        "max_ratio": str(m),
        "certificate_gap_squared": str(m * m - b / a),
        "valid": m * m >= b / a,
        "balanced": u == v,
        "balance_equation": x * x == a * b,
    }


def midpoint_on_axis_chain(points: List[Point]) -> Tuple[Point, Q]:
    """Exact arc-length midpoint for a rational axis-aligned polyline."""
    assert len(points) >= 2
    lengths = []
    total = Q(0)
    for p, q in zip(points, points[1:]):
        dx, dy = q[0] - p[0], q[1] - p[1]
        assert dx == 0 or dy == 0
        seg = abs(dx) + abs(dy)
        assert seg > 0
        lengths.append(seg)
        total += seg

    target = total / 2
    walked = Q(0)
    for (p, q), seg in zip(zip(points, points[1:]), lengths):
        if walked + seg >= target:
            remain = target - walked
            dx, dy = q[0] - p[0], q[1] - p[1]
            if dx != 0:
                sign = Q(1) if dx > 0 else Q(-1)
                return (p[0] + sign * remain, p[1]), total
            sign = Q(1) if dy > 0 else Q(-1)
            return (p[0], p[1] + sign * remain), total
        walked += seg
    raise AssertionError("midpoint not found")


def sqdist(p: Point, q: Point) -> Q:
    dx, dy = p[0] - q[0], p[1] - q[1]
    return dx * dx + dy * dy


def circular_chain_certificate(points: List[Point]) -> dict:
    center, total = midpoint_on_axis_chain(points)
    radius = total / 2
    margins = [radius * radius - sqdist(p, center) for p in points]

    # On each affine segment, squared distance to a fixed center is convex.
    # Therefore its maximum on the segment is attained at an endpoint.
    return {
        "points": [[str(x), str(y)] for x, y in points],
        "center": [str(center[0]), str(center[1])],
        "length": str(total),
        "radius": str(radius),
        "minimum_squared_margin_over_vertices": str(min(margins)),
        "valid": min(margins) >= 0,
    }


def random_axis_chain(rng: Random, nseg: int) -> List[Point]:
    x, y = Q(0), Q(0)
    points = [(x, y)]
    horizontal = True
    for _ in range(nseg):
        step = Q(rng.randint(1, 9), rng.randint(1, 4))
        sign = 1 if rng.random() < 0.5 else -1
        if horizontal:
            x += sign * step
        else:
            y += sign * step
        points.append((x, y))
        horizontal = not horizontal
    return points


def run_all() -> dict:
    gplm_cases = []

    # Equality cases with rational geometric mean.
    for p, q in [(1, 2), (2, 5), (3, 7), (5, 11)]:
        gplm_cases.append(
            gplm_certificate(Q(p * p), Q(q * q), Q(p * q))
        )

    # Strict inequality cases.
    gplm_cases.extend([
        gplm_certificate(Q(1), Q(16), Q(2)),
        gplm_certificate(Q(1), Q(16), Q(8)),
        gplm_certificate(Q(4), Q(25), Q(6)),
    ])

    assert all(case["valid"] for case in gplm_cases)
    assert all(
        case["balanced"] == case["balance_equation"]
        for case in gplm_cases
    )

    rng = Random(20260726)
    circle_cases = [
        circular_chain_certificate(random_axis_chain(rng, nseg))
        for nseg in range(2, 42)
    ]
    assert all(case["valid"] for case in circle_cases)

    straight_segment = {
        "identity":
            "(((u+L/2)^2+v^2)+((u-L/2)^2+v^2))/2-L^2/4=u^2+v^2",
        "conclusion":
            "At least one endpoint has squared distance >= L^2/4; radius >= L/2.",
        "valid_over_reals": True,
    }

    return {
        "summary": {
            "gplm_cases_checked": len(gplm_cases),
            "axis_aligned_chain_cases_checked": len(circle_cases),
            "all_passed": True,
            "arithmetic": "exact fractions; no floating-point acceptance tests",
        },
        "gplm_cases": gplm_cases,
        "circular_container_cases": circle_cases,
        "straight_segment_lower_bound": straight_segment,
    }


if __name__ == "__main__":
    result = run_all()
    out = Path(__file__).with_name("verification_results.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
