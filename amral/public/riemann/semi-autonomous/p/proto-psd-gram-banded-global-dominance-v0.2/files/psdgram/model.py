from __future__ import annotations

import math

import numpy as np
from scipy.linalg import eigh, null_space


def paired_bump_basis(
    t: np.ndarray,
    radius: float = 3.0,
    count: int = 24,
    width_factor: float = 1.2,
    power: int = 3,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return a real, even, compactly supported polynomial-bump basis."""
    t = np.asarray(t, dtype=float)
    spacing = radius / (count - 0.5)
    width = width_factor * spacing
    centers = np.linspace(0.0, max(0.0, radius - width), count)

    def bump(x: np.ndarray) -> np.ndarray:
        u = x / width
        return np.where(np.abs(u) < 1.0, (1.0 - u * u) ** power, 0.0)

    columns = []
    for index, center in enumerate(centers):
        columns.append(
            bump(t) if index == 0 else bump(t - center) + bump(t + center)
        )
    return np.stack(columns, axis=1), centers, width


def paired_bump_derivative(
    t: np.ndarray,
    radius: float = 3.0,
    count: int = 24,
    width_factor: float = 1.2,
    power: int = 3,
) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    spacing = radius / (count - 0.5)
    width = width_factor * spacing
    centers = np.linspace(0.0, max(0.0, radius - width), count)

    def derivative(x: np.ndarray) -> np.ndarray:
        u = x / width
        return np.where(
            np.abs(u) < 1.0,
            power * (1.0 - u * u) ** (power - 1) * (-2.0 * u) / width,
            0.0,
        )

    columns = []
    for index, center in enumerate(centers):
        columns.append(
            derivative(t)
            if index == 0
            else derivative(t - center) + derivative(t + center)
        )
    return np.stack(columns, axis=1)


def paired_bump_second_derivative(
    t: np.ndarray,
    radius: float = 3.0,
    count: int = 24,
    width_factor: float = 1.2,
    power: int = 3,
) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    spacing = radius / (count - 0.5)
    width = width_factor * spacing
    centers = np.linspace(0.0, max(0.0, radius - width), count)

    def second_derivative(x: np.ndarray) -> np.ndarray:
        u = x / width
        inside = np.abs(u) < 1.0
        value = np.zeros_like(u)
        value[inside] = (
            -2.0
            * power
            / (width * width)
            * (1.0 - u[inside] * u[inside]) ** (power - 2)
            * (1.0 - (2.0 * power - 1.0) * u[inside] * u[inside])
        )
        return value

    columns = []
    for index, center in enumerate(centers):
        columns.append(
            second_derivative(t)
            if index == 0
            else second_derivative(t - center)
            + second_derivative(t + center)
        )
    return np.stack(columns, axis=1)


def trapezoid_weights(size: int, step: float) -> np.ndarray:
    weights = np.full(size, step, dtype=float)
    weights[0] = weights[-1] = step / 2.0
    return weights


def fourier_vector(
    w: complex,
    t: np.ndarray,
    basis: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    return np.sum(
        weights[:, None] * basis * np.exp(1j * complex(w) * t)[:, None],
        axis=0,
    )


def fourier_matrix(
    points: np.ndarray,
    model: dict[str, object],
    batch_size: int = 256,
) -> np.ndarray:
    points = np.asarray(points, dtype=complex).reshape(-1)
    t = np.asarray(model["t"])
    weighted_basis = np.asarray(model["basis"]) * np.asarray(model["weights"])[:, None]
    output = np.empty((len(points), weighted_basis.shape[1]), dtype=complex)
    for start in range(0, len(points), batch_size):
        stop = min(start + batch_size, len(points))
        output[start:stop] = np.exp(
            1j * np.outer(points[start:stop], t)
        ) @ weighted_basis
    return output


def block_values(
    points: np.ndarray,
    coefficients: np.ndarray,
    model: dict[str, object],
) -> np.ndarray:
    transform = fourier_matrix(points, model) @ coefficients
    return 2.0 * np.real(transform * transform)


def block_matrices(
    points: np.ndarray,
    model: dict[str, object],
    coordinate_map: np.ndarray,
) -> np.ndarray:
    transform = fourier_matrix(points, model) @ coordinate_map
    return np.asarray([2.0 * np.real(np.outer(row, row)) for row in transform])


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def build_model(
    radius: float = 3.0,
    count: int = 24,
    step: float = 0.01,
    width_factor: float = 1.2,
) -> dict[str, object]:
    """Rebuild the floating arithmetic quadratic form used by the prior node."""
    t = np.arange(-radius, radius + step / 2.0, step)
    basis, centers, width = paired_bump_basis(
        t, radius, count, width_factor
    )
    derivative = paired_bump_derivative(
        t, radius, count, width_factor
    )
    second_derivative = paired_bump_second_derivative(
        t, radius, count, width_factor
    )
    weights = trapezoid_weights(len(t), step)

    c0 = basis.T @ (weights[:, None] * basis)
    derivative_matrix = derivative.T @ (weights[:, None] * derivative)
    g0 = fourier_vector(0.0, t, basis, weights).real
    endpoint = fourier_vector(0.5j, t, basis, weights).real

    core = np.zeros((count, count))
    shifts = np.arange(0.0, 2.0 * radius + step / 2.0, step)
    for index, x in enumerate(shifts):
        shifted, _, _ = paired_bump_basis(
            t - x, radius, count, width_factor
        )
        correlation = basis.T @ (weights[:, None] * shifted)
        correlation = (correlation + correlation.T) / 2.0
        if index == 0:
            integrand = c0 / 2.0
        else:
            integrand = (
                math.exp(x / 2.0) * correlation - c0
            ) / math.sinh(x)
        qweight = step / 2.0 if index in (0, len(shifts) - 1) else step
        core += qweight * integrand

    euler_gamma = 0.5772156649015328606
    q_infinity = (
        -(math.log(4.0 * math.pi) + euler_gamma) * c0
        - core
        - math.log(math.tanh(radius)) * c0
    )

    q_finite = np.zeros_like(q_infinity)
    prime_powers: list[tuple[int, int, float]] = []
    for prime in primes_upto(int(math.exp(2.0 * radius)) + 2):
        exponent = 1
        while exponent * math.log(prime) < 2.0 * radius - 1e-12:
            x = exponent * math.log(prime)
            shifted, _, _ = paired_bump_basis(
                t - x, radius, count, width_factor
            )
            correlation = basis.T @ (weights[:, None] * shifted)
            correlation = (correlation + correlation.T) / 2.0
            coefficient = -2.0 * math.log(prime) * prime ** (-exponent / 2.0)
            q_finite += coefficient * correlation
            prime_powers.append((prime, exponent, x))
            exponent += 1

    return {
        "radius": radius,
        "count": count,
        "step": step,
        "t": t,
        "basis": basis,
        "basis_derivative": derivative,
        "basis_second_derivative": second_derivative,
        "weights": weights,
        "c0": c0,
        "derivative": derivative_matrix,
        "g0_constraint": g0,
        "endpoint_constraint": endpoint,
        "q_infinity": q_infinity,
        "q_finite": q_finite,
        "q_arithmetic": q_infinity + q_finite,
        "prime_powers": prime_powers,
        "centers": centers,
        "width": width,
    }


def constrained_whitener(model: dict[str, object]) -> np.ndarray:
    """Impose only structural zeros at 0 and i/2, never known zeta zeros."""
    rows = np.vstack(
        [
            np.asarray(model["g0_constraint"]),
            np.asarray(model["endpoint_constraint"]),
        ]
    )
    kernel = null_space(rows, rcond=1e-11)
    gram = kernel.T @ np.asarray(model["c0"]) @ kernel
    values, vectors = eigh(gram)
    keep = values > 1e-9
    return kernel @ vectors[:, keep] @ np.diag(1.0 / np.sqrt(values[keep]))


def spectral_energy_matrix(
    model: dict[str, object],
    coordinate_map: np.ndarray,
    start: float = 14.0,
    stop: float = 145.0,
    step: float = 0.1,
) -> tuple[np.ndarray, list[dict[str, float]]]:
    """Continuous-axis proxy, independent of individual zero ordinates."""
    bands = [(14.0, 35.0), (35.0, 70.0), (70.0, 145.0)]
    pieces: list[np.ndarray] = []
    summaries: list[dict[str, float]] = []
    for left, right in bands:
        left = max(left, start)
        right = min(right, stop)
        if left >= right:
            continue
        grid = np.arange(left, right + step / 2.0, step)
        weights = trapezoid_weights(len(grid), step)
        density = 1.0 + np.log1p(grid) / (2.0 * math.pi)
        transform = fourier_matrix(grid.astype(complex), model) @ coordinate_map
        transform = transform.real
        matrix = transform.T @ ((weights * density)[:, None] * transform)
        matrix = 0.5 * (matrix + matrix.T)
        pieces.append(matrix)
        summaries.append(
            {
                "start": float(left),
                "stop": float(right),
                "step": float(step),
            }
        )
    return sum(pieces, np.zeros_like(pieces[0])), summaries


def function_diagnostics(
    coefficients: np.ndarray,
    model: dict[str, object],
) -> dict[str, float]:
    t = np.asarray(model["t"])
    weights = np.asarray(model["weights"])
    psi = np.asarray(model["basis"]) @ coefficients
    psi_second = np.asarray(model["basis_second_derivative"]) @ coefficients
    a0 = float(np.sum(weights * np.abs(psi)))
    a1 = float(np.sum(weights * np.abs(t * psi)))
    derivative_variation = float(np.sum(weights * np.abs(psi_second)))
    return {
        "l1": a0,
        "first_moment_l1": a1,
        "derivative_total_variation_proxy": derivative_variation,
    }
