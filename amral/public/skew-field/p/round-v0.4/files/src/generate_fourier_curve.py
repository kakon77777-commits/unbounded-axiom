"""Generate a normalized positive-curvature Fourier curve."""
from pathlib import Path
import argparse
import json
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid

def generate(coefficients, samples=8001):
    coeff = np.asarray(coefficients, dtype=float)
    modes = len(coeff) // 2
    s = np.linspace(0.0, 1.0, samples)
    g = np.zeros_like(s)

    for mode in range(1, modes + 1):
        a = coeff[2 * mode - 2]
        b = coeff[2 * mode - 1]
        g += a * np.cos(2 * math.pi * mode * s)
        g += b * np.sin(2 * math.pi * mode * s)

    raw = np.exp(g - np.max(g))
    kappa = math.pi * raw / np.trapezoid(raw, s)
    theta = np.concatenate([[0.0], cumulative_trapezoid(kappa, s)])
    theta *= math.pi / theta[-1]

    x = np.concatenate([[0.0], cumulative_trapezoid(np.cos(theta), s)])
    y = np.concatenate([[0.0], cumulative_trapezoid(np.sin(theta), s)])
    radial_dot = x * np.cos(theta) + y * np.sin(theta)
    return np.column_stack([s, x, y, kappa, theta, radial_dot])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode-key", default="M10")
    parser.add_argument("--output", default="data/curves/fourier_replayed.csv")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    summary = json.loads((root / "data/round04_summary.json").read_text())
    coefficients = summary["fourier_function_space"]["mode_results"][args.mode_key]["coefficients"]
    curve = generate(coefficients)
    output = root / args.output
    np.savetxt(
        output,
        curve,
        delimiter=",",
        header="s,x,y,kappa,theta,radial_dot",
        comments="",
    )
    print(output)
