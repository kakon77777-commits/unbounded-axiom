from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction

import numpy as np


@dataclass(frozen=True)
class Patch:
    patch_id: str
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    guard_dx: float = 0.025
    guard_dy: float = 0.0125

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    def points(self, nx: int, ny: int) -> np.ndarray:
        xs = np.linspace(self.x_min, self.x_max, nx)
        ys = np.linspace(self.y_min, self.y_max, ny)
        return (xs[:, None] + 1j * ys[None, :]).reshape(-1)

    def guard_ring(self, nx: int, ny: int) -> np.ndarray:
        xs = np.linspace(self.x_min - self.guard_dx, self.x_max + self.guard_dx, nx)
        ys = np.linspace(self.y_min - self.guard_dy, self.y_max + self.guard_dy, ny)
        xx, yy = np.meshgrid(xs, ys, indexing="ij")
        inside = (
            (xx >= self.x_min)
            & (xx <= self.x_max)
            & (yy >= self.y_min)
            & (yy <= self.y_max)
        )
        return (xx[~inside] + 1j * yy[~inside]).reshape(-1)


def default_cover() -> list[Patch]:
    coarse_x_bands = [
        ("X0", 20.00, 20.20),
        ("X1", 20.15, 20.35),
        ("X2", 20.30, 20.50),
    ]
    fine_x_bands = [
        ("x0", 20.00, 20.10),
        ("x1", 20.08, 20.18),
        ("x2", 20.16, 20.26),
        ("x3", 20.24, 20.34),
        ("x4", 20.32, 20.42),
        ("x5", 20.40, 20.50),
    ]
    distance_bands = [
        ("Y0", -0.200, -0.160, coarse_x_bands, 0.025, 0.008),
        ("Y1", -0.170, -0.135, coarse_x_bands, 0.025, 0.008),
        ("Y2", -0.145, -0.115, fine_x_bands, 0.015, 0.006),
        ("Y3", -0.125, -0.100, fine_x_bands, 0.015, 0.006),
    ]
    patches = []
    for y_name, y0, y1, x_bands, guard_dx, guard_dy in distance_bands:
        patches.extend(
            Patch(
                f"{x_name}_{y_name}",
                x0,
                x1,
                y0,
                y1,
                guard_dx=guard_dx,
                guard_dy=guard_dy,
            )
            for x_name, x0, x1 in x_bands
        )
    return patches


def coarse_cover() -> list[Patch]:
    """Six-patch isotropic baseline retained for the refinement ablation."""
    x_bands = [
        ("X0", 20.00, 20.20),
        ("X1", 20.15, 20.35),
        ("X2", 20.30, 20.50),
    ]
    y_bands = [
        ("Y0", -0.20, -0.14),
        ("Y1", -0.16, -0.10),
    ]
    return [
        Patch(f"{x_name}_{y_name}", x0, x1, y0, y1)
        for x_name, x0, x1 in x_bands
        for y_name, y0, y1 in y_bands
    ]


def refined_cover(
    patches: list[Patch],
    split_x: int,
    split_y: int,
) -> list[Patch]:
    """Subdivide every patch while preserving a deterministic lineage id."""
    if split_x < 1 or split_y < 1:
        raise ValueError("split counts must be positive")
    output: list[Patch] = []
    for patch in patches:
        xs = np.linspace(patch.x_min, patch.x_max, split_x + 1)
        ys = np.linspace(patch.y_min, patch.y_max, split_y + 1)
        for x_index in range(split_x):
            for y_index in range(split_y):
                output.append(
                    Patch(
                        patch_id=(
                            f"{patch.patch_id}__r"
                            f"{x_index}_{y_index}"
                        ),
                        x_min=float(xs[x_index]),
                        x_max=float(xs[x_index + 1]),
                        y_min=float(ys[y_index]),
                        y_max=float(ys[y_index + 1]),
                        guard_dx=patch.guard_dx / split_x,
                        guard_dy=patch.guard_dy / split_y,
                    )
                )
    return output


