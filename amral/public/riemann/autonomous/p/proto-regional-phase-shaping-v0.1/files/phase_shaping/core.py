from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np
from scipy.linalg import null_space


@dataclass(frozen=True)
class PhaseShapingConfig:
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    support_radius: float = 10.0
    basis_size: int = 32
    bump_width: float = 0.18
    quadrature_points: int = 5001
    fit_nx: int = 18
    fit_ny: int = 10
    check_nx: int = 81
    check_ny: int = 41
    ridge: float = 1e-5
    target_imag: float = 1.0

    def validate(self) -> None:
        if not self.x_min < self.x_max:
            raise ValueError("x_min must be smaller than x_max")
        if not self.y_min < self.y_max < 0:
            raise ValueError("Require y_min < y_max < 0 for a lower-half-plane target")
        if self.support_radius <= 0:
            raise ValueError("support_radius must be positive")
        if self.bump_width <= 0 or self.bump_width >= self.support_radius:
            raise ValueError("bump_width must lie in (0, support_radius)")
        if self.basis_size < 4:
            raise ValueError("basis_size must be at least 4")
        if self.quadrature_points < 1001 or self.quadrature_points % 2 == 0:
            raise ValueError("quadrature_points must be an odd integer >= 1001")
        if min(self.fit_nx, self.fit_ny, self.check_nx, self.check_ny) < 2:
            raise ValueError("grid dimensions must be at least 2")


@dataclass
class PhaseShapingResult:
    config: PhaseShapingConfig
    coefficients: np.ndarray
    centers: np.ndarray
    t: np.ndarray
    psi: np.ndarray
    check_x: np.ndarray
    check_y: np.ndarray
    G_grid: np.ndarray
    block_grid: np.ndarray
    endpoint_value: complex
    endpoint_residual: float
    symmetry_even_residual: float
    symmetry_real_residual: float
    max_target_error: float
    grid_block_max: float
    grid_block_min: float
    l1_weighted_psi: float
    l1_weighted_tpsi: float
    gradient_bound: float
    cell_radius: float
    continuous_upper_estimate: float

    @property
    def grid_negative(self) -> bool:
        return bool(self.grid_block_max < 0.0)

    @property
    def estimated_continuous_negative(self) -> bool:
        return bool(self.continuous_upper_estimate < 0.0)

    def summary_dict(self) -> dict[str, Any]:
        return {
            "config": asdict(self.config),
            "coefficients": self.coefficients.tolist(),
            "centers": self.centers.tolist(),
            "endpoint_value": {
                "real": float(self.endpoint_value.real),
                "imag": float(self.endpoint_value.imag),
            },
            "endpoint_residual": float(self.endpoint_residual),
            "symmetry_even_residual": float(self.symmetry_even_residual),
            "symmetry_real_residual": float(self.symmetry_real_residual),
            "max_target_error": float(self.max_target_error),
            "grid_block_max": float(self.grid_block_max),
            "grid_block_min": float(self.grid_block_min),
            "grid_negative": self.grid_negative,
            "l1_weighted_psi": float(self.l1_weighted_psi),
            "l1_weighted_tpsi": float(self.l1_weighted_tpsi),
            "gradient_bound": float(self.gradient_bound),
            "cell_radius": float(self.cell_radius),
            "continuous_upper_estimate": float(self.continuous_upper_estimate),
            "estimated_continuous_negative": self.estimated_continuous_negative,
            "warning": (
                "All bounds are floating-point prototype estimates, not interval-arithmetic proofs."
            ),
        }


def _trap_weights(t: np.ndarray) -> np.ndarray:
    dt = np.diff(t)
    weights = np.empty_like(t)
    weights[0] = dt[0] / 2.0
    weights[-1] = dt[-1] / 2.0
    weights[1:-1] = (dt[:-1] + dt[1:]) / 2.0
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
    max_center = support_radius - bump_width
    centers = np.linspace(0.0, max_center, basis_size)
    basis: list[np.ndarray] = []
    for center in centers:
        phi = smooth_bump((t - center) / bump_width)
        phi += smooth_bump((t + center) / bump_width)
        norm_sq = float(np.sum(weights * phi * phi))
        if norm_sq <= 0.0:
            raise RuntimeError("Degenerate basis function")
        basis.append(phi / np.sqrt(norm_sq))
    return np.asarray(basis), centers


def evaluate_basis_fourier(
    basis: np.ndarray,
    t: np.ndarray,
    weights: np.ndarray,
    points: np.ndarray,
    batch_size: int = 256,
) -> np.ndarray:
    weighted_basis = basis.T * weights[:, None]
    out = np.empty((len(points), basis.shape[0]), dtype=complex)
    for start in range(0, len(points), batch_size):
        stop = min(start + batch_size, len(points))
        exponential = np.exp(1j * np.outer(points[start:stop], t))
        out[start:stop] = exponential @ weighted_basis
    return out


