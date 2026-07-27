from __future__ import annotations

import math
import time
from dataclasses import dataclass
from typing import Any

import numpy as np


def strict_prime_power_cutoff(radius: float) -> int:
    value = math.exp(2.0 * radius)
    return int(math.ceil(value) - 1)


def pnt_prime_count_proxy(limit: float) -> float:
    if limit <= math.e:
        return 0.0
    return limit / math.log(limit)


def cost_projection(
    radius: float,
    dimension: int,
    log_bin_width: float = 0.01,
) -> dict[str, float | int]:
    cutoff = math.exp(2.0 * radius)
    prime_proxy = pnt_prime_count_proxy(cutoff)
    bins = int(math.ceil(2.0 * radius / log_bin_width)) + 1
    return {
        "radius": radius,
        "strict_integer_cutoff": strict_prime_power_cutoff(radius),
        "cutoff_float": cutoff,
        "pnt_prime_count_proxy": prime_proxy,
        "log_histogram_bins": bins,
        "prime_to_bin_compression_proxy": prime_proxy / bins,
        "dimension": dimension,
        "legacy_dense_matrix_update_proxy": (
            prime_proxy * dimension * dimension
        ),
        "histogram_matrix_update_proxy": bins * dimension * dimension,
    }


def _base_primes(limit: int) -> np.ndarray:
    if limit < 2:
        return np.empty(0, dtype=np.int64)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, int(math.isqrt(limit)) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = False
    return np.flatnonzero(sieve).astype(np.int64)


@dataclass
class PrimeHistogramResult:
    radius: float
    cutoff: int
    prime_count: int
    prime_power_term_count: int
    bin_width: float
    bin_count: int
    coefficient_sum: float
    elapsed_seconds: float
    segment_size: int
    segment_boolean_bytes: int
    histogram: np.ndarray

    def to_summary(self) -> dict[str, Any]:
        return {
            "radius": self.radius,
            "cutoff": self.cutoff,
            "prime_count": self.prime_count,
            "prime_power_term_count": self.prime_power_term_count,
            "bin_width": self.bin_width,
            "bin_count": self.bin_count,
            "coefficient_sum": self.coefficient_sum,
            "elapsed_seconds": self.elapsed_seconds,
            "segment_size": self.segment_size,
            "segment_boolean_bytes": self.segment_boolean_bytes,
        }


def segmented_prime_log_histogram(
    radius: float,
    bin_width: float = 0.01,
    segment_size: int = 1_000_000,
) -> PrimeHistogramResult:
    """Stream prime powers into a linearly interpolated log histogram."""
    start_time = time.perf_counter()
    cutoff = strict_prime_power_cutoff(radius)
    maximum_log = 2.0 * radius
    bin_count = int(math.ceil(maximum_log / bin_width)) + 1
    histogram = np.zeros(bin_count, dtype=float)
    base = _base_primes(math.isqrt(cutoff) + 1)
    prime_count = 0
    term_count = 0

    def deposit(log_values: np.ndarray, values: np.ndarray) -> None:
        nonlocal term_count
        positions = log_values / bin_width
        left = np.floor(positions).astype(np.int64)
        fraction = positions - left
        left = np.minimum(left, bin_count - 1)
        right = np.minimum(left + 1, bin_count - 1)
        np.add.at(histogram, left, values * (1.0 - fraction))
        np.add.at(histogram, right, values * fraction)
        term_count += len(values)

    for low in range(2, cutoff + 1, segment_size):
        high = min(cutoff + 1, low + segment_size)
        segment = np.ones(high - low, dtype=bool)
        for prime in base:
            prime_int = int(prime)
            first = max(
                prime_int * prime_int,
                ((low + prime_int - 1) // prime_int) * prime_int,
            )
            if first >= high:
                continue
            segment[first - low : high - low : prime_int] = False
        primes = np.flatnonzero(segment).astype(np.int64) + low
        primes = primes[primes >= 2]
        if not len(primes):
            continue
        prime_count += len(primes)
        logs = np.log(primes.astype(float))
        exponent = 1
        while True:
            selected = exponent * logs < maximum_log - 1e-12
            if not np.any(selected):
                break
            selected_logs = exponent * logs[selected]
            selected_primes = primes[selected].astype(float)
            coefficients = (
                -2.0
                * logs[selected]
                * selected_primes ** (-0.5 * exponent)
            )
            deposit(selected_logs, coefficients)
            exponent += 1

    return PrimeHistogramResult(
        radius=radius,
        cutoff=cutoff,
        prime_count=int(prime_count),
        prime_power_term_count=int(term_count),
        bin_width=bin_width,
        bin_count=bin_count,
        coefficient_sum=float(np.sum(histogram)),
        elapsed_seconds=float(time.perf_counter() - start_time),
        segment_size=segment_size,
        segment_boolean_bytes=segment_size,
        histogram=histogram,
    )
