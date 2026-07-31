#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys

import weil_interval_core as base
import mixed_order_core as mixed

sys.set_int_max_str_digits(0)


def fq(obj):
    return F(int(obj["num"]), int(obj["den"]))


def iv(obj):
    return base.IV(fq(obj["lower"]), fq(obj["upper"]))


def prime_power_base(n: int) -> int | None:
    for p in range(2, n + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        v = p
        while v < n:
            v *= p
        if v == n:
            return p
    return None


def ldlt(A):
    n = len(A)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        L[i][i] = F(1)
        pivot = A[i][i] - sum(L[i][k] * L[i][k] * pivots[k] for k in range(i))
        if pivot <= 0:
            return False, pivots + [pivot]
        pivots.append(pivot)
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * L[i][k] * pivots[k] for k in range(i))) / pivot
    return True, pivots


def grid_center(x: base.IV, grid: int) -> F:
    m = x.midpoint()
    q = m.numerator * grid // m.denominator
    left, right = F(q, grid), F(q + 1, grid)
    return left if abs(m - left) <= abs(right - m) else right


def interval_quadratic(A, c):
    total = base.IV.point(0)
    for i in range(len(c)):
        for j in range(len(c)):
            total += A[i][j].scale(F(c[i] * c[j]))
    return total


def exact_quadratic(A, c):
    return sum((F(c[i] * c[j]) * A[i][j] for i in range(len(c)) for j in range(len(c))), F(0))


def verify_block(Aiv, G, delta, claimed_eps, grid):
    n = len(Aiv)
    C = [[grid_center(Aiv[i][j], grid) for j in range(n)] for i in range(n)]
    eps = max(
        sum(max(abs(C[i][j]-Aiv[i][j].lo), abs(Aiv[i][j].hi-C[i][j])) for j in range(n))
        for i in range(n)
    )
    if eps != claimed_eps:
        raise AssertionError("row radius mismatch")
    test = [[C[i][j]-delta*G[i][j]-(eps if i==j else F(0)) for j in range(n)] for i in range(n)]
    ok,piv=ldlt(test)
    if not ok:
        raise AssertionError("LDLT positivity failed")
    return piv


