"""RH-W-01 GBUMP generator and independent correlation implementations.

This module is an engineering validator, not a proof of RH or Weil positivity.
It constructs g = D(D+1)h from a compactly supported smooth log-bump.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


@dataclass(frozen=True)
class BumpParams:
    amplitude_real: float = 1.0
    amplitude_imag: float = 0.0
    mu: float = 0.2
    sigma: float = 0.7
    tau: float = 1.3

    def __post_init__(self) -> None:
        if not math.isfinite(self.sigma) or self.sigma <= 0:
            raise ValueError("sigma must be finite and > 0")
        for name, value in asdict(self).items():
            if not math.isfinite(value):
                raise ValueError(f"{name} must be finite")

    @property
    def amplitude(self) -> complex:
        return complex(self.amplitude_real, self.amplitude_imag)

    @property
    def log_support(self) -> tuple[float, float]:
        return self.mu - self.sigma, self.mu + self.sigma

    @property
    def x_support(self) -> tuple[float, float]:
        lo, hi = self.log_support
        return math.exp(lo), math.exp(hi)

    @property
    def correlation_x_support(self) -> tuple[float, float]:
        return math.exp(-2 * self.sigma), math.exp(2 * self.sigma)


def _arr(x: np.ndarray | float) -> np.ndarray:
    return np.asarray(x, dtype=float)


def eta(q: np.ndarray | float) -> np.ndarray:
    q = _arr(q)
    out = np.zeros(q.shape, dtype=float)
    mask = np.abs(q) < 1.0
    qm = q[mask]
    a = 1.0 - qm * qm
    out[mask] = np.exp(-1.0 / a)
    return out


def eta_prime(q: np.ndarray | float) -> np.ndarray:
    q = _arr(q)
    out = np.zeros(q.shape, dtype=float)
    mask = np.abs(q) < 1.0
    qm = q[mask]
    a = 1.0 - qm * qm
    e = np.exp(-1.0 / a)
    out[mask] = e * (-2.0 * qm / a**2)
    return out


def eta_second(q: np.ndarray | float) -> np.ndarray:
    q = _arr(q)
    out = np.zeros(q.shape, dtype=float)
    mask = np.abs(q) < 1.0
    qm = q[mask]
    a = 1.0 - qm * qm
    e = np.exp(-1.0 / a)
    fp = -2.0 * qm / a**2
    fpp = -2.0 / a**2 - 8.0 * qm * qm / a**3
    out[mask] = e * (fp * fp + fpp)
    return out


def log_seed(u: np.ndarray | float, p: BumpParams) -> np.ndarray:
    u = _arr(u)
    q = (u - p.mu) / p.sigma
    return p.amplitude * eta(q) * np.exp(1j * p.tau * u)


def log_generator(u: np.ndarray | float, p: BumpParams) -> np.ndarray:
    """Return g(e^u) = H''(u)+H'(u), H(u)=h(e^u)."""
    u = _arr(u)
    q = (u - p.mu) / p.sigma
    base = np.exp(1j * p.tau * u) * p.amplitude
    return base * (
        eta_second(q) / p.sigma**2
        + (1.0 + 2j * p.tau) * eta_prime(q) / p.sigma
        + (1j * p.tau - p.tau**2) * eta(q)
    )


def g_of_x(x: np.ndarray | float, p: BumpParams) -> np.ndarray:
    x_arr = np.asarray(x, dtype=float)
    out = np.zeros(x_arr.shape, dtype=complex)
    mask = x_arr > 0
    out[mask] = log_generator(np.log(x_arr[mask]), p)
    return out


def _gauss_interval(lo: float, hi: float, n: int) -> tuple[np.ndarray, np.ndarray]:
    if n < 8:
        raise ValueError("quadrature order must be >= 8")
    z, w = leggauss(n)
    return 0.5 * (hi - lo) * z + 0.5 * (hi + lo), 0.5 * (hi - lo) * w


def mellin_seed(s: complex, p: BumpParams, order: int = 600) -> complex:
    lo, hi = p.log_support
    u, w = _gauss_interval(lo, hi, order)
    return complex(np.sum(w * log_seed(u, p) * np.exp(s * u)))


def mellin_g(s: complex, p: BumpParams, order: int = 600) -> complex:
    lo, hi = p.log_support
    u, w = _gauss_interval(lo, hi, order)
    return complex(np.sum(w * log_generator(u, p) * np.exp(s * u)))


def phi(u: np.ndarray | float, p: BumpParams) -> np.ndarray:
    u = _arr(u)
    return np.exp(u / 2.0) * log_generator(u, p)


def _overlap_for_shift(v: float, p: BumpParams) -> tuple[float, float] | None:
    lo, hi = p.log_support
    left = max(lo, lo - v)
    right = min(hi, hi - v)
    if left >= right:
        return None
    return left, right


def correlation_multiplicative(x: float, p: BumpParams, order: int = 300) -> complex:
    """Directly computes integral g(xy) conjugate(g(y)) dy in log-y coordinates."""
    if x <= 0:
        raise ValueError("x must be positive")
    v = math.log(x)
    overlap = _overlap_for_shift(v, p)
    if overlap is None:
        return 0j
    u, w = _gauss_interval(*overlap, order)
    value = np.sum(
        w
        * log_generator(u + v, p)
        * np.conj(log_generator(u, p))
        * np.exp(u)
    )
    return complex(value)


def correlation_additive(x: float, p: BumpParams, order: int = 300) -> complex:
    """Computes the same correlation through e^{-v/2} autocorrelation(phi)."""
    if x <= 0:
        raise ValueError("x must be positive")
    v = math.log(x)
    overlap = _overlap_for_shift(v, p)
    if overlap is None:
        return 0j
    u, w = _gauss_interval(*overlap, order)
    value = math.exp(-v / 2.0) * np.sum(w * phi(u + v, p) * np.conj(phi(u, p)))
    return complex(value)


def mellin_correlation(s: complex, p: BumpParams, order_v: int = 300, order_u: int = 400) -> complex:
    vlo, vhi = -2.0 * p.sigma, 2.0 * p.sigma
    v, w = _gauss_interval(vlo, vhi, order_v)
    f_values = np.array(
        [correlation_additive(math.exp(float(vv)), p, order=order_u) for vv in v],
        dtype=complex,
    )
    return complex(np.sum(w * f_values * np.exp(s * v)))


def write_params(path: str, p: BumpParams) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(asdict(p), fh, ensure_ascii=False, indent=2)
        fh.write("\n")
