from __future__ import annotations

import numpy as np


def trapezoid_weights(x: np.ndarray) -> np.ndarray:
    if x.ndim != 1 or len(x) < 2:
        raise ValueError("x must be one-dimensional with at least two points")
    dx = np.diff(x)
    weights = np.empty_like(x, dtype=float)
    weights[0] = dx[0] / 2.0
    weights[-1] = dx[-1] / 2.0
    weights[1:-1] = (dx[:-1] + dx[1:]) / 2.0
    return weights


def smooth_bump(u: np.ndarray) -> np.ndarray:
    out = np.zeros_like(u, dtype=float)
    mask = np.abs(u) < 1.0
    out[mask] = np.exp(-1.0 / (1.0 - u[mask] ** 2))
    return out


def build_even_pair_basis(
    t: np.ndarray,
    support_radius: float,
    basis_size: int,
    bump_width: float,
    weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if support_radius <= 0:
        raise ValueError("support_radius must be positive")
    if not 0 < bump_width < support_radius:
        raise ValueError("bump_width must lie in (0, support_radius)")
    if basis_size < 4:
        raise ValueError("basis_size must be at least 4")

    max_center = support_radius - bump_width
    centers = np.linspace(0.0, max_center, basis_size)
    functions: list[np.ndarray] = []
    for center in centers:
        phi = smooth_bump((t - center) / bump_width)
        phi += smooth_bump((t + center) / bump_width)
        norm_sq = float(np.sum(weights * phi * phi))
        if norm_sq <= 0.0:
            raise RuntimeError("Degenerate basis function")
        functions.append(phi / np.sqrt(norm_sq))
    return np.asarray(functions), centers


def evaluate_basis_fourier(
    basis: np.ndarray,
    t: np.ndarray,
    weights: np.ndarray,
    points: np.ndarray,
    batch_size: int = 192,
) -> np.ndarray:
    weighted_basis = basis.T * weights[:, None]
    output = np.empty((len(points), basis.shape[0]), dtype=complex)
    for start in range(0, len(points), batch_size):
        stop = min(start + batch_size, len(points))
        exponential = np.exp(1j * np.outer(points[start:stop], t))
        output[start:stop] = exponential @ weighted_basis
    return output
