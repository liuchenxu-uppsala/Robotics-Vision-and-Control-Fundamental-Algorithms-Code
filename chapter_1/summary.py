from matplotlib import pyplot as plt
from spatialmath import SE2

TA = SE2(1, 2) * SE2(30, unit="deg")
print(TA.R)
print(TA.t)
TA.plot(frame="A", color="b")
plt.show()