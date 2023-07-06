# TRABALHO 16
# Gilmar dos Reis JÃºnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva HonÃ³rio
# Matheus Henrique Maia Ramos

# Interpolação inversa

import numpy as np

Vx = np.array([18, 19, 20, 21, 22, 23]) #dados de x
fx = np.array([1400, 1900, 2500, 3250, 4200, 5400]) #dados de f(x)
nintervalos = 100000 #codigo roda mais rápido se diminuirmos o numero de intervalos, porem a precisao diminui
intervalos = np.linspace(18, 23, nintervalos)  #intervalos para a busca incremental
f = 0
fdesejado = 2800 #valor de f(x) que deseja-se obter


def L(i, j): #funcao Li

    return (Xi - Vx[j])/(Vx[i] - Vx[j])


for m in range(len(intervalos)):

    Xi = intervalos[m] #busca incremental sendo realizada
    f = 0

    for k in range(len(Vx)):

        Li = 1

        for x in range(len(Vx)):

            if (x != k):
                Li = Li * L(k, x) #calculo de Li de cada ponto

        f = f+(Li*fx[k]) #calculando o polinomio interpolador de lagrange


    if(f>= fdesejado):
        print("O x para f(x) seja ",fdesejado, " é " ,intervalos[m]) #f(x) encontrado mais próximo de fdesejado(x)
        break