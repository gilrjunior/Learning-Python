#TRABALHO 8
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np
import math

#MÉTODO DE GAUSS JACOBI

#MATRIZ AX = B SERÁ TRANSFORMADA NUMA MATRIZ DO TIPO X = CX + g

#Erro mr
def erro(m, Vxnovo):
    maximo = max(Vxnovo)
    mr = m/maximo
    return mr

#Máximo valor do vetor de subtrações par a par entre 
#a aproximação atual e a aproximação anterior
def m(Vxnovo, Vx):
    subVx = np.zeros(len(Vx))
    for i in range(len(Vx)):
        subVx[i] = abs(Vxnovo[i] - Vx[i])
    m = max(subVx)
    return m

#Declaração da matriz de entrada do exercício
C1 = np.array([[7.0 , -1.0 , 2.0 , 1.0 , -1.0],
               [-1.0 , -9.0 , 1.0 , -1.0 , 2.0],
               [0.0 , 1.0 , 8.0 , -1.0 , 1.0],
               [-2.0 , 3.0 , -1.0 , -10.0 , 1.0],
               [-1.0 , 0.0 , 0.0 , 1.0 , 11.0]])

#Declaração da diagonal da matriz (facilitador para cálculos)
C1Diag = np.array([7.0,-9.0,8.0,-10.0,11.0])

#Matriz dos termos independentes
g = np.array([-1.0,0.5,2.0,-1.5,3.0])

#Vetor de variáveis x do iteração anterior e da iteração atual
Vx = np.zeros(len(C1[0]))
Vxnovo = np.zeros(len(C1[0]))

#Preparacao da matriz para o sistema linear
for i in range(len(C1[0])):
    for j in range(len(C1[0])):
        C1[i][j]/=(-C1Diag[i])
        if(i == j):
            C1[i][j] = 0 #Como isolamos o termo Xn na n-ésima linha, a diagonal principal
            #ficará preenchida de zeros
    g[i]/=C1Diag[i]


k = 0 #quantidade de iterações (inicializando o k)
mr = 1
while (mr > 0.02):
    Vx = Vxnovo #Iteracao anterior recebe a atual
    Vxnovo = np.zeros(len(Vx))#Zeramos a iteracao atual para que ela receba o novo resultado
    #da multiplicação matricial da proxima iteração
    for i in range(len(C1[0])):
        for j in range(len(C1[0])):
            Vxnovo[i] += C1[i][j] * Vx[j]
        Vxnovo[i] += g[i]
    k+=1
    if(k > 1):
        mr = erro(m(Vxnovo,Vx),Vxnovo)

print(Vxnovo,'\n')

