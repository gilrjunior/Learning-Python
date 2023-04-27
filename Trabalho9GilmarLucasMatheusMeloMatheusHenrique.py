#TRABALHO 9
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

#MÉTODO GAUSS-SEIDEL

import numpy as np
import math

def erro(Vxant, Vxnovo):

    Vxsub = np.zeros(len(Vxant))

    for i in range(len(Vxant)):
        Vxsub[i] = abs(Vxnovo[i] - Vxant[i])
    m = max(Vxsub)#maximo valor do modulo da subtracao 
    #de variaveis entre a iteracao 'k' e a 'k+1'
    maximo = max(Vxnovo)#Maximo valor das variaveis da nova iteracao

    mr = m/maximo

    return mr

C = np.array([[9.0, -1.0, 2.0, 0.0, -1.0],
               [-1.0, -11.0, 1.0, -1.0, 2.0],
               [1.0, 1.0, 8.0, -1.0, 1.0],
               [-2.0, 3.0, -1.0, -12.0, 1.0],
               [-1.0, 0.0, 0.0, 1.0, 10.0]])

CDiag = np.diag(C)
print(C)
print('\n',CDiag)
g = np.array([-2.0, (1.0/3.0), 2.0, (-3.0/2.0), 2])
print(g)
Vxnovo = np.zeros(len(C[0])) #Vx = np.array(5)
Vxant = np.zeros(len(C[0]))

#Usando os valores do exemplo do material apenas
#x1 = (7.85 + 0.1x2 + 0.2x3)/(3.0) --> processo feito na linha 56 (iterado nas variaveis)
#x2 = (-19.3 - 0.1x1 + 0.2x3)/(10.0)
#x3 = (71.4 - 0.3x1 + 0.2x3)/(10.0)

mrdefinido = 0.02 #erro para parada da iteração ou 'tolerancia'
k = 0 #numero de iteracoes
mr = 1#definicao de um valor inicial para mr antes de atualizá-lo na 2 iteracao

while abs(mr) > mrdefinido:
    Vxant = Vxnovo
    Vxnovo = np.zeros(len(Vxant))

    for i in range (len(Vxnovo)):
        for j in range (len(Vxnovo)):
                if(i != j):
                    Vxnovo[i] += (Vxant[j] * (-(C[i][j]))/(CDiag[i]))
        Vxnovo[i] += (g[i]) / CDiag[i] #somando a parte das constantes independentes (divididas pelo valor da diagonal)
    if(k > 1):
        mr = erro(Vxant,Vxnovo)
        print(mr)
    k+=1

print(Vxnovo)