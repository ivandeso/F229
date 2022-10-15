import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

dados = pd.read_csv('C:\\Users\\sonic\\OneDrive\\Documentos\\F229\\Exp04\\python\\t3rmopar.csv', decimal=",")
print(dados)
x =dados["X"].values
y1 = dados["Y"].values
def Y(x,p0, p1, p2, p3, p4, q1, q2, q3):
    return ((p0 + p1*x + p2*(x**2)+p3*(x**3)+p4*(x**4))/(1+q1*x+q2*(x**2)+q3*(x**3)))
guess = [1, 1, 1, 1, 1, 1, 0, 0]
c, cov = curve_fit(Y,x,y1,guess)
print(c)
y=[]
for m in range(len(dados["X"])):
    y.append(0)
for i in range(len(dados["X"])):
    y[i] = Y(x[i], c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7])
plt.xlabel('DDP (v)')
plt.ylabel('Temperatura (ºC)')
plt.scatter(dados["X"], dados["Y"])
plt.plot(dados["X"], y, "r.")
plt.savefig('C:\\Users\\sonic\\OneDrive\\Documentos\\F229\\Exp04\\python\\grafico5.png', dpi=200)


