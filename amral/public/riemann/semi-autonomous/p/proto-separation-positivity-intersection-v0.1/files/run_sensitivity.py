from __future__ import annotations

import csv
from dataclasses import replace
from pathlib import Path

from intersection_solver import IntersectionConfig, solve_radius


BASE = IntersectionConfig(
    x_min=8.0,
    x_max=8.5,
    y_min=-0.2,
    y_max=-0.1,
    support_radii=(3.0,),
    basis_size=24,
    bump_width_ratio=0.18,
    bump_width_cap=0.12,
    quadrature_points=2401,
    fit_nx=10,
    fit_ny=6,
    check_nx=61,
    check_ny=31,
    impose_endpoint_zero=True,
    impose_central_zero=True,
    arithmetic_margin_fraction=0.2,
    optimizer_starts=5,
    optimizer_maxiter=700,
    optimizer_ftol=1e-10,
    random_seed=20260724,
    prime_bound_cap=2_000_000,
    selected_radius=3.0,
)


def main() -> None:
    output = Path('outputs')
    output.mkdir(exist_ok=True)
    rows = []
    for quadrature_points in (1601, 2401, 3201):
        config = replace(BASE, quadrature_points=quadrature_points)
        result = solve_radius(config, 3.0)
        rows.append(
            {
                'quadrature_points': quadrature_points,
                'arithmetic_min_eigenvalue': result.arithmetic_min_eigenvalue,
                'arithmetic_value': result.arithmetic_value,
                'check_grid_max_block': result.check_grid_max_block,
                'check_grid_min_block': result.check_grid_min_block,
                'endpoint_residual': result.endpoint_residual,
                'central_residual': result.central_residual,
                'intersection_found_on_grid': result.intersection_found_on_grid,
                'optimizer_success': result.optimizer_success,
            }
        )
    with (output / 'quadrature_sensitivity.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
