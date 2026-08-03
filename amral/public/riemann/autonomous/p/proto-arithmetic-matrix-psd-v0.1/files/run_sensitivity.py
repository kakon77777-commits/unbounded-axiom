from __future__ import annotations

import argparse
import csv
from pathlib import Path

from arithmetic_psd import ArithmeticScanConfig, build_radius_result


def main() -> None:
    parser = argparse.ArgumentParser(description="Quadrature sensitivity scan")
    parser.add_argument("--output", default="outputs/quadrature_sensitivity.csv")
    args = parser.parse_args()

    radii = (0.4, 0.7, 1.0)
    quadrature_sizes = (1601, 2401, 3601, 4801)
    rows: list[list[object]] = []
    for radius in radii:
        for quadrature_points in quadrature_sizes:
            config = ArithmeticScanConfig(
                support_radii=(radius,),
                basis_size=14,
                quadrature_points=quadrature_points,
                frequency_max=30.0,
                frequency_points=3001,
                selected_radius=radius,
            )
            result = build_radius_result(config, radius)
            rows.append(
                [
                    radius,
                    quadrature_points,
                    result.min_eigen_archimedean,
                    result.min_eigen_total,
                    len(result.activated_prime_powers),
                ]
            )

    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "support_radius",
                "quadrature_points",
                "min_eigen_archimedean",
                "min_eigen_total",
                "activated_count",
            ]
        )
        writer.writerows(rows)
    print(destination)


if __name__ == "__main__":
    main()
