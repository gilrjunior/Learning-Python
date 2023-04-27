
#TRABALHO 5
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np

def f(a):
    return -(a**4)/2 - (a**3) + (17.7*a) - 5

x1 = -8
delta = 10**(-6)
while True:
    x2 = x1 - (delta*x1*f(x1))/(f(x1+delta*x1)-f(x1))
    x1 = x2
    print('Valor da variável é: {}'.format(x2))
    print('Valor da funcao é: {}\n'.format(f(x2)))
    if(abs(f(x2)) < 0.01):
        break

print(x2)