def _grid_points(
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    nx: int,
    ny: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    xs = np.linspace(x_min, x_max, nx)
    ys = np.linspace(y_min, y_max, ny)
    points = (xs[:, None] + 1j * ys[None, :]).reshape(-1)
    return xs, ys, points


def fit_phase_shaper(config: PhaseShapingConfig) -> PhaseShapingResult:
    config.validate()
    t = np.linspace(
        -config.support_radius,
        config.support_radius,
        config.quadrature_points,
    )
    weights = _trap_weights(t)
    basis, centers = build_even_pair_basis(
        t=t,
        support_radius=config.support_radius,
        basis_size=config.basis_size,
        bump_width=config.bump_width,
        weights=weights,
    )

    _, _, fit_points = _grid_points(
        config.x_min,
        config.x_max,
        config.y_min,
        config.y_max,
        config.fit_nx,
        config.fit_ny,
    )
    fit_matrix = evaluate_basis_fourier(basis, t, weights, fit_points)

    endpoint_row = evaluate_basis_fourier(
        basis, t, weights, np.asarray([0.5j], dtype=complex)
    )[0]
    if np.max(np.abs(endpoint_row.imag)) > 1e-8:
        raise RuntimeError("Even real basis should have a real endpoint row")

    kernel = null_space(endpoint_row.real[None, :])
    if kernel.shape[1] == 0:
        raise RuntimeError("Endpoint constraint has no nonzero nullspace")

    real_system = np.vstack((fit_matrix.real, fit_matrix.imag)) @ kernel
    target = np.concatenate(
        (
            np.zeros(len(fit_points)),
            np.full(len(fit_points), config.target_imag),
        )
    )
    normal = real_system.T @ real_system
    rhs = real_system.T @ target
    reduced = np.linalg.solve(
        normal + config.ridge * np.eye(normal.shape[0]), rhs
    )
    coefficients = kernel @ reduced
    psi = coefficients @ basis

    check_x, check_y, check_points = _grid_points(
        config.x_min,
        config.x_max,
        config.y_min,
        config.y_max,
        config.check_nx,
        config.check_ny,
    )
    check_matrix = evaluate_basis_fourier(
        basis, t, weights, check_points, batch_size=128
    )
    G_values = check_matrix @ coefficients
    block_values = 2.0 * np.real(G_values**2)
    G_grid = G_values.reshape(config.check_nx, config.check_ny)
    block_grid = block_values.reshape(config.check_nx, config.check_ny)

    endpoint_value = complex(endpoint_row @ coefficients)

    probe = np.asarray(
        [
            complex(config.x_min, config.y_min),
            complex(config.x_max, config.y_max),
            complex((config.x_min + config.x_max) / 2.0, (config.y_min + config.y_max) / 2.0),
        ]
    )
    probe_values = evaluate_basis_fourier(basis, t, weights, probe) @ coefficients
    even_values = evaluate_basis_fourier(basis, t, weights, -probe) @ coefficients
    conjugate_values = (
        evaluate_basis_fourier(basis, t, weights, np.conjugate(probe))
        @ coefficients
    )
    symmetry_even_residual = float(np.max(np.abs(probe_values - even_values)))
    symmetry_real_residual = float(
        np.max(np.abs(conjugate_values - np.conjugate(probe_values)))
    )

    target_complex = 1j * config.target_imag
    max_target_error = float(np.max(np.abs(G_values - target_complex)))
    grid_block_max = float(np.max(block_values))
    grid_block_min = float(np.min(block_values))

    y_abs = max(abs(config.y_min), abs(config.y_max))
    exponential_weight = np.exp(y_abs * np.abs(t))
    l1_weighted_psi = float(np.sum(weights * np.abs(psi) * exponential_weight))
    l1_weighted_tpsi = float(
        np.sum(weights * np.abs(t * psi) * exponential_weight)
    )
    gradient_bound = float(
        4.0 * np.sqrt(2.0) * l1_weighted_psi * l1_weighted_tpsi
    )
    dx = (config.x_max - config.x_min) / (config.check_nx - 1)
    dy = (config.y_max - config.y_min) / (config.check_ny - 1)
    cell_radius = float(0.5 * np.sqrt(dx * dx + dy * dy))
    continuous_upper_estimate = float(
        grid_block_max + gradient_bound * cell_radius
    )

    return PhaseShapingResult(
        config=config,
        coefficients=coefficients,
        centers=centers,
        t=t,
        psi=psi,
        check_x=check_x,
        check_y=check_y,
        G_grid=G_grid,
        block_grid=block_grid,
        endpoint_value=endpoint_value,
        endpoint_residual=abs(endpoint_value),
        symmetry_even_residual=symmetry_even_residual,
        symmetry_real_residual=symmetry_real_residual,
        max_target_error=max_target_error,
        grid_block_max=grid_block_max,
        grid_block_min=grid_block_min,
        l1_weighted_psi=l1_weighted_psi,
        l1_weighted_tpsi=l1_weighted_tpsi,
        gradient_bound=gradient_bound,
        cell_radius=cell_radius,
        continuous_upper_estimate=continuous_upper_estimate,
    )
