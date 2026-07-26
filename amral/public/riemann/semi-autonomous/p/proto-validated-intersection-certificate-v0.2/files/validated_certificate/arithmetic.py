from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
from math import exp, floor, inf, log, nextafter

import numpy as np
from mpmath import iv

from .model import HatSplineModel, cosh, lower, midpoint, sinh, tanh, upper


@dataclass(frozen=True)
class PrimePower:
    prime: int
    exponent: int
    log_value: float


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def activated_prime_powers(log_radius: float) -> list[PrimePower]:
    output: list[PrimePower] = []
    for prime in primes_upto(int(exp(log_radius)) + 2):
        exponent = 1
        while exponent * log(prime) < log_radius - 1e-13:
            output.append(PrimePower(prime, exponent, exponent * log(prime)))
            exponent += 1
    output.sort(key=lambda item: (item.log_value, item.prime, item.exponent))
    return output


def interval_pair(value) -> list[float]:
    return [lower(value), upper(value)]


def _first_interval_integral(model: HatSplineModel, step: float):
    h = midpoint(model.h)
    count = round(h / step)
    if abs(count * step - h) > 1e-13:
        raise ValueError("first_interval_step must divide the spline spacing")
    c0 = model.c0
    a2 = (model.r(1) - model.r(0)) / model.h
    a3 = (
        model.r(0) / 2 - iv.mpf(2) * model.r(1) / 3 + model.r(2) / 6
    ) / (model.h * model.h)
    total = iv.mpf(0)
    for index in range(count):
        lo, hi = index * step, (index + 1) * step
        x = iv.mpf([lo, hi])
        correlation = c0 + a2 * x * x + a3 * x * x * x
        if index == 0:
            # Rigorous elementary bounds on removable ratios at zero.
            ratio_a = iv.mpf(
                [
                    1.0 / (2.0 * __import__("math").cosh(hi)),
                    __import__("math").exp(hi / 2.0) / 2.0,
                ]
            )
            ratio_x = iv.mpf([1.0 / __import__("math").cosh(hi), 1.0])
            x2_over_sinh = x * ratio_x
        else:
            ratio_a = iv.expm1(x / 2) / sinh(x)
            x2_over_sinh = x * x / sinh(x)
        integrand = correlation * ratio_a + (a2 + a3 * x) * x2_over_sinh
        total += iv.mpf(str(step)) * integrand
    return total


def _correlation_integrand_point(model: HatSplineModel, x_value: float | str):
    x = iv.mpf(str(x_value))
    correlation = model.correlation_point(x_value)
    return (correlation * iv.exp(x / 2) - model.c0) / sinh(x)


def _midpoint_integral(model: HatSplineModel, start: float, stop: float, step: float):
    count = round((stop - start) / step)
    if abs(start + count * step - stop) > 5e-13:
        raise ValueError("Midpoint step must divide its integration range")
    total = iv.mpf(0)
    start_decimal = Decimal(str(start))
    step_decimal = Decimal(str(step))
    half = Decimal("0.5")
    for index in range(count):
        x_decimal = start_decimal + (Decimal(index) + half) * step_decimal
        total += iv.mpf(str(step)) * _correlation_integrand_point(model, str(x_decimal))
    return total


def _derivative_bound(model: HatSplineModel, lo: float, hi: float) -> float:
    c0_upper = upper(model.c0)
    derivative_energy_upper = upper(model.derivative_energy())
    d1_upper = nextafter((c0_upper * derivative_energy_upper) ** 0.5, inf)
    lo_iv, hi_iv = iv.mpf(str(lo)), iv.mpf(str(hi))
    first = iv.exp(hi_iv / 2) * (d1_upper + c0_upper / 2) / sinh(lo_iv)
    second = (
        (iv.exp(hi_iv / 2) * c0_upper + c0_upper)
        * cosh(hi_iv)
        / (sinh(lo_iv) ** 2)
    )
    return nextafter(upper(first + second), inf)


def _composite_midpoint_error(
    model: HatSplineModel,
    start: float,
    stop: float,
    step: float,
    chunk: float,
) -> float:
    position = start
    total = 0.0
    while position < stop - 1e-14:
        end = min(position + chunk, stop)
        bound = _derivative_bound(model, position, end)
        total += bound * (end - position) * step / 4.0
        position = end
    return total


def certify_arithmetic(
    model: HatSplineModel,
    first_interval_step: float,
    near_zero_midpoint_step: float,
    far_midpoint_step: float,
    near_zero_chunk: float,
    far_chunk: float,
) -> dict:
    radius = midpoint(model.support_radius)
    c0 = model.c0
    finite = iv.mpf(0)
    activations = activated_prime_powers(2 * radius)
    for item in activations:
        exact_log = item.exponent * iv.log(item.prime)
        coefficient = (
            -2
            * iv.log(item.prime)
            * iv.mpf(item.prime) ** (iv.mpf(-item.exponent) / 2)
        )
        finite += coefficient * model.correlation_interval(lower(exact_log), upper(exact_log))

    first = _first_interval_integral(model, first_interval_step)
    near = _midpoint_integral(
        model,
        midpoint(model.h),
        0.1,
        near_zero_midpoint_step,
    )
    far = _midpoint_integral(model, 0.1, 2 * radius, far_midpoint_step)
    near_error = _composite_midpoint_error(
        model,
        midpoint(model.h),
        0.1,
        near_zero_midpoint_step,
        near_zero_chunk,
    )
    far_error = _composite_midpoint_error(
        model,
        0.1,
        2 * radius,
        far_midpoint_step,
        far_chunk,
    )
    error = iv.mpf([-near_error - far_error, near_error + far_error])
    core = first + near + far + error
    constant = -(iv.log(4 * iv.pi) + iv.euler) * c0
    tail = -iv.log(tanh(model.support_radius)) * c0
    archimedean = constant - core + tail
    total = archimedean + finite
    return {
        "c0_interval": interval_pair(c0),
        "endpoint_correction_interval": interval_pair(model.endpoint_correction),
        "endpoint_residual_interval": interval_pair(model.endpoint_residual),
        "derivative_energy_interval": interval_pair(model.derivative_energy()),
        "prime_power_count": len(activations),
        "prime_powers": [asdict(item) for item in activations],
        "finite_interval": interval_pair(finite),
        "first_interval_core": interval_pair(first),
        "near_midpoint_core": interval_pair(near),
        "far_midpoint_core": interval_pair(far),
        "near_midpoint_error": near_error,
        "far_midpoint_error": far_error,
        "core_interval": interval_pair(core),
        "constant_interval": interval_pair(constant),
        "tail_interval": interval_pair(tail),
        "archimedean_interval": interval_pair(archimedean),
        "arithmetic_total_interval": interval_pair(total),
        "arithmetic_scalar_certified_positive": lower(total) > 0,
    }
