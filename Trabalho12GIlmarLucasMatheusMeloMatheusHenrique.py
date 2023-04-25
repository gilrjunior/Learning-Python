#TRABALHO 12
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np
import matplotlib.pyplot as plt

def f(x, a0, a1, a2):
   
    return a2*(x**2)+a1*x+a0

Vx = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90 ,1.00])
Vc = np.array([0.62, 0.63, 0.64, 0.66, 0.68, 0.71, 0.76, 0.81, 0.89, 1.00])

Vx2 = np.array([])
Vx3 = np.array([])
Vx4 = np.array([])
Sxy = 0
Sx2y = 0

i = 0

for i in range(len(Vx)):
   
    Vx2 = np.append(Vx2, Vx[i]**2)
    Vx3 = np.append(Vx3, Vx[i]**3)
    Vx4 = np.append(Vx4, Vx[i]**4)
   
    Sxy += (Vx[i] * Vc[i])
    Sx2y += (Vx[i]**2 * Vc[i])
     
Svx = Vx.sum()
Svc = Vc.sum()
Svx2 = Vx2.sum()
Svx3 = Vx3.sum()
Svx4 = Vx4.sum()

matriz = np.array([[len(Vx), Svx, Svx2],
                   [Svx, Svx2, Svx3],
                   [Svx2, Svx3, Svx4]])

matrizC1R = np.array([[Svc, Svx, Svx2],
                      [Sxy, Svx2, Svx3],
                      [Sx2y, Svx3, Svx4]])

matrizC2R = np.array([[len(Vx), Svc, Svx2],
                      [Svx, Sxy, Svx3],
                      [Svx2, Sx2y, Svx4]])

matrizC3R = np.array([[len(Vx), Svx, Svc],
                      [Svx, Svx2, Sxy],
                      [Svx2, Svx3, Sx2y]])

det = np.linalg.det(matriz)
det1 = np.linalg.det(matrizC1R)
det2 = np.linalg.det(matrizC2R)
det3 = np.linalg.det(matrizC3R)

a0 = det1/det
a1 = det2/det
a2 = det3/det

valf = f(Vx, a0, a1, a2)

St = 0
Sr = 0

for i in range(len(Vc)):
    St+=((Vc[i] - np.average(Vc))**2)
    Sr+=((Vc[i] - a0 - a1*Vx[i] - a2*Vx2[i])**2)

r2 = (St - Sr)/St
print(r2)

plt.plot(Vx, valf)
plt.scatter(Vx, Vc)
plt.show()

