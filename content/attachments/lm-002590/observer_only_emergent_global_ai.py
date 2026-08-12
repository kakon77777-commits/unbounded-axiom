import numpy as np
import pandas as pd
import math

SEED = 20260810
rng = np.random.default_rng(SEED)

w = 1.3
m = 1.7

def Phi(t):
    c,s = math.cos(w*t), math.sin(w*t)
    return np.array([
        [c,0,s/w,0],
        [0,c,0,s/w],
        [-w*s,0,c,0],
        [0,-w*s,0,c]
    ], float)

def energy(z):
    x,y,vx,vy = z
    return 0.5*m*(vx*vx+vy*vy) + 0.5*m*w*w*(x*x+y*y)

def Lz(z):
    x,y,vx,vy=z
    return m*(x*vy-y*vx)

def build_observers(n_obs):
    base = [
        np.array([[1,0,0,0],[0,1,0,0]], float),
        np.array([[1,0,0,0],[0,0,1,0]], float),
        np.array([[0,1,0,0],[0,0,0,1]], float),
        np.array([[1,1,0,0],[0,0,1,-1]], float),
        np.array([[1,-1,0,0],[0,0,1,1]], float),
    ]
    obs={}
    for i in range(n_obs):
        if i < len(base):
            A=base[i]
        else:
            A=rng.normal(size=(2,4))
            q,_=np.linalg.qr(A.T)
            A=q[:,:2].T
        obs[f"O{i+1:02d}"]=A
    return obs

def fuse(obs, measurements, active=None):
    if active is None:
        active=list(obs.keys())
    H=np.vstack([obs[k] for k in active])
    y=np.concatenate([measurements[k] for k in active])
    zhat=np.linalg.pinv(H)@y
    return zhat, np.linalg.norm(H@zhat-y), np.linalg.matrix_rank(H)

def diagnose(obs, measurements):
    rows=[]
    keys=list(obs.keys())
    for excluded in keys:
        kept=[k for k in keys if k != excluded]
        zhat,fit,rank=fuse(obs,measurements,kept)
        pred=obs[excluded]@zhat
        score=np.linalg.norm(pred-measurements[excluded])
        rows.append((excluded,score,fit,rank))
    return sorted(rows,key=lambda x:x[1],reverse=True)

def reconstruct_history(A,times,yhist):
    O=np.vstack([A@Phi(t) for t in times])
    y=np.concatenate(yhist)
    z0hat=np.linalg.pinv(O)@y
    return z0hat,np.linalg.matrix_rank(O)

def run_trial(n_obs=8,sigma=0.01,n_history=4,bad_fraction=0.125,bias_scale=0.18):
    obs=build_observers(n_obs)
    z0=rng.normal(size=4)
    t_now=float(rng.uniform(0.4,2.0))
    z_true=Phi(t_now)@z0

    measurements={
        k:A@z_true+rng.normal(0,sigma,size=2)
        for k,A in obs.items()
    }

    n_bad=max(1,int(round(n_obs*bad_fraction)))
    bad_ids=list(rng.choice(list(obs.keys()),size=n_bad,replace=False))
    for k in bad_ids:
        measurements[k]+=rng.normal(0,bias_scale,size=2)

    z_all,_,rank_all=fuse(obs,measurements)

    diagnostic=diagnose(obs,measurements)
    suspects=[r[0] for r in diagnostic[:n_bad]]
    kept=[k for k in obs if k not in suspects]
    z_repair,_,rank_repair=fuse(obs,measurements,kept)

    o1=list(obs.keys())[0]
    times=np.linspace(0,t_now,n_history)
    yhist=[
        obs[o1]@(Phi(ti)@z0)+rng.normal(0,sigma,size=2)
        for ti in times
    ]
    z0_hist,rank_hist=reconstruct_history(obs[o1],times,yhist)
    z_hist=Phi(t_now)@z0_hist
    z_hybrid=0.5*(z_repair+z_hist)

    Etrue=energy(z_true)
    Ltrue=Lz(z_true)
    def errs(z):
        return (
            np.linalg.norm(z-z_true),
            abs(energy(z)-Etrue)/max(abs(Etrue),1e-15),
            abs(Lz(z)-Ltrue)/max(abs(Ltrue),1e-15),
        )
    ea=errs(z_all)
    er=errs(z_repair)
    eh=errs(z_hist)
    ehy=errs(z_hybrid)

    hits=len(set(suspects)&set(bad_ids))
    return {
        "n_obs":n_obs,"sigma":sigma,"n_bad":n_bad,
        "joint_rank_all":rank_all,
        "joint_rank_repaired":rank_repair,
        "history_rank":rank_hist,
        "state_err_all":ea[0],
        "state_err_repaired":er[0],
        "state_err_history_only":eh[0],
        "state_err_hybrid":ehy[0],
        "Eerr_all":ea[1],"Eerr_repaired":er[1],
        "Eerr_history":eh[1],"Eerr_hybrid":ehy[1],
        "Lerr_all":ea[2],"Lerr_repaired":er[2],
        "Lerr_history":eh[2],"Lerr_hybrid":ehy[2],
        "bad_detection_rate":hits/n_bad,
        "all_bad_identified":set(suspects)==set(bad_ids)
    }

def main():
    records=[]
    for n_obs in [5,8,12,20]:
        for sigma in [0.0,0.005,0.01,0.03]:
            for _ in range(120):
                records.append(run_trial(
                    n_obs=n_obs,
                    sigma=sigma,
                    n_history=4,
                    bad_fraction=0.1 if n_obs>=10 else 0.125,
                    bias_scale=0.18
                ))
    df=pd.DataFrame(records)
    agg=df.groupby(["n_obs","sigma"]).agg(
        mean_rank=("joint_rank_all","mean"),
        mean_state_err_all=("state_err_all","mean"),
        mean_state_err_repaired=("state_err_repaired","mean"),
        mean_state_err_history=("state_err_history_only","mean"),
        mean_state_err_hybrid=("state_err_hybrid","mean"),
        median_Eerr_repaired=("Eerr_repaired","median"),
        median_Lerr_repaired=("Lerr_repaired","median"),
        mean_bad_detection=("bad_detection_rate","mean"),
        all_bad_exact_rate=("all_bad_identified","mean"),
    ).reset_index()

    print(agg.to_string(index=False))
    print("\nOverall:")
    print("Full-rank fused rate:",(df.joint_rank_all==4).mean())
    print("History full-rank rate:",(df.history_rank==4).mean())
    print("Mean state error all:",df.state_err_all.mean())
    print("Mean state error repaired:",df.state_err_repaired.mean())
    print("Mean state error history:",df.state_err_history_only.mean())
    print("Mean state error hybrid:",df.state_err_hybrid.mean())
    print("Mean bad detection:",df.bad_detection_rate.mean())
    print("Exact bad-set ID:",df.all_bad_identified.mean())

    df.to_csv("observer_only_emergent_global_ai_trials.csv",index=False)
    agg.to_csv("observer_only_emergent_global_ai_summary.csv",index=False)

if __name__=="__main__":
    main()
