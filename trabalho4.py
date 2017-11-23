#Geovana Ramos Sousa Silva
#160122180

import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.special import erf


def f(t):
    return  np.exp(-t**2)


def simpson(x):

    h = x/10
    t = np.arange(0, x, h)

    res = np.sum(h/6 * (f(t) + 4 * f(t + h/2) + f(t + h)))

    return res  * (2/ sqrt(pi))

def gaussiana(x):


    h = x/10
    t = np.arange(0, x, h)

    u = np.array([0,
        1/3*sqrt(5-2*sqrt(10/7)),
        -1/3*sqrt(5-2*sqrt(10/7)),
        1/3*sqrt(5+2*sqrt(10/7)),
        -1/3*sqrt(5+2*sqrt(10/7))
    ])

    w = np.array([128/225,
        (322 + 13 * sqrt(70))/900,
        (322 + 13 * sqrt(70))/900,
        (322 - 13 * sqrt(70))/900,
        (322 - 13 * sqrt(70))/900
    ])

    r0 = np.sum(
        w[0] * f(t + h/2 *(1 +u[0] )) +
        w[1] * f(t + h/2 *(1 +u[1] )) +
        w[2] * f(t + h/2 *(1 +u[2] )) +
        w[3] * f(t + h/2 *(1 +u[3] )) +
        w[4] * f(t + h/2 *(1 +u[4] ))
    )
    res = r0 * h/2

    return res * (2/ sqrt(pi))

print (simpson(1) )
print (gaussiana(1))
print(erf(1))
