from __future__ import annotations

from dataclasses import asdict, dataclass
from math import hypot, inf, nextafter

from .model import HatSplineModel, complex_abs_upper, lower, upper


@dataclass(frozen=True)
class CertifiedCell:
    x_lo: float
    x_hi: float
    y_lo: float
    y_hi: float
    depth: int
    block_upper: float


@dataclass
class RegionCertificate:
    certified: list[CertifiedCell]
    unresolved: list[CertifiedCell]
    second_derivative_bound: float

    @property
    def global_upper(self) -> float:
        return max(cell.block_upper for cell in self.certified)

    @property
    def max_depth_used(self) -> int:
        return max(cell.depth for cell in self.certified)

    def to_dict(self) -> dict:
        return {
            "certified_cell_count": len(self.certified),
            "unresolved_cell_count": len(self.unresolved),
            "global_block_upper": self.global_upper,
            "max_depth_used": self.max_depth_used,
            "second_derivative_bound": self.second_derivative_bound,
            "continuous_region_certified_negative": not self.unresolved and self.global_upper < 0,
        }


def _point_rectangle_radius(z) -> tuple[complex, float]:
    rl, rh = lower(z.real), upper(z.real)
    il, ih = lower(z.imag), upper(z.imag)
    center = complex(0.5 * (rl + rh), 0.5 * (il + ih))
    radius = max(abs(complex(r, i) - center) for r in (rl, rh) for i in (il, ih))
    return center, nextafter(radius, inf)


def certify_region(
    model: HatSplineModel,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    initial_nx: int,
    initial_ny: int,
    max_depth: int,
) -> RegionCertificate:
    m2 = model.second_derivative_bound(max(abs(y_min), abs(y_max)))
    pending: list[tuple[float, float, float, float, int]] = []
    for ix in range(initial_nx):
        x0 = x_min + (x_max - x_min) * ix / initial_nx
        x1 = x_min + (x_max - x_min) * (ix + 1) / initial_nx
        for iy in range(initial_ny):
            y0 = y_min + (y_max - y_min) * iy / initial_ny
            y1 = y_min + (y_max - y_min) * (iy + 1) / initial_ny
            pending.append((x0, x1, y0, y1, 0))

    certified: list[CertifiedCell] = []
    unresolved: list[CertifiedCell] = []
    while pending:
        x0, x1, y0, y1, depth = pending.pop()
        xc, yc = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
        g, gp = model.fourier_and_derivative(xc, yc)
        center, point_radius = _point_rectangle_radius(g)
        gp_upper = complex_abs_upper(gp)
        cell_radius = nextafter(hypot(0.5 * (x1 - x0), 0.5 * (y1 - y0)), inf)
        error_radius = nextafter(
            point_radius
            + gp_upper * cell_radius
            + 0.5 * m2 * cell_radius * cell_radius,
            inf,
        )
        block_upper = 2.0 * (
            (center * center).real
            + 2.0 * abs(center) * error_radius
            + error_radius * error_radius
        )
        block_upper = nextafter(block_upper, inf)
        record = CertifiedCell(x0, x1, y0, y1, depth, block_upper)
        if block_upper < 0:
            certified.append(record)
        elif depth < max_depth:
            xm, ym = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
            next_depth = depth + 1
            pending.extend(
                [
                    (x0, xm, y0, ym, next_depth),
                    (xm, x1, y0, ym, next_depth),
                    (x0, xm, ym, y1, next_depth),
                    (xm, x1, ym, y1, next_depth),
                ]
            )
        else:
            unresolved.append(record)
    return RegionCertificate(certified, unresolved, m2)
