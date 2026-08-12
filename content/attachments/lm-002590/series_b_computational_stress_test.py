import itertools
import math
import numpy as np

TOL = 1e-10

def opnorm(M):
    return np.linalg.norm(M, 2)

def rot(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)

def run():
    report = {}

    # T1 — local order defect
    A = np.array([[1., 1.], [0., 1.]])
    B = np.array([[1., 0.], [1., 1.]])
    x = np.array([0.7, -1.2])
    ABx = A @ (B @ x)
    BAx = B @ (A @ x)
    delta = np.linalg.norm(ABx - BAx)
    report["T1_noncommutative_defect"] = delta > TOL

    # T2 — Lipschitz propagation bound + 2000 random cases
    S = np.array([[2.0, 0.3], [-0.1, 0.5]])
    lhs = np.linalg.norm(S @ ABx - S @ BAx)
    rhs = opnorm(S) * delta
    ok = lhs <= rhs + TOL

    rng = np.random.default_rng(20260810)
    violations = 0
    for _ in range(2000):
        Ar = rng.normal(size=(3,3))
        Br = rng.normal(size=(3,3))
        Sr = rng.normal(size=(3,3))
        xr = rng.normal(size=3)
        d = np.linalg.norm(Ar @ (Br @ xr) - Br @ (Ar @ xr))
        L = np.linalg.norm(Sr @ (Ar @ (Br @ xr)) - Sr @ (Br @ (Ar @ xr)))
        R = opnorm(Sr) * d
        if L > R + TOL:
            violations += 1
    report["T2_lipschitz_bound"] = ok and violations == 0

    # T3 — Z2 cycle obstruction
    def coboundary_z2(b):
        b1,b2,b3 = b
        return ((b2-b1)%2, (b3-b2)%2, (b1-b3)%2)

    all_cob = {coboundary_z2(b) for b in itertools.product([0,1], repeat=3)}
    report["T3_H1_cycle_obstruction"] = (1,1,1) not in all_cob and (1,1,0) in all_cob

    # T4 — nonexistence vs inaccessibility
    satisfying = []
    for a,b,c in itertools.product([0,1], repeat=3):
        if ((a^b)==0) and ((b^c)==0) and ((c^a)==1):
            satisfying.append((a,b,c))

    G = [(0,0),(0,1),(1,0),(1,1)]
    pre = {}
    for g in G:
        pre.setdefault(g[0], []).append(g)
    noninjective = any(len(v) > 1 for v in pre.values())
    report["T4_nonexistence_vs_inaccessibility"] = len(satisfying)==0 and noninjective

    # T5 — group-commutator holonomy
    K = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    report["T5_nontrivial_holonomy"] = opnorm(K - np.eye(2)) > TOL

    # T6 — nontrivial state holonomy, invariant survives
    H = rot(math.pi/2)
    v = np.array([3.,4.])
    q0 = v @ v
    q1 = (H @ v) @ (H @ v)
    report["T6_invariant_survives_holonomy"] = (
        opnorm(H-np.eye(2)) > TOL and abs(q1-q0) < TOL
    )

    # T7 — exact observer covariance / relative holonomy
    F = np.array([[2.0,0.2],[0.0,0.5]])
    Fi = np.linalg.inv(F)
    TO = rot(0.37)
    TP = F @ TO @ Fi
    d_cov = opnorm(F @ TO - TP @ F)

    HO = rot(0.71)
    HP = F @ HO @ Fi
    R = F @ HO @ Fi @ np.linalg.inv(HP)
    report["T7_observer_covariance"] = d_cov < TOL and opnorm(R-np.eye(2)) < TOL

    # T8 — coarse graining hides holonomy
    Fproj = np.array([[1.0,0.0]])
    Hhidden = np.array([[1.0,0.0],[0.0,-1.0]])
    report["T8_hidden_holonomy"] = (
        opnorm(Hhidden-np.eye(2)) > TOL
        and np.linalg.norm(Fproj @ Hhidden - Fproj) < TOL
    )

    # T9 — pairwise maps can exist while triple coherence fails
    F12 = np.eye(2)
    F23 = np.eye(2)
    F31 = rot(math.pi/3)
    Kbad = F31 @ F23 @ F12

    phi1 = rot(0.1)
    phi2 = np.array([[1.2,0.1],[0.0,0.8]])
    phi3 = rot(-0.4) @ np.array([[0.9,0.0],[0.2,1.1]])
    F12c = phi2 @ np.linalg.inv(phi1)
    F23c = phi3 @ np.linalg.inv(phi2)
    F31c = phi1 @ np.linalg.inv(phi3)
    Kgood = F31c @ F23c @ F12c

    report["T9_network_coherence"] = (
        opnorm(Kbad-np.eye(2)) > TOL
        and opnorm(Kgood-np.eye(2)) < TOL
    )

    # T10 — observer-covariant conserved quantity
    Fq = np.array([[1.7,0.2],[0.1,0.8]])
    Fqi = np.linalg.inv(Fq)
    TqO = rot(0.52)
    TqP = Fq @ TqO @ Fqi

    def QO(v):
        return float(v @ v)
    def QP(w):
        z = Fqi @ w
        return float(z @ z)

    v = np.array([1.3,-0.7])
    w = Fq @ v
    report["T10_observer_covariant_conservation"] = max(
        abs(QO(TqO@v)-QO(v)),
        abs(QP(TqP@w)-QP(w)),
        abs(QP(Fq@v)-QO(v)),
    ) < TOL

    # T11 — strict conservation fails but balance law succeeds
    Q0, Q1, Phi = 10.0, 7.0, -3.0
    report["T11_balance_not_strict"] = (
        abs(Q1-Q0) > TOL
        and abs((Q1-Q0)-Phi) < TOL
    )

    passed = sum(report.values())
    for name, ok in report.items():
        print(f"{name}: {'PASS' if ok else 'FAIL'}")
    print(f"\nPassed {passed}/{len(report)} checks.")
    return report

if __name__ == "__main__":
    run()
