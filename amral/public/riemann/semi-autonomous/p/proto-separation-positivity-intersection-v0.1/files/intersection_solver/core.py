from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np
from scipy.linalg import eigh, null_space
from scipy.optimize import minimize

from .arithmetic import (
    PrimePowerActivation,
    build_arithmetic_matrices,
    direct_scalar_audit,
)
from .basis import (
    build_even_pair_basis,
    evaluate_basis_fourier,
    trapezoid_weights,
)


@dataclass(frozen=True)
class IntersectionConfig:
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    support_radii: tuple[float, ...]
    basis_size: int = 24
    bump_width_ratio: float = 0.18
    bump_width_cap: float = 0.12
    quadrature_points: int = 2401
    fit_nx: int = 10
    fit_ny: int = 6
    check_nx: int = 61
    check_ny: int = 31
    impose_endpoint_zero: bool = True
    impose_central_zero: bool = True
    arithmetic_margin_fraction: float = 0.20
    optimizer_starts: int = 5
    optimizer_maxiter: int = 700
    optimizer_ftol: float = 1e-10
    random_seed: int = 20260724
    prime_bound_cap: int = 2_000_000
    selected_radius: float = 3.0
    feasibility_tolerance: float = 1e-7

    def validate(self) -> None:
        if not self.x_min < self.x_max:
            raise ValueError("x_min must be smaller than x_max")
        if not self.y_min < self.y_max < 0:
            raise ValueError("Require y_min < y_max < 0")
        if not self.support_radii or any(r <= 0 for r in self.support_radii):
            raise ValueError("support_radii must be non-empty and positive")
        if self.basis_size < 6:
            raise ValueError("basis_size must be at least 6")
        if self.quadrature_points < 1001 or self.quadrature_points % 2 == 0:
            raise ValueError("quadrature_points must be odd and >= 1001")
        if not 0 < self.bump_width_ratio < 1:
            raise ValueError("bump_width_ratio must lie in (0,1)")
        if self.bump_width_cap <= 0:
            raise ValueError("bump_width_cap must be positive")
        if not 0 <= self.arithmetic_margin_fraction <= 1:
            raise ValueError("arithmetic_margin_fraction must lie in [0,1]")
        if min(self.fit_nx, self.fit_ny, self.check_nx, self.check_ny) < 2:
            raise ValueError("grid sizes must be at least 2")


@dataclass
class RadiusIntersectionResult:
    support_radius: float
    bump_width: float
    constrained_dimension: int
    arithmetic_min_eigenvalue: float
    arithmetic_max_eigenvalue: float
    required_arithmetic_margin: float
    arithmetic_value: float
    optimizer_success: bool
    optimizer_message: str
    fit_grid_max_block: float
    check_grid_max_block: float
    check_grid_min_block: float
    intersection_found_on_grid: bool
    endpoint_residual: float
    central_residual: float
    c0_norm: float
    activated_prime_powers: list[PrimePowerActivation]
    coefficients: np.ndarray
    reduced_coefficients: np.ndarray
    check_x: np.ndarray
    check_y: np.ndarray
    check_G: np.ndarray
    check_block: np.ndarray
    t: np.ndarray
    psi: np.ndarray
    matrix_archimedean: np.ndarray
    matrix_finite: np.ndarray
    matrix_total: np.ndarray
    direct_audit: dict[str, float]
    matrix_audit: dict[str, float]

    def summary_dict(self) -> dict[str, Any]:
        return {
            "support_radius": self.support_radius,
            "bump_width": self.bump_width,
            "constrained_dimension": self.constrained_dimension,
            "arithmetic_min_eigenvalue": self.arithmetic_min_eigenvalue,
            "arithmetic_max_eigenvalue": self.arithmetic_max_eigenvalue,
            "required_arithmetic_margin": self.required_arithmetic_margin,
            "arithmetic_value": self.arithmetic_value,
            "optimizer_success": self.optimizer_success,
            "optimizer_message": self.optimizer_message,
            "fit_grid_max_block": self.fit_grid_max_block,
            "check_grid_max_block": self.check_grid_max_block,
            "check_grid_min_block": self.check_grid_min_block,
            "intersection_found_on_grid": self.intersection_found_on_grid,
            "endpoint_residual": self.endpoint_residual,
            "central_residual": self.central_residual,
            "c0_norm": self.c0_norm,
            "activated_count": len(self.activated_prime_powers),
            "activated_prime_powers": [asdict(item) for item in self.activated_prime_powers],
            "coefficients": self.coefficients.tolist(),
            "reduced_coefficients": self.reduced_coefficients.tolist(),
            "direct_audit": self.direct_audit,
            "matrix_audit": self.matrix_audit,
            "warning": (
                "Floating-point finite-grid prototype only. A negative check grid is not a "
                "continuous-region interval certificate, and matrix positivity is not an interval PSD proof."
            ),
        }


