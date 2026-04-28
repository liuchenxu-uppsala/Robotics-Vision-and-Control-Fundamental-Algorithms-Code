from spatialmath import SE2
from roboticstoolbox import ET2
import numpy as np
a1=1
a2=1
e = ET2.R() * ET2.tx(a1) * ET2.R() * ET2.tx(a2)
print(e)

q0 = np.deg2rad(30)
q1 = np.deg2rad(40)

result = e.fkine([q0,q1])
print(result)