from __future__ import annotations

import csv
from dataclasses import dataclass
from math import floor, inf, nextafter
from pathlib import Path
from typing import Iterable

from mpmath import iv


def lower(x) -> float:
    return float(x.a)


def upper(x) -> float:
    return float(x.b)


def midpoint(x) -> float:
    return 0.5 * (lower(x) + upper(x))


def real_interval(value: str | float | int):
    return iv.mpf(str(value))


def sinh(x):
    return (iv.exp(x) - iv.exp(-x)) / 2


def cosh(x):
    return (iv.exp(x) + iv.exp(-x)) / 2


def tanh(x):
    return sinh(x) / cosh(x)


def interval_abs_upper(x) -> float:
    return max(abs(lower(x)), abs(upper(x)))


def complex_abs_upper(z) -> float:
    rl, rh = lower(z.real), upper(z.real)
    il, ih = lower(z.imag), upper(z.imag)
    value = max(abs(complex(r, i)) for r in (rl, rh) for i in (il, ih))
    return nextafter(value, inf)


@dataclass
class HatSplineModel:
    t: list
    base_values: list
    values: list
    h: object
    support_radius: object
    endpoint_correction: object
    endpoint_residual: object
    correlations: list

    @classmethod
    def from_csv(cls, path: str | Path, dps: int = 38) -> "HatSplineModel":
        iv.dps = dps
        rows: list[tuple[str, str]] = []
        with Path(path).open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                rows.append((row["t"], row["base_value"]))
        if len(rows) < 5:
            raise ValueError("At least five spline nodes are required")
        t = [iv.mpf(item[0]) for item in rows]
        base = [iv.mpf(item[1]) for item in rows]
        h = t[1] - t[0]
        for index in range(1, len(t) - 1):
            if not (lower(t[index + 1] - t[index] - h) <= 0 <= upper(t[index + 1] - t[index] - h)):
                raise ValueError("Nodes must be uniformly spaced")
        radius = -t[0]
        mid = (len(t) - 1) // 2
        # Fourier transform of a unit hat at w=i/2.
        qhat = h * (sinh(h / 4) / (h / 4)) ** 2
        weights = [qhat * iv.exp(-node / 2) for node in t]
        correction = -iv.fsum([base[i] * weights[i] for i in range(len(t))]) / weights[mid]
        values = list(base)
        values[mid] = values[mid] + correction
        residual = iv.fsum([values[i] * weights[i] for i in range(len(t))])
        correlations = []
        for lag in range(len(values)):
            correlations.append(
                iv.fsum([values[i] * values[i + lag] for i in range(len(values) - lag)])
            )
        return cls(t, base, values, h, radius, correction, residual, correlations)

    @property
    def size(self) -> int:
        return len(self.values)

    def r(self, lag: int):
        lag = abs(lag)
        if lag >= len(self.correlations):
            return iv.mpf(0)
        return self.correlations[lag]

    def cubic_weights(self, s):
        h = self.h
        return (
            h * (1 - s) ** 3 / 6,
            h * (iv.mpf(2) / 3 - s * s + s**3 / 2),
            h * (iv.mpf(2) / 3 - (1 - s) ** 2 + (1 - s) ** 3 / 2),
            h * s**3 / 6,
        )

    def correlation_interval(self, x_lo: float, x_hi: float):
        h_float = midpoint(self.h)
        if x_lo < 0 or x_hi < x_lo:
            raise ValueError("Require 0 <= x_lo <= x_hi")
        if x_lo >= 2 * midpoint(self.support_radius):
            return iv.mpf(0)
        cell = min(int(floor(x_lo / h_float + 1e-11)), self.size - 2)
        if x_hi > (cell + 1) * h_float + 1e-12:
            raise ValueError("Correlation interval may not cross a knot cell")
        s = iv.mpf([x_lo - cell * h_float, x_hi - cell * h_float]) / self.h
        wm, w0, w1, wp = self.cubic_weights(s)
        return (
            self.r(cell - 1) * wm
            + self.r(cell) * w0
            + self.r(cell + 1) * w1
            + self.r(cell + 2) * wp
        )

    def correlation_point(self, x: float | str):
        x_float = float(x)
        if x_float < 0:
            x_float = -x_float
            x = str(x_float)
        if x_float >= 2 * midpoint(self.support_radius):
            return iv.mpf(0)
        h_float = midpoint(self.h)
        cell = min(int(floor(x_float / h_float + 1e-11)), self.size - 2)
        x_interval = iv.mpf(str(x))
        s = (x_interval - cell * self.h) / self.h
        wm, w0, w1, wp = self.cubic_weights(s)
        return (
            self.r(cell - 1) * wm
            + self.r(cell) * w0
            + self.r(cell + 1) * w1
            + self.r(cell + 2) * wp
        )

    @property
    def c0(self):
        return self.correlation_point(0.0)

    def polynomial_sum(self, coefficients: Iterable, z):
        result = iv.mpc(0)
        for coefficient in reversed(list(coefficients)):
            result = result * z + coefficient
        return result

    def fourier_and_derivative(self, x: float, y: float):
        w = iv.mpc([x, x], [y, y])
        z = w * self.h / 2
        sinc = iv.sin(z) / z
        phi = self.h * sinc * sinc
        phi_prime = (
            self.h
            * self.h
            * sinc
            * (z * iv.cos(z) - iv.sin(z))
            / (z * z)
        )
        step = iv.exp(1j * w * self.h)
        phase = iv.exp(1j * w * self.t[0])
        spectral = phase * self.polynomial_sum(self.values, step)
        weighted = [self.t[i] * self.values[i] for i in range(self.size)]
        spectral_prime = 1j * phase * self.polynomial_sum(weighted, step)
        return phi * spectral, phi_prime * spectral + phi * spectral_prime

    def second_derivative_bound(self, max_abs_imag: float) -> float:
        total = 0.0
        h_float = midpoint(self.h)
        for node, value in zip(self.t, self.values):
            center = midpoint(node)
            support_max = max(abs(center - h_float), abs(center + h_float))
            total += (
                interval_abs_upper(value)
                * h_float
                * support_max**2
                * __import__("math").exp(max_abs_imag * support_max)
            )
        return nextafter(total, inf)

    def derivative_energy(self):
        return iv.fsum(
            [
                (self.values[i + 1] - self.values[i]) ** 2 / self.h
                for i in range(self.size - 1)
            ]
        )