def _grid_points(config: IntersectionConfig, check: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    nx = config.check_nx if check else config.fit_nx
    ny = config.check_ny if check else config.fit_ny
    xs = np.linspace(config.x_min, config.x_max, nx)
    ys = np.linspace(config.y_min, config.y_max, ny)
    points = (xs[:, None] + 1j * ys[None, :]).reshape(-1)
    return xs, ys, points


def _whitening_map(c0_reduced: np.ndarray) -> np.ndarray:
    values, vectors = eigh(0.5 * (c0_reduced + c0_reduced.T))
    threshold = max(1e-12, 1e-10 * float(np.max(values)))
    keep = values > threshold
    if not np.any(keep):
        raise RuntimeError("C0 metric is numerically singular after constraints")
    return vectors[:, keep] @ np.diag(1.0 / np.sqrt(values[keep]))


def _initial_phase_fit(transform: np.ndarray) -> np.ndarray:
    system = np.vstack((transform.real, transform.imag))
    target = np.concatenate((np.zeros(len(transform)), np.ones(len(transform))))
    coefficient, *_ = np.linalg.lstsq(system, target, rcond=1e-11)
    norm = float(np.linalg.norm(coefficient))
    if norm < 1e-14:
        coefficient = np.ones(transform.shape[1])
        norm = float(np.linalg.norm(coefficient))
    return coefficient / norm


def _orbit_matrices(transform: np.ndarray) -> np.ndarray:
    return np.asarray([2.0 * np.real(np.outer(row, row)) for row in transform])


def _solve_minimax(
    matrices: np.ndarray,
    arithmetic: np.ndarray,
    required_margin: float,
    initial: np.ndarray,
    config: IntersectionConfig,
) -> Any:
    dimension = arithmetic.shape[0]

    def objective(x: np.ndarray) -> float:
        return float(x[-1])

    def objective_jac(x: np.ndarray) -> np.ndarray:
        gradient = np.zeros_like(x)
        gradient[-1] = 1.0
        return gradient

    def sphere(x: np.ndarray) -> float:
        return float(x[:-1] @ x[:-1] - 1.0)

    def sphere_jac(x: np.ndarray) -> np.ndarray:
        return np.concatenate((2.0 * x[:-1], [0.0]))

    def arithmetic_constraint(x: np.ndarray) -> float:
        return float(x[:-1] @ arithmetic @ x[:-1] - required_margin)

    def arithmetic_jac(x: np.ndarray) -> np.ndarray:
        return np.concatenate((2.0 * arithmetic @ x[:-1], [0.0]))

    def regional_constraints(x: np.ndarray) -> np.ndarray:
        values = np.einsum("i,kij,j->k", x[:-1], matrices, x[:-1])
        return x[-1] - values

    def regional_jac(x: np.ndarray) -> np.ndarray:
        grad_y = -2.0 * np.einsum("kij,j->ki", matrices, x[:-1])
        return np.column_stack((grad_y, np.ones(len(matrices))))

    constraints = [
        {"type": "eq", "fun": sphere, "jac": sphere_jac},
        {"type": "ineq", "fun": arithmetic_constraint, "jac": arithmetic_jac},
        {"type": "ineq", "fun": regional_constraints, "jac": regional_jac},
    ]

    rng = np.random.default_rng(config.random_seed)
    starts = [initial]
    mean_matrix = np.mean(matrices, axis=0)
    _, mean_vectors = eigh(0.5 * (mean_matrix + mean_matrix.T))
    starts.append(mean_vectors[:, 0])
    while len(starts) < config.optimizer_starts:
        trial = rng.normal(size=dimension)
        trial /= np.linalg.norm(trial)
        starts.append(trial)

    best = None
    for start in starts:
        start = np.asarray(start, dtype=float)
        start /= np.linalg.norm(start)
        initial_max = float(np.max(np.einsum("i,kij,j->k", start, matrices, start)))
        x0 = np.concatenate((start, [initial_max + 1e-7]))
        result = minimize(
            objective,
            x0,
            jac=objective_jac,
            constraints=constraints,
            method="SLSQP",
            options={
                "ftol": config.optimizer_ftol,
                "maxiter": config.optimizer_maxiter,
                "disp": False,
            },
        )
        if best is None or result.fun < best.fun:
            best = result
    return best


def solve_radius(config: IntersectionConfig, support_radius: float) -> RadiusIntersectionResult:
    bump_width = min(config.bump_width_cap, config.bump_width_ratio * support_radius)
    t = np.linspace(-support_radius, support_radius, config.quadrature_points)
    weights = trapezoid_weights(t)
    basis, _ = build_even_pair_basis(
        t, support_radius, config.basis_size, bump_width, weights
    )

    arch, finite, total, c0, activations = build_arithmetic_matrices(
        basis, t, support_radius, config.prime_bound_cap
    )

    endpoint_row = evaluate_basis_fourier(
        basis, t, weights, np.asarray([0.5j], dtype=complex)
    )[0].real
    central_row = evaluate_basis_fourier(
        basis, t, weights, np.asarray([0.0j], dtype=complex)
    )[0].real
    rows: list[np.ndarray] = []
    if config.impose_endpoint_zero:
        rows.append(endpoint_row)
    if config.impose_central_zero:
        rows.append(central_row)
    constraint_kernel = null_space(np.asarray(rows)) if rows else np.eye(config.basis_size)
    if constraint_kernel.shape[1] == 0:
        raise RuntimeError("Constraints leave no nonzero subspace")

    whitening = _whitening_map(constraint_kernel.T @ c0 @ constraint_kernel)
    shared_map = constraint_kernel @ whitening
    arithmetic = shared_map.T @ total @ shared_map
    arithmetic = 0.5 * (arithmetic + arithmetic.T)
    arithmetic_eigenvalues = np.linalg.eigvalsh(arithmetic)
    arithmetic_min = float(arithmetic_eigenvalues[0])
    arithmetic_max = float(arithmetic_eigenvalues[-1])
    required_margin = (
        config.arithmetic_margin_fraction * arithmetic_min
        if arithmetic_min > 0.0
        else 0.0
    )

    _, _, fit_points = _grid_points(config, check=False)
    fit_transform_full = evaluate_basis_fourier(basis, t, weights, fit_points)
    fit_transform = fit_transform_full @ shared_map
    fit_matrices = _orbit_matrices(fit_transform)
    initial = _initial_phase_fit(fit_transform)

    optimizer = _solve_minimax(
        fit_matrices, arithmetic, required_margin, initial, config
    )
    reduced = np.asarray(optimizer.x[:-1], dtype=float)
    reduced /= np.linalg.norm(reduced)
    coefficients = shared_map @ reduced

    fit_values = np.einsum("i,kij,j->k", reduced, fit_matrices, reduced)
    fit_grid_max = float(np.max(fit_values))

    check_x, check_y, check_points = _grid_points(config, check=True)
    check_transform = evaluate_basis_fourier(
        basis, t, weights, check_points, batch_size=128
    )
    check_g = check_transform @ coefficients
    check_block_flat = 2.0 * np.real(check_g**2)
    check_block = check_block_flat.reshape(config.check_nx, config.check_ny)
    check_g_grid = check_g.reshape(config.check_nx, config.check_ny)
    check_max = float(np.max(check_block_flat))
    check_min = float(np.min(check_block_flat))

    arithmetic_value = float(coefficients @ total @ coefficients)
    c0_norm = float(coefficients @ c0 @ coefficients)
    endpoint_residual = float(abs(endpoint_row @ coefficients))
    central_residual = float(abs(central_row @ coefficients))
    psi = coefficients @ basis

    direct = direct_scalar_audit(
        coefficients, basis, t, support_radius, activations
    )
    matrix_audit = {
        "c0_matrix": c0_norm,
        "archimedean_matrix": float(coefficients @ arch @ coefficients),
        "finite_matrix": float(coefficients @ finite @ coefficients),
        "total_matrix": arithmetic_value,
        "c0_abs_difference": abs(c0_norm - direct["c0_direct"]),
        "archimedean_abs_difference": abs(
            float(coefficients @ arch @ coefficients) - direct["archimedean_direct"]
        ),
        "finite_abs_difference": abs(
            float(coefficients @ finite @ coefficients) - direct["finite_direct"]
        ),
        "total_abs_difference": abs(arithmetic_value - direct["total_direct"]),
    }

    feasible = bool(
        check_max < 0.0
        and arithmetic_value >= required_margin - config.feasibility_tolerance
        and endpoint_residual < 1e-8
        and (not config.impose_central_zero or central_residual < 1e-8)
    )

    return RadiusIntersectionResult(
        support_radius=float(support_radius),
        bump_width=float(bump_width),
        constrained_dimension=shared_map.shape[1],
        arithmetic_min_eigenvalue=arithmetic_min,
        arithmetic_max_eigenvalue=arithmetic_max,
        required_arithmetic_margin=float(required_margin),
        arithmetic_value=arithmetic_value,
        optimizer_success=bool(optimizer.success),
        optimizer_message=str(optimizer.message),
        fit_grid_max_block=fit_grid_max,
        check_grid_max_block=check_max,
        check_grid_min_block=check_min,
        intersection_found_on_grid=feasible,
        endpoint_residual=endpoint_residual,
        central_residual=central_residual,
        c0_norm=c0_norm,
        activated_prime_powers=activations,
        coefficients=coefficients,
        reduced_coefficients=reduced,
        check_x=check_x,
        check_y=check_y,
        check_G=check_g_grid,
        check_block=check_block,
        t=t,
        psi=psi,
        matrix_archimedean=arch,
        matrix_finite=finite,
        matrix_total=total,
        direct_audit=direct,
        matrix_audit=matrix_audit,
    )


def run_scan(config: IntersectionConfig) -> list[RadiusIntersectionResult]:
    config.validate()
    return [solve_radius(config, radius) for radius in config.support_radii]
