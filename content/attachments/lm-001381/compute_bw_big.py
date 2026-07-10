import numpy as np, math, time

# Large-scale: B-W(M) = sum_{m<=M} (-1)^m r3(m).
# r3 = theta1 conv theta1 conv theta1 where theta1[m]=r1(m).
# Use FFT-based convolution with float64, values of r3 are small (max ~ few hundred) -> safe rounding.
M = 4_000_000
t0=time.time()
theta = np.zeros(M+1)
n = np.arange(0, int(math.isqrt(M))+1)
theta[n*n] = 2.0
theta[0] = 1.0
# r2 = theta*theta truncated
L = 1
while L < 2*(M+1): L <<= 1
ft = np.fft.rfft(theta, L)
r2 = np.fft.irfft(ft*ft, L)[:M+1]
r2 = np.rint(r2).astype(np.int64)
# r3 = r2 conv theta truncated
f2 = np.fft.rfft(r2.astype(np.float64), L)
r3 = np.fft.irfft(f2*ft, L)[:M+1]
r3 = np.rint(r3).astype(np.int64)
print("fft done", time.time()-t0, "s; spot check r3(0..5):", r3[:6], "(expect 1 6 12 8 6 24)")

signs = np.where(np.arange(M+1)%2==0, 1, -1)
BW = np.cumsum(signs*r3)
hits_center = np.where((BW==0)|(BW==1))[0]
hits_any = np.where(np.abs(BW)<=1)[0]
print("center-start hits (B-W in {0,1}) up to M=%d:"%M)
print(list(hits_center[:80]), "... total:", len(hits_center))
print("any-endpoint hits total:", len(hits_any))
print("last few any hits:", list(hits_any[-10:]))
# growth of running max |BW|
run = np.maximum.accumulate(np.abs(BW))
for m in [10**2,10**3,10**4,10**5,10**6, 2*10**6, 4*10**6]:
    if m<=M: print(f"M={m:>8}  max|B-W| so far = {run[m]:>8}  ~ M^{math.log(run[m])/math.log(m):.3f}")
np.save("BW.npy", BW[:1000001])
