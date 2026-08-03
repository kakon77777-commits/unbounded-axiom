from __future__ import annotations

from dataclasses import asdict, dataclass
from math import exp, log
from typing import Any

import numpy as np
from scipy.linalg import null_space
from scipy.signal import correlate
from scipy.special import digamma

from .basis import (
    build_even_pair_basis,
    evaluate_basis_fourier,
    shifted_correlation_matrix,
    trapezoid_weights,
)


@dataclass(frozen=True)
class ArithmeticScanConfig:
    support_radii: tuple[float, ...]
    basis_size: int = 14
    bump_width_ratio: float = 0.22
    bump_width_cap: float = 0.08
    quadrature_points: int = 2401
    frequency_max: float = 70.0
    frequency_points: int = 14001
    impose_endpoint_zero: bool = True
    impose_central_zero: bool = True
    psd_tolerance: float = 1e-8
    prime_bound_cap: int = 2_000_000
    selected_radius: float = 0.4

    def validate(self) -> None:
        if not self.support_radii:
            raise ValueError("support_radii must not be empty")
        if any(radius <= 0 for radius in self.support_radii):
            raise ValueError("support radii must be positive")
        if self.basis_size < 4:
            raise ValueError("basis_size must be at least 4")
        if self.quadrature_points < 1001 or self.quadrature_points % 2 == 0:
            raise ValueError("quadrature_points must be an odd integer >= 1001")
        if self.frequency_points < 2001 or self.frequency_points % 2 == 0:
            raise ValueError("frequency_points must be an odd integer >= 2001")
        if self.frequency_max <= 0:
            raise ValueError("frequency_max must be positive")
        if not 0 < self.bump_width_ratio < 1:
            raise ValueError("bump_width_ratio must lie in (0, 1)")
        if self.bump_width_cap <= 0:
            raise ValueError("bump_width_cap must be positive")


@dataclass(frozen=True)
class PrimePowerActivation:
    prime: int
    exponent: int
    log_value: float
    coefficient: float


@dataclass
class RadiusResult:
    support_radius: float
    convolution_log_radius: float
    bump_width: float
    constraint_rank: int
    constrained_dimension: int
    activated_prime_powers: list[PrimePowerActivation]
    min_eigen_archimedean: float
    max_eigen_archimedean: float
    min_eigen_finite: float
    max_eigen_finite: float
    min_eigen_total: float
    max_eigen_total: float
    numerical_psd: bool
    archimedean_spectral_crosscheck_norm: float
    endpoint_constraint_residual: float
    central_constraint_residual: float
    most_negative_vector_reduced: np.ndarray
    most_negative_vector_full: np.ndarray
    matrix_archimedean: np.ndarray
    matrix_finite: np.ndarray
    matrix_total: np.ndarray
    matrix_total_reduced: np.ndarray

    def summary_dict(self) -> dict[str, Any]:
        return {
            "support_radius": self.support_radius,
            "convolution_log_radius": self.convolution_log_radius,
            "bump_width": self.bump_width,
            "constraint_rank": self.constraint_rank,
            "constrained_dimension": self.constrained_dimension,
            "activated_prime_powers": [asdict(item) for item in self.activated_prime_powers],
            "activated_count": len(self.activated_prime_powers),
            "min_eigen_archimedean": self.min_eigen_archimedean,
            "max_eigen_archimedean": self.max_eigen_archimedean,
            "min_eigen_finite": self.min_eigen_finite,
            "max_eigen_finite": self.max_eigen_finite,
            "min_eigen_total": self.min_eigen_total,
            "max_eigen_total": self.max_eigen_total,
            "numerical_psd": self.numerical_psd,
            "archimedean_spectral_crosscheck_norm": self.archimedean_spectral_crosscheck_norm,
            "endpoint_constraint_residual": self.endpoint_constraint_residual,
            "central_constraint_residual": self.central_constraint_residual,
            "most_negative_vector_reduced": self.most_negative_vector_reduced.tolist(),
            "most_negative_vector_full": self.most_negative_vector_full.tolist(),
            "warning": (
                "Floating-point/quadrature research prototype only. PSD status is not an interval proof, "
                "and the archimedean integral is frequency-truncated."
            ),
        }


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def activated_prime_powers(log_radius: float, cap: int) -> list[PrimePowerActivation]:
    """Prime powers with m log p < log_radius, using the open-support convention."""
    if log_radius <= log(2):
        return []
    natural_bound = int(exp(log_radius)) + 1
    if natural_bound > cap:
        raise ValueError(
            f"Prime bound exp({log_radius:.3f})≈{natural_bound} exceeds cap={cap}. "
            "Reduce support or increase prime_bound_cap explicitly."
        )
    activations: list[PrimePowerActivation] = []
    for prime in primes_upto(natural_bound):
        exponent = 1
        while exponent * log(prime) < log_radius - 1e-12:
            value = exponent * log(prime)
            coefficient = -2.0 * log(prime) * prime ** (-0.5 * exponent)
            activations.append(
                PrimePowerActivation(
                    prime=prime,
                    exponent=exponent,
                    log_value=value,
                    coefficient=coefficient,
                )
            )
            exponent += 1
    activations.sort(key=lambda item: (item.log_value, item.prime, item.exponent))
    return activations


