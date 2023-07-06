# TRABALHO 22
# Gilmar dos Reis Júnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva Honório
# Matheus Henrique Maia Ramos

#Método de Heun com itera��es
#t [0,4]

import numpy as np

tmax = 4
h = 0.25
y0 = 1

vet = np.array([])

def deriv(y, t): #função da derivada
    
    return  (y*(t**2)) - (1.1*y) #4*np.exp(0.8*t)-0.5*y

def fn_correcao(yi, ti, yprox, tprox): #função corretora
    
    return yi + (deriv(yi, ti) + deriv(yprox , tprox))/2 * h


def fn_incremento(yi, ti): #funcao de predição
    
    return yi + deriv(yi, ti) * h

vet = np.append(vet, y0) #setando o vetor de valores com a condição inicial

for i in range(tmax):
    
    tprox = i+1
    yprox = fn_incremento(vet[i], i)
    
    for k in range(5):
        
        yprox = fn_correcao(vet[i], i, yprox, tprox)
        #iterando os próximos valores da função indo de 0 ate tmax
        #a cada iteração nos armazenamos o valor corrigido 1 vez, (SEM ITERAÇÃO)
    
    vet = np.append(vet, yprox)
    
print(vet)

