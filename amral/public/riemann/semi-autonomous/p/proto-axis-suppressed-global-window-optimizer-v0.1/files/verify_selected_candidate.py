from __future__ import annotations
import csv, json
from pathlib import Path
import numpy as np

from prototype import build_model, fourier_vector, block_value

ROOT = Path(__file__).resolve().parent

def main():
    model = build_model()
    with (ROOT/"data/selected_coefficients.csv").open() as f:
        coefficients = np.array([
            float(row["coefficient"]) for row in csv.DictReader(f)
        ])
    with (ROOT/"data/first_50_ordinates.csv").open() as f:
        ordinates = np.array([
            float(row["ordinate"]) for row in csv.DictReader(f)
        ])

    spectral = lambda w: coefficients @ fourier_vector(
        w,model["t"],model["basis"],model["weights"]
    )

    residuals = [abs(spectral(0.0)),abs(spectral(0.5j))]
    residuals.extend(abs(spectral(g)) for g in ordinates[:12])

    target = [
        block_value(x+1j*y,coefficients,model)
        for x in np.linspace(20.0,20.5,201)
        for y in np.linspace(-0.2,-0.1,81)
    ]
    control = [
        block_value(x+1j*y,coefficients,model)
        for x in np.linspace(10.0,60.0,401)
        for y in np.linspace(-0.45,-0.05,33)
        if not (20.0 <= x <= 20.5 and -0.2 <= y <= -0.1)
    ]

    report = {
        "constraint_residual_max":float(max(residuals)),
        "c0_normalization":float(coefficients@model["c0"]@coefficients),
        "arithmetic_quadratic_value":float(
            coefficients@model["q_arithmetic"]@coefficients
        ),
        "remaining_first_50_axis_mass":float(
            sum(abs(spectral(g))**2 for g in ordinates[12:50])
        ),
        "target_dense_max":float(max(target)),
        "target_dense_min":float(min(target)),
        "control_dense_max":float(max(control)),
        "control_dense_min":float(min(control)),
        "target_negative_on_dense_grid":bool(max(target)<0),
        "control_nonpositive_on_dense_grid":bool(max(control)<=0),
    }
    (ROOT/"outputs/recomputed_selected_report.json").write_text(
        json.dumps(report,indent=2),encoding="utf-8"
    )
    print(json.dumps(report,indent=2))
    return report

if __name__ == "__main__":
    main()