def archimedean_multiplier(frequency: np.ndarray) -> np.ndarray:
    """2 theta'(t) = Re digamma(1/4 + i t/2) - log(pi)."""
    return np.real(digamma(0.25 + 0.5j * frequency)) - np.log(np.pi)


def correlation_grid(
    basis: np.ndarray,
    t: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """All symmetric cross-correlations on the uniform lag grid."""
    dt = float(t[1] - t[0])
    size = basis.shape[1]
    lags = np.arange(-(size - 1), size, dtype=float) * dt
    matrices = np.empty((len(lags), basis.shape[0], basis.shape[0]), dtype=float)
    for j in range(basis.shape[0]):
        for k in range(basis.shape[0]):
            matrices[:, j, k] = correlate(
                basis[j], basis[k], mode="full", method="fft"
            ) * dt
    matrices = 0.5 * (matrices + np.swapaxes(matrices, 1, 2))
    return lags, matrices


def interpolate_correlation_matrix(
    lags: np.ndarray,
    correlations: np.ndarray,
    shift: float,
) -> np.ndarray:
    if shift < lags[0] or shift > lags[-1]:
        return np.zeros(correlations.shape[1:], dtype=float)
    index = int(np.searchsorted(lags, shift))
    if index == 0:
        return correlations[0].copy()
    if index >= len(lags):
        return correlations[-1].copy()
    left = index - 1
    alpha = (shift - lags[left]) / (lags[index] - lags[left])
    matrix = (1.0 - alpha) * correlations[left] + alpha * correlations[index]
    return 0.5 * (matrix + matrix.T)


def archimedean_matrix_time_domain(
    lags: np.ndarray,
    correlations: np.ndarray,
    support_radius: float,
) -> np.ndarray:
    """Compact-support log-coordinate form of the archimedean explicit term."""
    positive = lags >= -1e-14
    x = lags[positive]
    corr = correlations[positive]
    c0 = corr[0]

    kernel = np.empty_like(x)
    kernel[0] = 0.0
    kernel[1:] = np.exp(x[1:] / 2.0) / (np.exp(x[1:]) - np.exp(-x[1:]))

    integrand = np.empty_like(corr)
    integrand[0] = 0.5 * c0
    integrand[1:] = (
        2.0
        * (corr[1:] - np.exp(-x[1:, None, None] / 2.0) * c0)
        * kernel[1:, None, None]
    )
    weights = np.empty_like(x)
    dx = np.diff(x)
    weights[0] = dx[0] / 2.0
    weights[-1] = dx[-1] / 2.0
    weights[1:-1] = (dx[:-1] + dx[1:]) / 2.0
    core = np.tensordot(weights, integrand, axes=(0, 0))

    euler_gamma = 0.5772156649015328606
    tail = -np.log(np.tanh(support_radius)) * c0
    matrix = -(np.log(4.0 * np.pi) + euler_gamma) * c0 - core + tail
    return 0.5 * (matrix + matrix.T)

def _projected_spectrum(matrix: np.ndarray, kernel: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    reduced = kernel.T @ matrix @ kernel
    reduced = 0.5 * (reduced + reduced.T)
    values, vectors = np.linalg.eigh(reduced)
    return values, vectors


def build_radius_result(config: ArithmeticScanConfig, support_radius: float) -> RadiusResult:
    bump_width = min(config.bump_width_cap, config.bump_width_ratio * support_radius)
    t = np.linspace(-support_radius, support_radius, config.quadrature_points)
    t_weights = trapezoid_weights(t)
    basis, _ = build_even_pair_basis(
        t=t,
        support_radius=support_radius,
        basis_size=config.basis_size,
        bump_width=bump_width,
        weights=t_weights,
    )

    lags, correlations = correlation_grid(basis, t)
    matrix_arch = archimedean_matrix_time_domain(
        lags=lags,
        correlations=correlations,
        support_radius=support_radius,
    )

    # Spectral digamma evaluation is retained only as an empirical cross-check.
    frequency = np.linspace(
        -config.frequency_max,
        config.frequency_max,
        config.frequency_points,
    )
    frequency_weights = trapezoid_weights(frequency)
    transform = evaluate_basis_fourier(
        basis=basis,
        t=t,
        weights=t_weights,
        points=frequency.astype(complex),
        batch_size=192,
    )
    multiplier = archimedean_multiplier(frequency)
    weighted = frequency_weights * multiplier / (2.0 * np.pi)
    matrix_arch_spectral = (
        transform.conj().T @ (transform * weighted[:, None])
    ).real
    matrix_arch_spectral = 0.5 * (matrix_arch_spectral + matrix_arch_spectral.T)
    spectral_crosscheck_norm = float(
        np.linalg.norm(matrix_arch - matrix_arch_spectral, ord=2)
    )

    log_radius = 2.0 * support_radius
    activations = activated_prime_powers(log_radius, config.prime_bound_cap)
    matrix_finite = np.zeros_like(matrix_arch)
    for activation in activations:
        correlation = interpolate_correlation_matrix(
            lags=lags,
            correlations=correlations,
            shift=activation.log_value,
        )
        matrix_finite += activation.coefficient * correlation
    matrix_finite = 0.5 * (matrix_finite + matrix_finite.T)
    matrix_total = matrix_arch + matrix_finite
    matrix_total = 0.5 * (matrix_total + matrix_total.T)

    constraint_rows: list[np.ndarray] = []
    endpoint_row = evaluate_basis_fourier(
        basis, t, t_weights, np.asarray([0.5j], dtype=complex)
    )[0]
    central_row = evaluate_basis_fourier(
        basis, t, t_weights, np.asarray([0.0j], dtype=complex)
    )[0]
    if config.impose_endpoint_zero:
        constraint_rows.append(endpoint_row.real)
    if config.impose_central_zero:
        constraint_rows.append(central_row.real)

    if constraint_rows:
        constraints = np.asarray(constraint_rows)
        kernel = null_space(constraints)
        constraint_rank = int(np.linalg.matrix_rank(constraints))
    else:
        constraints = np.zeros((0, config.basis_size))
        kernel = np.eye(config.basis_size)
        constraint_rank = 0
    if kernel.shape[1] == 0:
        raise RuntimeError("Constraints leave no nonzero test-function subspace")

    eig_arch, _ = _projected_spectrum(matrix_arch, kernel)
    eig_fin, _ = _projected_spectrum(matrix_finite, kernel)
    eig_total, vec_total = _projected_spectrum(matrix_total, kernel)
    min_index = int(np.argmin(eig_total))
    negative_reduced = vec_total[:, min_index]
    negative_full = kernel @ negative_reduced

    endpoint_residual = float(abs(endpoint_row @ negative_full))
    central_residual = float(abs(central_row @ negative_full))
    reduced_total = kernel.T @ matrix_total @ kernel
    reduced_total = 0.5 * (reduced_total + reduced_total.T)

    return RadiusResult(
        support_radius=float(support_radius),
        convolution_log_radius=log_radius,
        bump_width=bump_width,
        constraint_rank=constraint_rank,
        constrained_dimension=kernel.shape[1],
        activated_prime_powers=activations,
        min_eigen_archimedean=float(eig_arch[0]),
        max_eigen_archimedean=float(eig_arch[-1]),
        min_eigen_finite=float(eig_fin[0]),
        max_eigen_finite=float(eig_fin[-1]),
        min_eigen_total=float(eig_total[0]),
        max_eigen_total=float(eig_total[-1]),
        numerical_psd=bool(eig_total[0] >= -config.psd_tolerance),
        archimedean_spectral_crosscheck_norm=spectral_crosscheck_norm,
        endpoint_constraint_residual=endpoint_residual,
        central_constraint_residual=central_residual,
        most_negative_vector_reduced=negative_reduced,
        most_negative_vector_full=negative_full,
        matrix_archimedean=matrix_arch,
        matrix_finite=matrix_finite,
        matrix_total=matrix_total,
        matrix_total_reduced=reduced_total,
    )


def run_scan(config: ArithmeticScanConfig) -> list[RadiusResult]:
    config.validate()
    return [build_radius_result(config, radius) for radius in config.support_radii]
