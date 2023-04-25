# TRABALHO 13
# Gilmar dos Reis Júnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva Honório
# Matheus Henrique Maia Ramos

import numpy as np
import matplotlib.pyplot as plt

i = 0
Sx12 = 0
Sx1x2 = 0
Sx1y = 0
Sx2y = 0
Sx22 = 0

x1 = np.array([0, 2, 2.5, 1, 4, 7])
x2 = np.array([0, 1, 2, 3, 6, 2])
y = np.array([6, 11, 9, 1, 3, 27])

Sx1 = x1.sum()
Sx2 = x2.sum()
Sy = y.sum()

for i in range(len(x1)):

    Sx12 += x1[i]**2
    Sx1x2 += x1[i]*x2[i]
    Sx22 += x2[i]**2
    Sx1y += x1[i]*y[i]
    Sx2y += x2[i]*y[i]

matriz = np.array([[len(x1), Sx1, Sx2],
                   [Sx1, Sx12, Sx1x2],
                   [Sx2, Sx1x2, Sx22]])

matrizC1R = np.array([[Sy, Sx1, Sx2],
                      [Sx1y, Sx12, Sx1x2],
                      [Sx2y, Sx1x2, Sx22]])

matrizC2R = np.array([[len(x1), Sy, Sx2],
                      [Sx1, Sx1y, Sx1x2],
                      [Sx2, Sx2y, Sx22]])

matrizC3R = np.array([[len(x1), Sx1, Sy],
                      [Sx1, Sx12, Sx1y],
                      [Sx2, Sx1x2, Sx2y]])

det = np.linalg.det(matriz)
det1 = np.linalg.det(matrizC1R)
det2 = np.linalg.det(matrizC2R)
det3 = np.linalg.det(matrizC3R)

a0 = det1/det
a1 = det2/det
a2 = det3/det

print(a0)
print(a1)
print(a2)
