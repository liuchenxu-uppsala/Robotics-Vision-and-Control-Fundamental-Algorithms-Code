import numpy as np
from spatialmath.base import rotx, trplot, tranimate, roty, rotz, eul2r, tr2eul, rpy2r, tr2rpy
import matplotlib.pyplot as plt
# R = rotx(np.pi / 2)
R = rotx(np.pi / 2) @ roty(np.pi / 2)
trplot(R, anaglyph=True)
plt.show()
# tranimate(R, anaglyph=True)
# plt.show()

#ZYZ
R = rotz(0.1) @ roty(0.2) @ rotz(0.3)
print(R)
R2 = eul2r(0.1, 0.2, 0.3)
print(R2)
gamma = tr2eul(R2)
print(gamma)
R3 = eul2r(0.1, 0.0, 0.3)
print(tr2eul(R3))
print("--------------------------------------zyx------------------------------")
R = rpy2r(0.1, 0.2, 0.3, order="zyx")
print(R)
gamma = tr2rpy(R, order="zyx")
print(gamma)