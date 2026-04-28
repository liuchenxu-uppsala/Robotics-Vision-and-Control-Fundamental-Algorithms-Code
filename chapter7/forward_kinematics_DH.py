import numpy as np
from matplotlib import pyplot as plt
from roboticstoolbox import DHRobot, RevoluteDH

link1 = RevoluteDH(d=0, a=1.0, alpha=0)
link2 = RevoluteDH(d=0, a=2.0, alpha=0)

robot = DHRobot([link1, link2])
print(robot)

result = np.deg2rad([30,40])
robot.fkine(result)
print(result)

# robot.teach(result)
# plt.show()

robot.plot(result, block=True)

