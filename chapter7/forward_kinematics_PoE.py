import numpy as np
from spatialmath import SE2, Twist2

a1=1.0
a2=1.0

TE0 = SE2(a1+a2,0,0)
S0 = Twist2.UnitRevolute([0, 0])
S1 = Twist2.UnitRevolute([a1,0])
q = np.deg2rad([30,40])
result = S0.exp(q[0])*S1.exp(q[1])
print(result)