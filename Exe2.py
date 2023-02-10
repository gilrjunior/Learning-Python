import matplotlib.pyplot as plt
import numpy as np

print("Entre com os parametros abaixo")
m = float(input("Massa do saltador de bungee jumping em kg: "))
t = int(input("Digite o tempo final: "))
t2 = int(input("Digite a quantidade de intervalos: "))
c = float(input("Informe o coeficiente de arrasto em kg/m: "))
g = 9.8

vtempo = np.linspace(0, t, t2)
tam = len(vtempo)

v = np.zeros(tam)

vanterior = 0
tanterior = 0

print("Tempo:                Velocidade (m/s)")

for i in range(tam):
    if(i==0):
        v[i] = 0
    
    if(i > 0):
        v[i] = v[i-1]+(g-(c/m)*(v[i-1]**2))*(vtempo[i]-vtempo[i-1])
    
    vtempoaux = round(vtempo[i], 4)
    vaux = round(v[i], 4)
    print(vtempoaux,"      ",vaux)
    vanterior = v[i]
    tanterior = i
    
plt.plot(vtempo, v)

plt.title("Velocidade do Saltador de bungee jump")
plt.xlabel("tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.show()