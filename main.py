
import datetime
from vias import Via, Ciudad
import vias
import numpy.random as random

random.seed(1)

A = Via("A", 4, 2, 9)
B = Via("B", 3.75, 3, 13)
C = Via("C", 5, 1, 3)


A.start(vias.prolluvia, 0.2, 0.15)
B.start(vias.prolluvia, 0.8, 0.3)
C.start(vias.prolluvia, 0.1, 0.05)

ciudad = Ciudad([A, B, C])

while vias.t < vias.fin:
    print(vias.t, vias.fin)
    vias.t = vias.t + vias.delta
    ciudad.update()


p_lluvia = 0.3
p_no_lluvia = 1 - p_lluvia
