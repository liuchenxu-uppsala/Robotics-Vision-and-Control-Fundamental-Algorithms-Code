import numpy as np

u, v = 0.2, 0.2
z = 1.0
lmbda = 0.5
s_star = np.array([0, 0])
s_curr = np.array([u, v])

Ls = np.array([
    [-1/z,  0,    u/z],
    [ 0,   -1/z,  v/z]
])

e = s_curr - s_star

Ls_pinv = np.linalg.pinv(Ls)
vc = -lmbda * Ls_pinv @ e
print(f"推荐相机速度 (vx, vy, vz): {vc}")