def main():
    root = Path(__file__).resolve().parent
    obj = json.loads((root / "mixed_10x10_interval.json").read_text(encoding="utf-8"))
    if obj["schema"] != "RH-W-12-mixed-order-dictionary-v0.1":
        raise AssertionError("schema")
    if obj["status"] != "CERTIFIED_POSITIVE_ON_THIS_MIXED_SUBSPACE":
        raise AssertionError("status")

    b = obj["basis"]
    h, d = fq(b["h"]), fq(b["spacing"])
    N, dim = int(b["per_channel_dimension"]), int(b["total_dimension"])
    degrees = tuple(map(int, b["basis_degrees"]))
    if degrees != (1,3) or dim != 2*N:
        raise AssertionError("basis layout")
    corr = {(1,1):3,(1,3):5,(3,3):7}

    matrix = [[iv(x) for x in row] for row in obj["matrix"]]
    gram = [[fq(x) for x in row] for row in obj["gram"]]
    if len(matrix) != dim or any(len(r)!=dim for r in matrix):
        raise AssertionError("matrix dimension")
    for i in range(dim):
        for j in range(dim):
            if matrix[i][j] != matrix[j][i]:
                raise AssertionError("matrix symmetry")
            if gram[i][j] != gram[j][i]:
                raise AssertionError("gram symmetry")

    # Rebuild exact Gram and lag references.
    for ca,a in enumerate(degrees):
        for cb,bdeg in enumerate(degrees):
            key=f"{min(a,bdeg)}x{max(a,bdeg)}"
            r=corr[(min(a,bdeg),max(a,bdeg))]
            for i in range(N):
                for j in range(N):
                    I,J=ca*N+i,cb*N+j
                    expected=mixed.f_value(r,h,F(i-j)*d,F(0))
                    if gram[I][J] != expected:
                        raise AssertionError("gram reconstruction")
                    lag=abs(i-j)
                    if matrix[I][J] != iv(obj["lag_entries"][key][str(lag)]):
                        raise AssertionError("lag reconstruction")

    gok,gp=ldlt(gram)
    if not gok:
        raise AssertionError("Gram is not positive definite")

    # Prime-power completeness and support exclusion.
    exclusion=int(obj["support"]["exclusion_n"])
    pp={n:prime_power_base(n) for n in range(2,exclusion)}
    pp={n:p for n,p in pp.items() if p is not None}
    claimed={int(n):int(p) for n,p in obj["prime_powers"].items()}
    if pp != claimed:
        raise AssertionError("prime-power enumeration")
    max_radius=F(N-1)*d+F(4)*h
    if base.log_rational_iv(F(exclusion),210).lo <= max_radius:
        raise AssertionError("exclusion threshold")

    # Activation graph independently reconstructed from interval spline samples.
    logs={n:base.log_rational_iv(F(n),210) for n in pp}
    for pair,r in corr.items():
        key=f"{pair[0]}x{pair[1]}"
        for lag in range(N):
            center=F(lag)*d
            active=[]
            for n,x in logs.items():
                plus=mixed.f_interval(r,h,center,x)
                minus=mixed.f_interval(r,h,center,-x)
                if not (plus.lo==plus.hi==0 and minus.lo==minus.hi==0):
                    active.append(n)
            if active != obj["activation_graph"][key][str(lag)]:
                raise AssertionError(f"activation mismatch {key} lag {lag}")

    grid=int(obj["certificate"]["grid_denominator"])
    delta=fq(obj["certificate"]["delta"])
    eps=fq(obj["certificate"]["row_radius"])
    piv=verify_block(matrix,gram,delta,eps,grid)

    # Isolated blocks.
    for name,start in (("m1_only",0),("m3_only",N)):
        cert=obj["isolated_channel_certificates"][name]
        A=[[matrix[start+i][start+j] for j in range(N)] for i in range(N)]
        G=[[gram[start+i][start+j] for j in range(N)] for i in range(N)]
        verify_block(A,G,fq(cert["delta"]),fq(cert["row_radius"]),grid)

    # Rational upper witness and its exact decomposition.
    wobj=obj["mixed_upper_witness"]
    c=list(map(int,wobj["integer_vector"]))
    if len(c)!=dim or all(x==0 for x in c):
        raise AssertionError("witness")
    q=interval_quadratic(matrix,c)
    g=exact_quadratic(gram,c)
    if q.lo != iv(wobj["quadratic_interval"]).lo or q.hi != iv(wobj["quadratic_interval"]).hi:
        # Builder coarsens outward, so only containment is required.
        claimed_iv=iv(wobj["quadratic_interval"])
        if not (claimed_iv.lo <= q.lo and q.hi <= claimed_iv.hi):
            raise AssertionError("witness interval")
    if g != fq(wobj["gram_exact"]):
        raise AssertionError("witness Gram")
    upper=fq(wobj["upper_ratio"])
    if q.hi >= upper*g:
        raise AssertionError("mixed upper witness failed")

    # Recompute and sign-check exact channel decomposition.
    w1,w3=c[:N],c[N:]
    A11=[[matrix[i][j] for j in range(N)] for i in range(N)]
    A33=[[matrix[N+i][N+j] for j in range(N)] for i in range(N)]
    q11=interval_quadratic(A11,w1)
    q33=interval_quadratic(A33,w3)
    q13=base.IV.point(0)
    for i in range(N):
        for j in range(N):
            q13 += matrix[i][N+j].scale(F(2*w1[i]*w3[j]))
    comps=wobj["channel_components"]
    for name,actual in (("m1_self",q11),("cross_twice",q13),("m3_self",q33)):
        claimed=iv(comps[name])
        if not (claimed.lo <= actual.lo and actual.hi <= claimed.hi):
            raise AssertionError(f"channel component {name}")
    if not (q11.lo>0 and q33.lo>0 and q13.hi<0 and q.lo>0):
        raise AssertionError("cross-cancellation signs")

    # Prime-power witness components are independently reconstructed from lag audits.
    for n in pp:
        P=[[base.IV.point(0) for _ in range(dim)] for _ in range(dim)]
        for ca,a in enumerate(degrees):
            for cb,bdeg in enumerate(degrees):
                key=f"{min(a,bdeg)}x{max(a,bdeg)}"
                for i in range(N):
                    for j in range(N):
                        P[ca*N+i][cb*N+j]=iv(obj["lag_audits"][key][str(abs(i-j))]["prime_blocks"][str(n)])
        actual=interval_quadratic(P,c)
        claimed=iv(wobj["prime_power_components"][str(n)])
        if not (claimed.lo <= actual.lo and actual.hi <= claimed.hi):
            raise AssertionError(f"prime component {n}")

    # Exact spectral separation encoded by the certificates.
    if not (delta == F(1,2000) and upper == F(1,1000)):
        raise AssertionError("mixed bracket constants")
    if fq(obj["isolated_channel_certificates"]["m3_only"]["delta"]) != F(1,250):
        raise AssertionError("m3 bound")
    if fq(obj["isolated_channel_certificates"]["m1_only"]["delta"]) != F(1,20):
        raise AssertionError("m1 bound")

    lines=[
        "schema=OK",
        "matrix_symmetry=OK",
        "gram_reconstruction=OK",
        f"gram_ldlt_pivots_positive={len(gp)}",
        f"prime_power_enumeration={list(pp)}",
        "activation_graph=OK",
        f"mixed_ldlt_pivots_positive={len(piv)}",
        "mixed_lower_bound=lambda_min>1/2000",
        "mixed_upper_witness=lambda_min<1/1000",
        "cross_channel_cancellation=EXACT_SIGN_CERTIFIED",
        "prime_witness_components=OK",
        "m3_isolated_lower_bound=lambda_min>1/250",
        "m1_isolated_lower_bound=lambda_min>1/20",
        "status=EXACT_MIXED_DICTIONARY_CERTIFICATE_OK",
        "RH_CLAIM=False",
    ]
    text="\n".join(lines)+"\n"
    (root/"EXACT_VERIFY.txt").write_text(text,encoding="utf-8")
    print(text,end="")

if __name__ == "__main__":
    main()
