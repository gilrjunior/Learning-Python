# TRABALHO 17
# Gilmar dos Reis JÃºnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva HonÃ³rio
# Matheus Henrique Maia Ramos

# Regra do Trapézio

import numpy as np

a = 1 #limite inferior
b = 3 #limite superior
n = 20 #número de intervalos
somatorio = 0
intervalos = np.linspace(a, b, n) #vetor de 20 intervalos


def f(x):

    return (np.exp(x/2))/2 #funcao que iremos realizar a integral


for i in range(1, len(intervalos)-1):

    somatorio = somatorio+f(intervalos[i]) #calculo do somatorio envolvido na formula

I = (b-a)*(f(intervalos[0])+2*somatorio+f(intervalos[n-1]))/(2*n) #formula da regra do trapézio que resulta em um valor aproximado ao da integral

print(I)
