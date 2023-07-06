# TRABALHO 19
# Gilmar dos Reis JÃºnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva HonÃ³rio
# Matheus Henrique Maia Ramos

# Regra 3/8 de simpson

import numpy as np

a = 1  # limite inferior
b = 3  # limite superior
n = 20  # número de intervalos
somatorio1 = 0
somatorio2 = 0
intervalos = np.linspace(a, b, n)  # vetor de n intervalos


def f(x):

    return (np.exp(x/2))/2  # funcao que iremos realizar a integral


for i in range(1, len(intervalos)-1):

    if (i % 3 != 0):
        # somatorio dos f(x) onde x não é múltiplo de três
        somatorio1 = somatorio1+f(intervalos[i])
    else:
        # somatorio dos f(x) onde x é múltilo de três
        somatorio2 = somatorio2+f(intervalos[i])

I = 3*(b-a)*(f(intervalos[0])+3*somatorio1 +
             2*somatorio2+f(intervalos[n-1]))/(8*n)  # formula da regra 3/8 de simpson que resulta em um valor aproximado ao da integral

print(I)
