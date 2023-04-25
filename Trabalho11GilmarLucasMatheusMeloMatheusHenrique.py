#TRABALHO 11
#Gilmar dos Reis Júnior
#Lucas Moragas Melo Oliveira
#Matheus de Melo Silva Honório
#Matheus Henrique Maia Ramos

import numpy as np
import matplotlib.pyplot as plt

def potencia(a,b,x):
    
    return a*(x**b)

def exponencial(a,b,x):
    
    return a*np.exp(b*x)

def saturacao(a,b,x):
    
    return a*(x/(b+x))
    
Vx = np.array([1980, 1985, 1990, 1993, 1997, 2000, 2006])
Vy = np.array([8300, 9900, 10400, 13200, 13600, 13700, 14600])

VxP = np.array([np.log10(1980), np.log10(1985), np.log10(1990), np.log10(1993), np.log10(1997), np.log10(2000), np.log10(2006)])
VyP = np.array([np.log10(8300), np.log10(9900), np.log10(10400), np.log10(13200), np.log10(13600), np.log10(13700), np.log10(14600)])

VxE = np.array([1980, 1985, 1990, 1993, 1997, 2000, 2006])
VyE = np.array([np.log(8300), np.log(9900), np.log(10400), np.log(13200), np.log(13600), np.log(13700), np.log(14600)])

VxS = np.array([1/1980, 1/1985, 1/1990, 1/1993, 1/1997, 1/2000, 1/2006])
VyS = np.array([1/8300, 1/9900, 1/10400, 1/13200, 1/13600, 1/13700, 1/14600])

SvxP = VxP.sum()


SvyP = VyP.sum()

SvxE = VxE.sum()
SvyE = VyE.sum()
SvxS = VxS.sum()
SvyS = VyS.sum()

n = len(VxP)

SxyP = Sx2P = SxyE = Sx2E = SxyS = Sx2S = 0

for i in range(len(VxP)):
    
    SxyP += (VxP[i] * VyP[i])
    Sx2P += (VxP[i]**2)
    SxyE += (VxE[i] * VyE[i])
    Sx2E += (VxE[i]**2)
    SxyS += (VxS[i] * VyS[i])
    Sx2S += (VxS[i]**2)


a1P = (n*(SxyP) - (SvxP * SvyP))/(n*Sx2P - SvxP**2)
a0P = (SvyP/len(VyP)) - a1P*(SvxP/len(VxP))

a1E = (n*(SxyE) - (SvxE * SvyE))/(n*Sx2E - SvxE**2)
a0E = (SvyE/len(VyE)) - a1E*(SvxE/len(VxE))

a1S = (n*(SxyS) - (SvxS * SvyS))/(n*Sx2S - SvxS**2)
a0S = (SvyS/len(VyS)) - a1S*(SvxS/len(VxS))

alfaP = 10**a0P
BetaP = a1P

alfaE = np.exp(a0E)
BetaE = a1E


alfaS = 1/a0S
BetaS = a1S * alfaS


print("Potência : alfa: ", alfaP, "beta: ", BetaP)
print("Exponencial : alfa: ", alfaE, "beta: ", BetaE)
print("Saturação : alfa: ", alfaS, "beta: ", BetaS)

plt.subplot(2,2,1)
plt.plot(Vx, Vy)
plt.subplot(2,2,2)
plt.plot(Vx, potencia(alfaP, BetaP, Vx))
plt.subplot(2,2,3)
plt.plot(Vx, exponencial(alfaE, BetaE, Vx))
plt.subplot(2,2,4)
plt.plot(Vx, saturacao(alfaS, BetaS, Vx))

plt.show()

