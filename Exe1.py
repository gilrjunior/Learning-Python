import matplotlib.pyplot as plt
import numpy as np

print("Entre com os parametros abaixo")
m = float(input("Massa do saltador de bungee jump em kg: "))
t = int(input("Digite o tempo final: "))
t2 = int(input("Digite a quantidade de intervalos: "))
c = float(input("Informe o coeficiente de arrasto em kg/m: "))
g = 9.8

vtempo = np.linspace(0, t, t2)
tam = len(vtempo)

v = np.zeros(tam)

for i in range (tam):
    v[i] = (np.sqrt(g*m/c))*np.tanh(np.sqrt(g*c/m)*vtempo[i])
    print("Tempo:           ", vtempo[i], "  Velocidade:      ", v[i])

plt.plot(vtempo, v)

plt.title("Velocidade do Saltador de bungee jump")
plt.xlabel("tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.show()
