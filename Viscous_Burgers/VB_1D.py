
import numpy as np

deltaT = 0.01
deltaX = 0.01
nu     = 1.0

DimB     = [-1, 1] #shows simulation space boundary
SpaceLen = DimB[1] - DimB[0]

Time = 10 #simulation Time

time_step  = int(Time / deltaT)
space_step = int(SpaceLen / deltaX)

C1 = deltaT / (2*deltaX)
C2 = (deltaT * nu) / (deltaX ** 2)

P = np.zeros((time_step, space_step))
P = P.astype(np.longdouble)


for X in range(space_step):
    P[0][X] = np.exp(-(2*(X*deltaX - 1))**2)


for T in range(time_step - 1):
    for X in range(space_step):
        P[T+1][X] = P[T][X] + C1 * (P[T][X]* (P[T][(X+1)%space_step] - P[T][X-1]) ) \
            + C2 * (P[T][(X+1)%space_step] - 2 * P[T][X] + P[T][X-1])

np.savetxt('viscusBurgersEq.csv', P, delimiter=',', fmt='%g')


