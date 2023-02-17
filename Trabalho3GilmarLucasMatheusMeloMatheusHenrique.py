# -*- coding: utf-8 -*-

#TRABALHO 3
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np

Xl = -2
Xu = 5
Xr = Xu - ((2*np.exp(Xu)-3)*(Xl-Xu))/((2*np.exp(Xl)-3)-2*np.exp(Xu)-3)

while(abs(2*np.exp(Xr)-3) > 0.00001):
    
    if(((2*np.exp(Xr)-3) * (2*np.exp(Xu)-3)) < 0):
        Xl = Xr

    if(((2*np.exp(Xr)-3) * (2*np.exp(Xl)-3)) < 0):
        Xu = Xr
    
    Xr = Xu - ((2*np.exp(Xu)-3)*(Xl-Xu))/((2*np.exp(Xl)-3)-2*np.exp(Xu)-3)

print("A raiz está entre os pontos: ", round(Xl, 5), " e ", round(Xu, 5))