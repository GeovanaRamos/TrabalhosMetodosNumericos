import numpy as np
from math import *
import matplotlib.pyplot as plt

# pontos de sin(wt)
ys = [ 0.2493938 ,  0.72091586,  1.08935177,  0.82557285,  0.15184373,
      -0.55819513, -0.84832015, -1.13075724, -0.66132559, -0.37482053,
       0.49910671,  0.99533713,  0.97493417,  0.56770796, -0.59740919,
      -0.76333201, -1.05362856, -0.8085086 , -0.32029816,  0.4021104 ]


ts = [   0.        ,    5.26315789,   10.52631579,   15.78947368,
        21.05263158,   26.31578947,   31.57894737,   36.84210526,
        42.10526316,   47.36842105,   52.63157895,   57.89473684,
        63.15789474,   68.42105263,   73.68421053,   78.94736842,
        84.21052632,   89.47368421,   94.73684211,  100.        ]






# função EQ(w)
def eq(w):
    soma = 0;
    for i in range(20):
        soma+= (sin(w*ts[i]) - ys[i])**2

    return soma



# gerando gráfico de EQ(w) para achar intervalo
# eq_lista = []
# for i in range(20):
#     w = i/100
#     eq_lista.append(eq(w))
# w = np.arange(0.0, 0.2, 0.01)
# plt.plot(w,eq_lista)
# plt.show()
# o mínimo esta, com certeza, entre 0.10 e 0.15


# calculando mínimo
for i in range(5):
    wtol=1e-3
    w1, w2 = 0, 0.2

    wa, wb = w1 + (w2 - w1)/3, w1 + (w2 - w1) * 2 / 3
    eqa, eqb = eq(wa), eq(wb)

    if eqa > eqb:
        w1 = wa
    else:
        w2 = wb

    if eqa < eqb:
        print("%.4f" %wa)
    else:
        print("%.4f" %wb)
