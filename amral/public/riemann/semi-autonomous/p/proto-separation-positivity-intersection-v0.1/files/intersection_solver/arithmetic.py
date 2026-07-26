from __future__ import annotations

from dataclasses import dataclass
from math import exp, log

import numpy as np
from scipy.signal import correlate


@dataclass(frozen=True)
class PrimePowerActivation:
    prime: int
    exponent: int
    log_value: float
    coefficient: float


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def activated_prime_powers(log_radius: float, cap: int) -> list[PrimePowerActivation]:
    """Return prime powers satisfying m log(p) < log_radius."""
    if log_radius <= log(2):
        return []
    natural_bound = int(exp(log_radius)) + 1
    if natural_bound > cap:
        raise ValueError(
            f"Prime bound exp({log_radius:.3f})≈{natural_bound} exceeds cap={cap}."
        )
    activations: list[PrimePowerActivation] = []
    for prime in primes_upto(natural_bound):
        exponent = 1
        while exponent * log(prime) < log_radius - 1e-12:
            activations.append(
                PrimePowerActivation(
                    prime=prime,
                    exponent=exponent,
                    log_value=exponent * log(prime),
                    coefficient=-2.0 * log(prime) * prime ** (-0.5 * exponent),
                )
            )
            exponent += 1
    activations.sort(key=lambda item: (item.log_value, item.prime, item.exponent))
    return activations


def correlation_grid(
    basis: np.ndarray,
    t: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Symmetrized cross-correlation matrices on a uniform lag grid."""
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
    """Floating-point compact-support log-coordinate archimedean matrix."""
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
    dx = np.diff(x)
    weights = np.empty_like(x)
    weights[0] = dx[0] / 2.0
    weights[-1] = dx[-1] / 2.0
    weights[1:-1] = (dx[:-1] + dx[1:]) / 2.0
    core = np.tensordot(weights, integrand, axes=(0, 0))

    euler_gamma = 0.5772156649015328606
    tail = -np.log(np.tanh(support_radius)) * c0
    matrix = -(np.log(4.0 * np.pi) + euler_gamma) * c0 - core + tail
    return 0.5 * (matrix + matrix.T)


def build_arithmetic_matrices(
    basis: np.ndarray,
    t: np.ndarray,
    support_radius: float,
    prime_bound_cap: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, list[PrimePowerActivation]]:
    lags, correlations = correlation_grid(basis, t)
    archimedean = archimedean_matrix_time_domain(
        lags, correlations, support_radius
    )
    finite = np.zeros_like(archimedean)
    activations = activated_prime_powers(2.0 * support_radius, prime_bound_cap)
    for activation in activations:
        finite += activation.coefficient * interpolate_correlation_matrix(
            lags, correlations, activation.log_value
        )
    finite = 0.5 * (finite + finite.T)
    total = 0.5 * (archimedean + finite + (archimedean + finite).T)
    c0 = interpolate_correlation_matrix(lags, correlations, 0.0)
    return archimedean, finite, total, c0, activations


def direct_scalar_audit(
    coefficients: np.ndarray,
    basis: np.ndarray,
    t: np.ndarray,
    support_radius: float,
    activations: list[PrimePowerActivation],
) -> dict[str, float]:
    """Recompute the same quadratic form from the combined test function."""
    psi = coefficients @ basis
    dt = float(t[1] - t[0])
    scalar_corr = correlate(psi, psi, mode="full", method="fft") * dt
    lags = np.arange(-(len(t) - 1), len(t), dtype=float) * dt

    def interp(shift: float) -> float:
        return float(np.interp(shift, lags, scalar_corr, left=0.0, right=0.0))

    c0 = interp(0.0)
    positive = lags >= -1e-14
    x = lags[positive]
    corr = scalar_corr[positive]
    kernel = np.empty_like(x)
    kernel[0] = 0.0
    kernel[1:] = np.exp(x[1:] / 2.0) / (np.exp(x[1:]) - np.exp(-x[1:]))
    integrand = np.empty_like(x)
    integrand[0] = 0.5 * c0
    integrand[1:] = 2.0 * (corr[1:] - np.exp(-x[1:] / 2.0) * c0) * kernel[1:]
    core = float(np.trapezoid(integrand, x))
    euler_gamma = 0.5772156649015328606
    tail = -np.log(np.tanh(support_radius)) * c0
    arch = -(np.log(4.0 * np.pi) + euler_gamma) * c0 - core + tail
    finite = sum(item.coefficient * interp(item.log_value) for item in activations)
    return {
        "c0_direct": c0,
        "archimedean_direct": float(arch),
        "finite_direct": float(finite),
        "total_direct": float(arch + finite),
    }
