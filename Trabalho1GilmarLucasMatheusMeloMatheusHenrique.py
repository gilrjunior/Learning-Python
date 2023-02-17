# -*- coding: utf-8 -*-

#TRABALHO 1
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np

intervalos = np.linspace(-2, 5, 100)

for i in range (1,len(intervalos)):
        
    if(((2*np.exp(intervalos[i])-3) * (2*np.exp(intervalos[i-1])-3)) < 0):
        print("Existe uma raiz entre esse intervalo ", round(intervalos[i-1], 4), " e ", round(intervalos[i], 4))

    

        
        