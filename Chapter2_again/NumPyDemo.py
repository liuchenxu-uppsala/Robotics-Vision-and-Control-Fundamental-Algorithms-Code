import numpy as np

theta = np.radians(30)
matrix_rotate = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
T = np.eye(3)
T[0:2, 0:2] = matrix_rotate
T[0:2,2] = [1,2]
print("--- 扫地机器人当前齐次变换矩阵 T ---")
print(T)

p_local = np.array([1.0, 0.0, 1.0])
p_world = T @ p_local
print("\n--- 障碍物在世界坐标系下的真实位置 ---\n")
print(p_world)
print(f"\nX_w: {p_world[0]:.3f}, Y_w: {p_world[1]:.3f}")

