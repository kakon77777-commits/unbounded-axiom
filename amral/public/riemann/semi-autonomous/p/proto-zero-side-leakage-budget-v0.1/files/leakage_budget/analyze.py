
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path
import mpmath as mp
from .model import HatSpline

def s_bound(T: float) -> float:
    # Trudgian (2012): |S(T)| <= 0.111 log T + 0.275 log log T + 2.450, T >= e.
    return 0.111*math.log(T) + 0.275*math.log(math.log(T)) + 2.450

def theta(T):
    z = mp.mpf("0.25") + 0.5j*mp.mpf(T)
    return mp.im(mp.loggamma(z)) - mp.mpf(T)*mp.log(mp.pi)/2

def shell_zero_majorant(n: int) -> float:
    # N(n+1)-N(n) <= Δtheta/pi + |S(n+1)|+|S(n)|.
    delta = float((theta(n+1)-theta(n))/mp.pi)
    return max(0.0, delta + s_bound(n+1) + s_bound(n))

def run(nodes: Path, out: Path, zero_count: int, tail_start: int, tail_stop: int):
    mp.mp.dps = 70
    model = HatSpline.from_csv(nodes, dps=70)
    rows=[]
    cumulative=mp.mpf("0")
    for k in range(1, zero_count+1):
        rho=mp.zetazero(k)
        gamma=mp.im(rho)
        val=model.G(gamma)
        mass=abs(val)**2
        cumulative += mass
        rows.append({
            "index":k, "gamma":float(gamma), "G_real":float(mp.re(val)),
            "G_imag":float(mp.im(val)), "axis_mass":float(mass),
            "cumulative_axis_mass":float(cumulative)
        })
    with (out/"known_axis_zeros.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

    tv=float(model.derivative_total_variation())
    shell_rows=[]
    tail=0.0
    for n in range(tail_start,tail_stop):
        count=shell_zero_majorant(n)
        env=tv/(n*n)
        contribution=count*env*env
        tail += contribution
        shell_rows.append({
            "shell_start":n, "zero_count_majorant":count,
            "G_abs_envelope":env, "axis_mass_majorant":contribution
        })
    # Integral continuation: count per unit <= a log t + b loglog t + c, use a deliberately
    # conservative 1 + 2*S-bound + theta increment upper bounded by 1 + log(t)/(2π)+2*S.
    T=float(tail_stop)
    def density(t):
        return 1.0 + math.log(t)/(2*math.pi) + 2*s_bound(t+1)
    # numerical upper-oriented continuation with factor 1.05 safety
    cont=float(mp.quad(lambda u: density(float(u))*tv*tv/(u**4), [T, mp.inf]))*1.05
    tail_total=tail+cont
    with (out/"tail_shell_majorant.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=shell_rows[0].keys()); w.writeheader(); w.writerows(shell_rows)

    target_margin=2.2416560599e-6
    l1=float(model.l1_weighted(0.5))
    per_unknown=2*l1*l1
    summary={
        "target_negative_margin":target_margin,
        "known_axis_zero_count":zero_count,
        "known_axis_mass_sum":float(cumulative),
        "first_axis_zero_mass":rows[0]["axis_mass"],
        "first_zero_to_target_ratio":rows[0]["axis_mass"]/target_margin,
        "known_axis_to_target_ratio":float(cumulative)/target_margin,
        "derivative_total_variation":tv,
        "tail_start":tail_start,
        "tail_stop":tail_stop,
        "finite_shell_tail_majorant":tail,
        "continuation_tail_majorant":cont,
        "total_tail_majorant":tail_total,
        "weighted_L1_strip_half":l1,
        "worst_case_per_unknown_off_axis_orbit":per_unknown,
        "target_tolerable_unknown_orbits":target_margin/per_unknown,
        "conclusion":{
            "current_test_can_dominate_first_axis_zero": target_margin > rows[0]["axis_mass"],
            "current_test_can_dominate_known_axis_prefix": target_margin > float(cumulative),
            "single_target_strategy_viable_without_axis_suppression": False
        },
        "status_note":"Known-zero values are exploratory numerical evaluations. Tail bound uses an explicit S(T) bound plus a conservative continuation profile; it is a prototype budget, not a formal proof object."
    }
    (out/"leakage_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    return summary

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--nodes",default="data/corrected_nodes.csv")
    p.add_argument("--output",default="outputs")
    p.add_argument("--zeros",type=int,default=50)
    p.add_argument("--tail-start",type=int,default=60)
    p.add_argument("--tail-stop",type=int,default=500)
    a=p.parse_args()
    out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
    s=run(Path(a.nodes),out,a.zeros,a.tail_start,a.tail_stop)
    print(json.dumps(s,indent=2))
if __name__=="__main__": main()
