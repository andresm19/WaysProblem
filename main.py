
import datetime
from vias import Via, Ciudad, P, probabilidad, obtener, probabilidad_Total
import vias
import numpy.random as random

random.seed(1)

lluvia = tuple()

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
    lluvia = ([A.plluvia, 1-A.plluvia],[])
    lluvia2 = ([B.plluvia, 1-B.plluvia],[])
    lluvia3 = ([C.plluvia, 1-C.plluvia],[])
    ciudad.update()




trafico_lluvia =  ([[True],[0.4, 0.6], 
                  [False],[0.01, 0.99]],["Lluvia"])

mayortiempo_accidentalidad_ = ([[True],[0.4, 0.5],
                              [False],[0.6, 0.5]],["accidentalidad"])


accidentalidad_Lluvia_Trafico = ([[True,True],[0, 1],
                              [True,False],[0.8, 0.2],
                              [False,True],[0.9, 0.1],
                              [False,False],[0.99, 0.01]  ],["Lluvia","Trafico"])

vias.accidentalidad_Lluvia_Trafico = accidentalidad_Lluvia_Trafico




#Crear diccionario global que tome mis datos bien bellos

mi_diccionario = {"Trafico":trafico_lluvia,"accidentalidad":accidentalidad_Lluvia_Trafico,"Lluvia":lluvia,"mayortiempo":mayortiempo_accidentalidad_}
vias.mi_diccionario = mi_diccionario


print("\nProbabilidad total de lluvia para cada ciudad: ")
print("\nCiudad A: ", end='')
print(probabilidad_Total(trafico_lluvia,True))
print("\nCiudad B: ", end='')
print(probabilidad_Total(lluvia2,True))
print("\nCiudad C: ", end='')
print(probabilidad_Total(lluvia3,True))

