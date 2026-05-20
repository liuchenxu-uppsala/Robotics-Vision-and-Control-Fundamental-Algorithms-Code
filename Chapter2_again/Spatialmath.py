from spatialmath import SO2
import numpy as np

# 1. 直接用角度创建标准的 SO(2) 对象（Toolbox 会自动在底层做安检）
R1 = SO2(30, unit='deg')
print("--- Toolbox 生成的规范 SO(2) 矩阵 ---")
R1.print()

# 2. 连续旋转：再转 45 度，在群内直接相乘
R2 = SO2(45, unit='deg')
R_total = R1 * R2
print(f"\n连续旋转后的总角度: {R_total.theta() * 180 / np.pi:.1f} 度")