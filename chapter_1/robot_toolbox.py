from roboticstoolbox import models
from swift import Swift   # ✅ 注意这里

robot = models.DH.Puma560()

env = Swift()
env.launch()

env.add(robot)

robot.q = robot.qz
env.step()