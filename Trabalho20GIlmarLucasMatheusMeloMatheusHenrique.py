# TRABALHO 20
# Gilmar dos Reis Júnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva Honório
# Matheus Henrique Maia Ramos

#Método de Euler
#t [0,4]

import numpy as np

tmax = 4
h = 0.25
y0 = 1

vet = np.array([])

def deriv(y, t): #função da derivada
    
    return (y*(t**2)) - (1.1*y)

def fn_incremento(yi, ti): #funcao de incremento
    
    return yi + deriv(yi, ti) * h

vet = np.append(vet, y0) #setando o vetor de valores com a condição inicial

for i in range(tmax):
    
    vet = np.append(vet, fn_incremento(vet[i], i))
    #iterando os próximos valores da função indo de 0 ate tmax
    #a cada iteração, ela fica salva na posição anterior, sendo reutilizada na proxima
    
print(vet)#printando o vetor final com a solução do problema em termos de valores
#esses valores desenham uma curva que se colocados num gráfico, 
#dão a resposta final graficamente
    
    
    
    


                                                                                                                            