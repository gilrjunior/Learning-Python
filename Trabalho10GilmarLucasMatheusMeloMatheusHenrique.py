# TRABALHO 10
# Gilmar dos Reis Júnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva Honório
# Matheus Henrique Maia Ramos

import numpy as np

import matplotlib.pyplot as plt


def f(a0, a1, x):

    return a0 + (a1 * x)


Vx = np.array([1980, 1985, 1990, 1993, 1997, 2000, 2006])

Vy = np.array([8300, 9900, 10400, 13200, 13600, 13700, 14600])

Svx = Vx.sum()
Svy = Vy.sum()
Sxy = 0
Sx2 = 0
St = 0
Sr = 0
aux1 = 0
aux2 = 0


for i in range(len(Vy)):
    aux1 += Vx[i] * Vy[i]
    aux2 += Vx[i]**2
    St += (Vy[i] - (Vy.sum() / len(Vy)))**2

a1 = ((len(Vx) * aux1) - (Vx.sum() * Vy.sum())) / \
    ((len(Vx) * aux2) - (Vx.sum()**2))
a0 = (Vy.sum() / len(Vy)) - (a1 * (Vx.sum() / len(Vx)))

for i in range(len(Vx)):
    Sr += (Vy[i] - a0 - (a1 * Vx[i]))**2

r2 = (St - Sr) / St

print(a0)
print(a1)
print(r2)

plt.plot(Vx, Vx*a1 + a0)
plt.scatter(Vx, Vy)
plt.show()
