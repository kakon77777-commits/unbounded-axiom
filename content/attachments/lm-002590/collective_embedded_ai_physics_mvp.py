import numpy as np, math
m=1.7; w=1.3; t_star=1.17
z0=np.array([1.2, -0.45, 0.35, 1.05],float)

def Phi(t):
    c,s=math.cos(w*t),math.sin(w*t)
    return np.array([
        [c,0,s/w,0],[0,c,0,s/w],
        [-w*s,0,c,0],[0,-w*s,0,c]
    ],float)

obs={
"O1_pos":np.array([[1,0,0,0],[0,1,0,0]],float),
"O2_xvx":np.array([[1,0,0,0],[0,0,1,0]],float),
"O3_yvy":np.array([[0,1,0,0],[0,0,0,1]],float),
"O4_diag":np.array([[1,1,0,0],[0,0,1,-1]],float),
}

print("Individual ranks:")
for k,H in obs.items():
    print(k,np.linalg.matrix_rank(H))
print("O2+O3 joint rank:",np.linalg.matrix_rank(np.vstack([obs["O2_xvx"],obs["O3_yvy"]])))
print("O1 position-only two-time observability rank:",
      np.linalg.matrix_rank(np.vstack([obs["O1_pos"]@Phi(0),obs["O1_pos"]@Phi(0.43)])))
