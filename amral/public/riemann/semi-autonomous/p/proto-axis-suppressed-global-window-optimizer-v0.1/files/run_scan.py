from __future__ import annotations
import csv
from pathlib import Path
import numpy as np

from prototype import (
    build_model, constrained_whitener, block_matrix, minimax_target
)

ROOT = Path(__file__).resolve().parent

def main():
    model = build_model()
    with (ROOT/"data/first_50_ordinates.csv").open() as handle:
        ordinates = [
            float(row["ordinate"]) for row in csv.DictReader(handle)
        ]

    target_points = [
        x+1j*y
        for x in np.linspace(20.0,20.5,7)
        for y in np.linspace(-0.2,-0.1,5)
    ]
    rows = []

    for q in [0,1,2,3,4,5,6,8,10,12,15]:
        coordinate_map = constrained_whitener(model,ordinates[:q])
        arithmetic = (
            coordinate_map.T @ model["q_arithmetic"] @ coordinate_map
        )
        eigenvalues = np.linalg.eigvalsh(arithmetic)
        maximum = float(eigenvalues[-1])
        row = {
            "q":q,
            "dimension":coordinate_map.shape[1],
            "positive_arithmetic_dimension":int(np.sum(eigenvalues>1e-6)),
            "max_arithmetic_eigenvalue":maximum,
        }
        if maximum > 0:
            floor = min(0.001,0.05*maximum)
            matrices = np.asarray([
                block_matrix(point,model,coordinate_map)
                for point in target_points
            ])
            result = minimax_target(
                model,coordinate_map,matrices,floor
            )
            row["target_grid_max"] = float(result.x[-1])
            row["optimizer_success"] = bool(result.success)
        rows.append(row)

    fields = sorted(set().union(*(row.keys() for row in rows)))
    with (ROOT/"outputs/recomputed_scan.csv").open(
        "w",newline="",encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle,fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
