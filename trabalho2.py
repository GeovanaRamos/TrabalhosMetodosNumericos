#Geovana Ramos Sousa SIlva
# 16/0122180

import numpy as np
import matplotlib.pyplot as plt
from math import *


def f(w, x):
    return w*exp(w) - x

def resolver_w(x):
    A = 0
    B = x
    while True:
        C = (B + A) / 2.0

        if (f(A,x) * f(C,x)) < 0:
            B = C
        elif abs(f(C,x)) < 0.0005:
            return C
            break
        else:
            A = C



valor = float(input("Digite o valor de x: "))
while True:
    if (valor<0):
        print ('Insira um valor positivo')
        valor = float(input())
    else:
        break

resultado = resolver_w(valor)
#print (resultado)
