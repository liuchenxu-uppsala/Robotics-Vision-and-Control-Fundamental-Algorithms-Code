import numpy as np
from numpy import arccos, arctan2, rad2deg


def solve_ik_planar_2j(x, y, a1, a2):
    # 1. 计算末端到原点的距离平方
    d2 = x ** 2 + y ** 2
    L = np.sqrt(d2)

    # 安全检查：如果目标点超出手臂长度，直接返回
    if L > (a1 + a2) or L < abs(a1 - a2):
        return "目标点超出工作空间"

    # 2. 计算三角形内角 (余弦定理)
    # 这里的 cos_q1_internal 是大臂和小臂之间的夹角
    cos_q1_internal = (a1 ** 2 + a2 ** 2 - d2) / (2 * a1 * a2)
    q1_internal = arccos(np.clip(cos_q1_internal, -1, 1))

    # 转换成机器人关节角 q1 (通常是内角的补角)
    # q1 = 0 表示手臂伸直，正值往下拐，负值往上拐
    q1_down = np.pi - q1_internal
    q1_up = -(np.pi - q1_internal)

    # 3. 计算 beta (大臂 a1 和连线 L 之间的夹角)
    # 注意这里加了括号！
    cos_beta = (a1 ** 2 + d2 - a2 ** 2) / (2 * a1 * L)
    beta = arccos(np.clip(cos_beta, -1, 1))

    # 4. 计算 alpha (连线 L 和 X轴之间的夹角)
    alpha = arctan2(y, x)

    # 5. 组合成肩部角度 q0
    # 肘朝下时，肩膀要往“下”撇一点，所以是 alpha - beta (取决于你的坐标系定义)
    # 通常：肘朝下 q0 = alpha - beta; 肘朝上 q0 = alpha + beta
    q0_down = alpha - beta
    q0_up = alpha + beta

    return {
        "姿态 A (肘朝下)": (rad2deg(q0_down), rad2deg(q1_down)),
        "姿态 B (肘朝上)": (rad2deg(q0_up), rad2deg(q1_up))
    }


# --- 测试 ---
a1, a2 = 1.0, 1.0
target_x, target_y = 1.2, 0.5

solutions = solve_ik_planar_2j(target_x, target_y, a1, a2)

if isinstance(solutions, dict):
    for pose, angles in solutions.items():
        # angles[0] 是 q0 (肩膀), angles[1] 是 q1 (肘部)
        print(f"{pose}: 肩膀 q0 = {angles[0]:.2f}°, 肘部 q1 = {angles[1]:.2f}°")
else:
    print(solutions)