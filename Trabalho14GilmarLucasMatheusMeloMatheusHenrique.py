# TRABALHO 14
# Gilmar dos Reis JÃºnior
# Lucas Moragas Melo Oliveira
# Matheus de Melo Silva HonÃ³rio
# Matheus Henrique Maia Ramos

import numpy as np


def divisao_de_diferencas(x, y):  # onde as divisões
    n = len(y)
    # cria-se uma matriz para os coeficientes calculados
    # se olhar o material de interpolação polinomial, slide 17, tem uma tabela com valores de f(x) - primeira coluna
    # e valores dos coeficientes a serem calculados
    coef = np.zeros([n, n])
    # a primeira coluna dessa matriz é composta apenas dos valores de y que são dados no enunciado
    coef[:, 0] = y  # utilizando os dois pontos pra cortar o vetor
    # todas as linhas da coluna 0 recebem os valores de y

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])

    return coef


def pol_newton(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n+1):
        p = coef[n-k] + (x - x_data[n-k])*p
    return p


# se o usuario passar valores em forma de colchete
x, y = eval(input("Entre duas listas (valores de x e de y) "))
# exemplo [1,2,3], [4,5,6]
# x receberá [1,2,3] e y receberá [4,5,6]

x = np.array(x)  # Convertendo a lista recebida pra array da biblioteca numpy
y = np.array(y)  # Convertendo a lista recebida pra array da biblioteca numpy

# utilizando a mesma ideia de corte, pegamos apenas a primeira
coeficientes = divisao_de_diferencas(x, y)[0, :]
# linha da matriz de coeficientes só que no retorno da funcao
print("Coeficientes: ", coeficientes)

valorestimado = pol_newton(coeficientes, x, 21.8)  # estimando o valor de 21.8
print("Estimando f(21.8): ", valorestimado)
