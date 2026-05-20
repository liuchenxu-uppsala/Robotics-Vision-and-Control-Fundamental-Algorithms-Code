import numpy as np

theta  = np.radians(45)
matrix_rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
move = np.array([2,3])
T = np.eye(3)
T[0:2,0:2] = matrix_rotation
T[0:2,2] = move
p_local = np.array([0.0, 1.0, 1.0])
p_world = T@p_local
print(p_world)
print(f"\nX_w: {p_world[0]:.3f}, Y_w: {p_world[1]:.3f}")