def _interval_union_audit(
    target: tuple[str, str],
    intervals: list[tuple[str, str]],
) -> dict[str, object]:
    left, right = map(Fraction, target)
    ordered = sorted((Fraction(a), Fraction(b)) for a, b in intervals)
    cursor = left
    gaps: list[tuple[str, str]] = []
    for a, b in ordered:
        if b < left or a > right:
            continue
        a = max(a, left)
        b = min(b, right)
        if a > cursor:
            gaps.append((str(cursor), str(a)))
        cursor = max(cursor, b)
    if cursor < right:
        gaps.append((str(cursor), str(right)))
    return {
        "target": [str(left), str(right)],
        "intervals": [[str(a), str(b)] for a, b in ordered],
        "gaps": gaps,
        "covered_exactly_as_rational_intervals": not gaps,
    }


def coverage_audit(patches: list[Patch]) -> dict[str, object]:
    x_intervals = sorted(
        {(str(p.x_min), str(p.x_max)) for p in patches},
        key=lambda item: Fraction(item[0]),
    )
    y_intervals = sorted(
        {(str(p.y_min), str(p.y_max)) for p in patches},
        key=lambda item: Fraction(item[0]),
    )
    x_audit = _interval_union_audit(("20", "20.5"), x_intervals)
    y_audit = _interval_union_audit(("-0.2", "-0.1"), y_intervals)

    target_x = (Fraction("20"), Fraction("20.5"))
    target_y = (Fraction("-0.2"), Fraction("-0.1"))
    rational_patches = [
        (
            Fraction(str(p.x_min)),
            Fraction(str(p.x_max)),
            Fraction(str(p.y_min)),
            Fraction(str(p.y_max)),
        )
        for p in patches
    ]
    x_breaks = sorted(
        {target_x[0], target_x[1]}
        | {
            value
            for x0, x1, _, _ in rational_patches
            for value in (max(target_x[0], x0), min(target_x[1], x1))
            if target_x[0] <= value <= target_x[1]
        }
    )
    y_breaks = sorted(
        {target_y[0], target_y[1]}
        | {
            value
            for _, _, y0, y1 in rational_patches
            for value in (max(target_y[0], y0), min(target_y[1], y1))
            if target_y[0] <= value <= target_y[1]
        }
    )
    x_probes = sorted(
        set(x_breaks)
        | {
            (left + right) / 2
            for left, right in zip(x_breaks[:-1], x_breaks[1:])
        }
    )
    y_probes = sorted(
        set(y_breaks)
        | {
            (left + right) / 2
            for left, right in zip(y_breaks[:-1], y_breaks[1:])
        }
    )
    uncovered_rational_probes = []
    for x in x_probes:
        for y in y_probes:
            if not any(
                x0 <= x <= x1 and y0 <= y <= y1
                for x0, x1, y0, y1 in rational_patches
            ):
                uncovered_rational_probes.append([str(x), str(y)])

    xs = np.linspace(20.0, 20.5, 501)
    ys = np.linspace(-0.2, -0.1, 301)
    xx, yy = np.meshgrid(xs, ys, indexing="ij")
    multiplicity = np.zeros_like(xx, dtype=int)
    for patch in patches:
        multiplicity += (
            (xx >= patch.x_min)
            & (xx <= patch.x_max)
            & (yy >= patch.y_min)
            & (yy <= patch.y_max)
        )
    return {
        "target": {
            "x": ["20", "20.5"],
            "y": ["-0.2", "-0.1"],
        },
        "x_audit": x_audit,
        "y_audit": y_audit,
        "adaptive_anisotropic_structure": True,
        "rational_atomic_probe_count": len(x_probes) * len(y_probes),
        "rational_uncovered_probes": uncovered_rational_probes,
        "covered_exactly_on_rational_atomic_cells": not uncovered_rational_probes,
        "dense_grid_uncovered_count": int(np.sum(multiplicity == 0)),
        "dense_grid_min_multiplicity": int(np.min(multiplicity)),
        "dense_grid_max_multiplicity": int(np.max(multiplicity)),
        "cover_pass": bool(
            x_audit["covered_exactly_as_rational_intervals"]
            and y_audit["covered_exactly_as_rational_intervals"]
            and not uncovered_rational_probes
            and np.min(multiplicity) >= 1
        ),
    }
