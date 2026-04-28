from spatialmath.base import *
import numpy as np
import matplotlib.pyplot as plt

T1 = transl2(1, 2)    # 移动矩阵
T2 = trot2(np.pi/6)   # 旋转矩阵（30度）

T_A = T1 @ T2  # 矩阵相乘
print(T1)
print(T2)
print(T_A)

# 2. 创建一个坐标轴窗口
plotvol2([-0.5, 5, -0.5, 5])
trplot2(T_A, frame="A", color="b")

T0 = transl2(0, 0)
trplot2(T0, frame="0", color="k")

TB = transl2(2, 1)
trplot2(TB, frame="B", color="r")
TAB = T_A @ TB
print(TAB)
trplot2(TAB, frame="AB", color="g")


P = np.array([3, 2])
plot_point(P, "ko", text="P")

plt.show() # 3. 这一行是关键，不加这行窗口会闪退或不显示