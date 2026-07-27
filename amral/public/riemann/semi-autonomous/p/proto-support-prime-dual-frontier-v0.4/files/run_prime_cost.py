from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from frontier.primecost import (
    cost_projection,
    segmented_prime_log_histogram,
)


ROOT = Path(__file__).resolve().parent


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    benchmark_radii = (3.0, 7.0, 8.0, 8.5, 9.0, 10.25)
    projection_radii = (
        3.0,
        7.0,
        8.5,
        10.25,
        12.0,
        14.0,
        16.0,
    )
    benchmark_rows = []
    histograms = {}
    for radius in benchmark_radii:
        result = segmented_prime_log_histogram(
            radius,
            bin_width=0.01,
            segment_size=(
                2_000_000 if radius >= 10.0 else 1_000_000
            ),
        )
        benchmark_rows.append(result.to_summary())
        histograms[f"R_{str(radius).replace('.', '_')}"] = (
            result.histogram
        )
    np.savez_compressed(
        ROOT / "outputs" / "prime_histograms.npz",
        **histograms,
    )
    projections = [
        cost_projection(
            radius,
            dimension=max(22, int(round(10.0 * radius)) - 2),
        )
        for radius in projection_radii
    ]
    output = {
        "schema": "RH.SupportPrime.PrimeCost.v0.4",
        "fourier_convention": "G(w)=integral psi(t) exp(i*w*t) dt",
        "support_derivation": (
            "supp(psi) subset [-R,R] implies the correlation support "
            "is contained in [-2R,2R]. A prime-power term at "
            "m*log(p) can occur only when m*log(p)<2R, equivalently "
            "p^m<exp(2R)."
        ),
        "benchmark_rows": benchmark_rows,
        "projection_rows": projections,
        "histogram_artifact": "outputs/prime_histograms.npz",
        "compression_scope": (
            "Linear log-bin aggregation reduces matrix updates. It "
            "does not remove prime enumeration and is not yet supplied "
            "with an interval interpolation error."
        ),
        "global_rh_certificate": False,
    }
    write_json(ROOT / "outputs" / "prime_cost.json", output)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
