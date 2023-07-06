# TRABALHO 23
# Gilmar dos Reis JÃºnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva HonÃ³rio
# Matheus Henrique Maia Ramos

# Método do Ponto Médio
# t [0,4]

import numpy as np

tmax = 4  # intervalo varia de 0 ate tmax
h = 0.25  # tamanho do passo
y0 = 1  # condicao inicial para y quando t = 0

vet = np.array([])


def deriv(y, t):  # funcao da derivada - equação que queremos resolver

    return (y*(t**2)) - (1.1*y)  # 4*np.exp(0.8*t)-0.5*y


def fn_incremento(y, yi, ti, i):  # funcao de predicao

    if (i % 2 == 0):
        return y + deriv(yi, ti) * h/2  # quando t NAO for inteiro
    else:
        return y + deriv(yi, ti) * h  # quando t for inteiro


vet = np.append(vet, y0)  # setando o vetor de valores com a condicao inicial

j = 0
k = 0

for i in range(tmax*2):

    if (i % 2 == 0):
        y = vet[i]

    vet = np.append(vet, fn_incremento(y, vet[i], j, i))

    j = 0.5+j

for t in range((tmax*2)+1):
    if (t % 2 == 0):
        print(t/2, ": ", vet[t])
