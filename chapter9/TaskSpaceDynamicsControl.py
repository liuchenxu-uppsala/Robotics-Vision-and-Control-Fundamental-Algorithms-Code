import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath import SE2

# 1. 定义机器人模型 (以你的 RevoluteDH 为例)
# 假设是一个简单的二连杆
L1, L2 = 1.0, 1.0
robot = DHRobot([
    RevoluteDH(a=L1),
    RevoluteDH(a=L2)
], name="MyRobot")

# 设置动力学参数（质量、质心等，否则无法计算 M）
robot.links[0].m = 2.0  # 连杆 1 质量
robot.links[1].m = 1.0  # 连杆 2 质量


def control_step(q, qd, x_dd_star):
    """
    q: 当前关节角度
    qd: 当前关节速度
    x_dd_star: 任务空间期望加速度 (例如 [2.0, 1.0])
    """

    # 2. 获取当前的雅可比矩阵 J
    # jacob0 得到的是相对于基坐标系的雅可比
    J = robot.jacob0(q)
    # 对于 2D 机器人，通常只取前两行 (x, y 方向)
    J = J[:2, :]

    # 3. 获取当前姿态下的关节质量矩阵 M
    M = robot.inertia(q)

    # 4. 计算等效质量矩阵 Lambda = (J * M^-1 * J^T)^-1
    M_inv = np.linalg.inv(M)
    Lambda = np.linalg.inv(J @ M_inv @ J.T)

    # 5. 计算非线性项补偿 (Coriolis & Gravity)
    # 在 roboticstoolbox 中，可以直接获取关节空间的补偿力矩，再转到空间
    tau_nle = robot.coriolis(q, qd) @ qd + robot.gravload(q)
    # 将其映射到任务空间的力 (F_nle = J^-T * tau_nle)
    F_nle = np.linalg.inv(J.T) @ tau_nle

    # 6. 计算最终需要的空间力 F
    F = Lambda @ x_dd_star + F_nle

    # 7. 翻译回电机力矩指令 tau = J^T * F
    tau = J.T @ F

    return tau


# 模拟一个状态
q_curr = np.array([0.1, 0.2])
qd_curr = np.array([0.0, 0.0])
x_accel = np.array([0.5, 0.0])  # 想要手尖向 X 加速

torque = control_step(q_curr, qd_curr, x_accel)
print(f"电机需要输出的力矩: {torque}")