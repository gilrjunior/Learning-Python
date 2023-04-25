# -*- coding: utf-8 -*-

#TRABALHO 6
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import math as m

def f(x):
    
    return 2*m.sin(x/5)+3

def erro(x, xant):

    return abs((x-xant)/x)

def next_x(x1, x2, x3):

    return x2 - (1/2)*(((x2-x1)**2) * (f(x2) - f(x3)) - ((x2 - x3)**2)*(f(x2) - f(x1)))/((x2-x1) * (f(x2) - f(x3)) - (x2 - x3)*(f(x2) - f(x1)))


x1 = -2
x2 = 3
x3 = 8
x4 = next_x(x1,x2,x3)
x4_ant = 0
eMax = 10**(-8)

while(erro(x4, x4_ant) > eMax):

    if(x4 > x2):

        x1 = x2
    
    else:

        x3 = x2

    x2 = x4
    x4_ant = x4
    x4 = next_x(x1,x2,x3)

print("Máximo em x= ", round(x4, 3))
