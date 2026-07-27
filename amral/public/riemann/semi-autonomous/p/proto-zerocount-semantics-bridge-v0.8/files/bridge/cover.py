from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Patch:
    patch_id: str
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    guard_dx: float = 0.0
    guard_dy: float = 0.0

    def points(self, nx: int, ny: int) -> np.ndarray:
        x = np.linspace(self.x_min, self.x_max, nx)
        y = np.linspace(self.y_min, self.y_max, ny)
        return (x[:, None] + 1j * y[None, :]).reshape(-1)
