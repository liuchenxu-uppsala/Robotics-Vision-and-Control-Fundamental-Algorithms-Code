import numpy as np
import sympy as sp

theta, d = sp.symbols('theta d')
local_rot = sp.Matrix(
    [
        [sp.cos(theta), -sp.sin(theta), 0],
        [sp.sin(theta), sp.cos(theta), 0],
        [0, 0, 1],
    ]
)
T_rot = sp.eye(4)
T_rot[0:3,0:3] = local_rot

T_mv = sp.eye(4)
T_mv[0,3] = d

T_total = T_rot * T_mv
print("--- SymPy 自动化简出来的最终复合变换矩阵 ---")
sp.pprint(T_total)

matrix_compiler = sp.lambdify((theta, d), T_total, 'numpy')
current_theta = np.radians(30.0)
current_d = 0.5
T_now = matrix_compiler(current_theta, current_d)
print(T_now)
