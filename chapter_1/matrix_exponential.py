import numpy as np
import scipy.linalg as linalg
from scipy.linalg import logm, expm
from spatialmath import Twist2
from spatialmath.base import *

C = np.array([1,0])
theta = np.pi/2
TC = transl2(C)@trot2(theta)@transl2(-C)
print("1. 手动构造的动作矩阵 TC (绕点 [1,0] 转 90度):")
print(TC)

L = logm(TC)
S = vexa(L)
print("--------------------------------------break0------------------------------")
print(L)
print("\n2. 提取出来的螺旋向量 S (动作的压缩包):")
print(f"vx: {S[0]:.4f}, vy: {S[1]:.4f}, omega: {S[2]:.4f}")
print("--------------------------------------break1------------------------------")
TC_recovered = expm(skewa(S))
print("\n3. 利用 expm(skewa(S)) 还原出来的矩阵:")
print(TC_recovered)

if np.allclose(TC, TC_recovered):
    print("\n✅ 验证成功：S 向量完美保存了整个变换动作！")
print("--------------------------------------break------------------------------")

T = transl2(3, 4) @ trot2(0.5)
S = Twist2(T)
print(S.exp(0.5))
print(T)
