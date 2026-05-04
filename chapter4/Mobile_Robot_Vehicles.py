import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

# 1. 创建一个单轮机器人模型 (Unicycle)
# 初始位置在 (0, 0)，朝向 0 弧度 (向东)
robot = rtb.Unicycle(x0=[0, 0, 0])

# 2. 定义控制指令 [v, omega]
# 假设线速度 v = 1 m/s, 角速度 omega = 0.5 rad/s (向左缓转)
u = [1, 0.5]

# 3. 模拟运动 (Integration)
# 模拟 10 秒钟，看看轨迹
# robot.step 会根据运动学方程更新状态 q_dot = [v*cosθ, v*sinθ, omega]
dt = 0.1
t_end = 10
history = []

x = robot.x # 获取初始位姿
for t in np.arange(0, t_end, dt):
    history.append(robot.x.flatten().copy())
    # 在 RTB 中，step 函数会自动应用我们学过的运动学公式
    x = robot.step(u, dt)

history = np.array(history)

# 4. 可视化
plt.figure(figsize=(8, 6))
plt.plot(history[:, 0], history[:, 1], 'b-', label='Robot Trajectory')
plt.quiver(history[::10, 0], history[::10, 1],
           np.cos(history[::10, 2]), np.sin(history[::10, 2]),
           color='red', scale=10, label='Heading')
plt.title("Unicycle Model Trajectory (v=1, ω=0.5)")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()