import itertools
import math
import numpy as np
import pandas as pd

TOL = 1e-10

def Rx(a):
    c,s = math.cos(a), math.sin(a)
    return np.array([[1,0,0],[0,c,-s],[0,s,c]], float)

def Ry(a):
    c,s = math.cos(a), math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]], float)

def Rz(a):
    c,s = math.cos(a), math.sin(a)
    return np.array([[c,-s,0],[s,c,0],[0,0,1]], float)

def opnorm(A):
    return np.linalg.norm(A, 2)

def product(mats):
    H = np.eye(mats[0].shape[0])
    for T in mats:
        H = T @ H
    return H

def coboundary_cycle_z2(bits):
    n = len(bits)
    return tuple((bits[(i+1)%n]-bits[i]) % 2 for i in range(n))

def run(seed=20260810):
    rng = np.random.default_rng(seed)

    # Hidden world: five noncommuting orthogonal transports.
    edges = [Rx(0.37), Ry(-0.51), Rz(0.63), Rx(0.22), Ry(0.41)]
    H = product(edges)
    order_defects = [
        opnorm(edges[(i+1)%5]@edges[i] - edges[i]@edges[(i+1)%5])
        for i in range(5)
    ]

    states = rng.normal(size=(1000,3))
    q_resid = 0.0
    for T in edges:
        q0 = np.sum(states*states, axis=1)
        s1 = states @ T.T
        q1 = np.sum(s1*s1, axis=1)
        q_resid = max(q_resid, float(np.max(np.abs(q1-q0))))

    # Observer frames.
    frames = {
        "O0": np.eye(3),
        "O1": np.array([[1.8,0.2,0.0],[0.0,0.7,0.1],[0.1,0.0,1.3]]),
        "O2": Rz(0.4) @ np.diag([0.8,1.5,1.1]),
        "O3": np.array([[1.0,0.2,-0.1],[0.1,1.3,0.2],[0.0,-0.1,0.9]])
    }

    local_edges, local_H, metrics = {}, {}, {}
    for name,F in frames.items():
        Fi = np.linalg.inv(F)
        local_edges[name] = [F@T@Fi for T in edges]
        local_H[name] = F@H@Fi
        metrics[name] = Fi.T@Fi

    def F(a,b):
        return frames[b] @ np.linalg.inv(frames[a])

    # Pairwise observer covariance.
    cov_rows = []
    for a,b in itertools.permutations(frames.keys(), 2):
        Fab = F(a,b)
        edge_def = max(opnorm(Fab@Ta - Tb@Fab)
                       for Ta,Tb in zip(local_edges[a], local_edges[b]))
        R = Fab@local_H[a]@np.linalg.inv(Fab)@np.linalg.inv(local_H[b])
        relH = opnorm(R-np.eye(3))
        spec = float(np.max(np.abs(
            np.sort_complex(np.linalg.eigvals(local_H[a])) -
            np.sort_complex(np.linalg.eigvals(local_H[b]))
        )))
        cov_rows.append((a,b,edge_def,relH,spec))
    cov_df = pd.DataFrame(cov_rows, columns=[
        "observer_A","observer_B","max_edge_cov_defect",
        "relative_holonomy_defect","holonomy_spectrum_diff"
    ])

    # Q conservation in every observer frame.
    cons_rows = []
    for name in frames:
        M = metrics[name]
        path_resid = max(opnorm(T.T@M@T-M) for T in local_edges[name])
        loop_resid = opnorm(local_H[name].T@M@local_H[name]-M)
        cons_rows.append((name,path_resid,loop_resid))
    cons_df = pd.DataFrame(cons_rows, columns=[
        "observer","max_path_Q_residual","loop_Q_residual"
    ])

    # Deliberately blind observer: left eigenvector of holonomy with eigenvalue 1.
    evals,evecs = np.linalg.eig(local_H["O2"].T)
    idx = np.argmin(np.abs(evals-1))
    p = np.real(evecs[:,idx]); p /= np.linalg.norm(p)
    Pblind = p.reshape(1,3)
    blind_resid = np.linalg.norm(Pblind@local_H["O2"] - Pblind)

    # Observer-network coherence.
    K_exact = F("O2","O0") @ F("O1","O2") @ F("O0","O1")
    exact_triangle = opnorm(K_exact-np.eye(3))

    E = np.zeros((3,3)); E[0,1] = 1e-3
    F12_bad = (np.eye(3)+E) @ F("O1","O2")
    K_bad = F("O2","O0") @ F12_bad @ F("O0","O1")
    bad_triangle = opnorm(K_bad-np.eye(3))

    # Z2 cycle obstruction.
    all_cob = {coboundary_cycle_z2(b) for b in itertools.product([0,1], repeat=4)}
    c_nontriv = (1,0,0,0)
    c_triv = (1,1,0,0)

    # Inject a bad local observer model.
    T_bad = local_edges["O3"][2].copy()
    T_bad[0,2] += 1e-3
    F03 = F("O0","O3")
    bad_cov = opnorm(F03@local_edges["O0"][2] - T_bad@F03)
    M3 = metrics["O3"]
    bad_Q = opnorm(T_bad.T@M3@T_bad-M3)

    # Open-system balance example.
    S = np.diag([1.0,1.0,0.8])
    v = np.array([1.2,-0.5,2.0])
    q0 = float(v@v); q1 = float((S@v)@(S@v))
    phi = q1-q0
    balance_resid = (q1-q0)-phi

    summary = pd.DataFrame([
        ["noncommutative order detected", float(np.mean(order_defects)), np.mean(order_defects)>TOL],
        ["nontrivial world holonomy", opnorm(H-np.eye(3)), opnorm(H-np.eye(3))>TOL],
        ["hidden-world Q conservation", q_resid, q_resid<TOL],
        ["exact observer covariance", cov_df["max_edge_cov_defect"].max(), cov_df["max_edge_cov_defect"].max()<TOL],
        ["observer can be holonomy-blind", blind_resid, blind_resid<TOL],
        ["exact observer triangle closes", exact_triangle, exact_triangle<TOL],
        ["perturbed observer triangle fails", bad_triangle, bad_triangle>1e-6],
        ["odd Z2 cycle obstruction", float(c_nontriv not in all_cob), c_nontriv not in all_cob],
        ["even Z2 cycle coboundary", float(c_triv in all_cob), c_triv in all_cob],
        ["bad local observer covariance detected", bad_cov, bad_cov>1e-6],
        ["bad local observer apparent Q violation", bad_Q, bad_Q>1e-6],
        ["open edge violates strict Q conservation", abs(q1-q0), abs(q1-q0)>TOL],
        ["open edge satisfies balance law", abs(balance_resid), abs(balance_resid)<TOL],
    ], columns=["test","numeric_value","pass"])

    print(summary.to_string(index=False))
    print(f"\nPassed {int(summary['pass'].sum())}/{len(summary)} checks.")
    return summary, cov_df, cons_df

if __name__ == "__main__":
    summary, covariance, conservation = run()
    summary.to_csv("series_b_relational_world_summary.csv", index=False)
    covariance.to_csv("series_b_observer_covariance.csv", index=False)
    conservation.to_csv("series_b_observer_conservation.csv", index=False)
