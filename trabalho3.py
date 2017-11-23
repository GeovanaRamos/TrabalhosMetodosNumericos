import numpy as np
import matplotlib.pyplot as plt
from math import *

h = 1e-3
x = np.arange(0,10,h)
b = -2 - h**2


M = np.array([[b, 1, 0, 0, 0, 0, 0],
              [1, b, 1, 0, 0, 0, 0],
              [0, 1, b, 1, 0, 0, 0],
              [0, 0, 1, b, 1, 0, 0],
              [0, 0, 0, 1, b, 1, 0],
              [0, 0, 0, 0, 1, b, 1],
              [0, 0, 0, 0, 0, 1, b]])

y0 = 0
yf = 10
v = np.array([sqrt(x[0]) - y0, sqrt(x[1]), sqrt(x[2]), sqrt(x[3]), sqrt(x[4]), sqrt(x[5]), sqrt(x[6]) - yf])


# Gerar matriz aumentada
G = np.append(M, v, 1).astype(float)

# Aplicar Eliminação de Gauss
n = len(G[:, 0])
for i in range(n - 1):
    if G[i, i] == 0:
        print (0)
        break
    for j in range(i + 1, n):
        G[j] -= G[i] * G[j, i] / G[i, i]

# Continuar com o Método de Gauss-Jordan
n = len(G[:, 0])
for i in range(n - 1, -1, -1):
    G[i] /= G[i, i]
    for j in range(i):
        G[j] -= G[i] * G[j, i]

#Mostrar resultados
print (G[:, n:])
