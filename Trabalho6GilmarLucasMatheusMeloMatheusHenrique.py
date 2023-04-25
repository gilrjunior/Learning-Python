# -*- coding: utf-8 -*-

#TRABALHO 6
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import math as m

def razao_aurea(xl, xu):
    
    return (((1+m.sqrt(5))/2) - 1)*(xu-xl)

def f(x):
    
    return 2*m.sin(x/5)+3

def erro(xl, xu, xopt):
    
    return ((2-0)*abs((((xu-xl)/xopt))*100))

xl = -1
xu = 15
eMax = 10**(-8)

xopt = xl if f(xl) > f(xu) else xu


while(erro(xl,xu,xopt) > eMax):

      x1 = xl + razao_aurea(xl, xu)
      x2 = xu - razao_aurea(xl, xu)
      
      if(f(x1) > f(x2)): #aproximação está em x1
          
          if(x1 > x2):
              
              xl = x2
              
          else:
              
              xu = x2
          
      else: #aproximação está em x2
      
          if(x2 > x1):
              
              xl = x1
              
          else:
              
              xu = x1
    
      xopt = x1 if f(x1) > f(x2) else x2
               
              
print("Máximo: ",round(xopt, 4))              
        