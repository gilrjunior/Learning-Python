# -*- coding: utf-8 -*-

#TRABALHO 4
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np

x1 = x2 = x3 = 2.5

Vx1 = ant1 = 0
Vx2 = ant2 = 0
Vx3 = ant3 = 0
i = 0
k = 0

for i in range (30):
    
    Vx1 = (((x1**4)/2)+(x1**3)+5)/17.7
    Vx2 = (-((x2**4)/2)-17.7*x2-5)**(1/3)
    Vx3 = (2*(-(x3**3)+17.7*x3-5))**(1/4)
    
    ant1 = x1
    ant2 = x2
    ant3 = x3
    
    x1 = Vx1
    x2 = Vx2
    x3 = Vx3
    
if(not np.isnan(Vx1) and Vx1 - ant1 <= 0.00005 ):
    
    print("Existe uma raiz em: ", round(Vx1, 3))
    
if(not np.isnan(Vx2) and Vx2 - ant2 <= 0.00005):
    
    print("Existe uma raiz em: ", round(Vx2, 3))

if(not np.isnan(Vx3) and Vx3 - ant3 <= 0.00005):
    
    print("Existe uma raiz em: ", round(Vx3, 3))
        

    
    
    
