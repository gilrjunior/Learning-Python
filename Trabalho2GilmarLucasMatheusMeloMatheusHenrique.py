# -*- coding: utf-8 -*-

#TRABALHO 2
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np

intervalo1 = -2
intervalo2 = 5
Vmedio = (intervalo1+intervalo2)/2
i = 0

while(abs(2*np.exp(Vmedio)-3) > 0.00001):
    
    if(((2*np.exp(intervalo1)-3) * (2*np.exp(Vmedio)-3)) < 0):
    
        intervalo2 = Vmedio
        
    
    if(((2*np.exp(intervalo2)-3) * (2*np.exp(Vmedio)-3)) < 0):
    
        intervalo1 = Vmedio

    Vmedio = (intervalo1+intervalo2)/2
        
print("A raiz está entre os pontos: ", round(intervalo1, 5), " e ", round(intervalo2, 5))


