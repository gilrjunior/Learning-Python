# TRABALHO 15
# Gilmar dos Reis JÃºnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva HonÃ³rio
# Matheus Henrique Maia Ramos
 
#Polinômio interpolador de Lagrange

import numpy as np

Vx = np.array([18,19,20,21,22,23]) #dados de x
fx = np.array([1400, 1900, 2500, 3250, 4200, 5400]) #dados de f(x)
Xi = 21.8 #valor de x que queremos obter o f(x)
f = 0

def L(i, j): #funcao Li

    return (Xi - Vx[j])/(Vx[i] - Vx[j])

for k in range(len(Vx)):

    Li = 1

    for x in range(len(Vx)):

        if(x!= k):
            Li = Li * L(k, x) #calculo de Li de cada ponto

    f = f+(Li*fx[k]) #calculando o polinomio interpolador de lagrange

print(round(f, 3)) #resultado f(Xi)