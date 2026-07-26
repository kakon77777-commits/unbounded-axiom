
from __future__ import annotations
import csv
from dataclasses import dataclass
from pathlib import Path
import mpmath as mp

@dataclass
class HatSpline:
    t: list[mp.mpf]
    y: list[mp.mpf]
    h: mp.mpf

    @classmethod
    def from_csv(cls, path: str | Path, dps: int = 70):
        mp.mp.dps = dps
        rows = list(csv.DictReader(Path(path).open(encoding="utf-8")))
        t = [mp.mpf(r["t"]) for r in rows]
        y = [mp.mpf(r["value_midpoint"]) for r in rows]
        return cls(t=t, y=y, h=t[1]-t[0])

    def G(self, w):
        w = mp.mpc(w)
        z = w*self.h/2
        phi = self.h if abs(z) == 0 else self.h*(mp.sin(z)/z)**2
        return phi*mp.fsum(v*mp.e**(1j*w*x) for x, v in zip(self.t, self.y))

    def l1_weighted(self, y_abs: float = 0.5):
        # Exact-enough high precision quadrature of the piecewise-linear absolute envelope.
        total = mp.mpf("0")
        for i in range(len(self.t)-1):
            a,b = self.t[i],self.t[i+1]
            ya,yb = self.y[i],self.y[i+1]
            # Conservative endpoint maximum for |linear segment| exp(y_abs |t|).
            m = max(abs(ya)*mp.e**(y_abs*abs(a)), abs(yb)*mp.e**(y_abs*abs(b)))
            total += (b-a)*m
        return total

    def derivative_total_variation(self):
        slopes = [(self.y[i+1]-self.y[i])/self.h for i in range(len(self.y)-1)]
        tv = abs(slopes[0]) + abs(slopes[-1])
        tv += mp.fsum(abs(slopes[i+1]-slopes[i]) for i in range(len(slopes)-1))
        return tv

    def tail_envelope(self, x):
        x = mp.mpf(x)
        return self.derivative_total_variation()/(x*x)
