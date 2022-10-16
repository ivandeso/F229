from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
var =[47.32278973, 120.11346824, -162.31862203, -7.93263284, 23.20380742, 2.16662888, -4.20419762, 1.35221002]
v = [-0.97, 0.15, 0.48, 0.75, 0.77]
dTeq = 0.05
dT2 = 2.32
Teq = []
for i in range(len(v)):
    k= (var[0]+var[1]*v[i]+var[2]*(v[i]**2)+var[3]*(v[i]**3)+var[4]*(v[i]**4))/(1+var[5]*v[i]+var[6]*(v[i]**2)+var[7]*(v[i]**3))
    Teq.append(k)
m1 = 100
m2 = [50, 100, 150, 200, 250]
vt2 = 2.32
T2 = (var[0]+var[1]*vt2+var[2]*(vt2**2)+var[3]*(vt2**3)+var[4]*(vt2**4))/(1+var[5]*vt2+var[6]*(vt2**2)+var[7]*(vt2**3))
vtamb = -1.12
Tamb = (var[0]+var[1]*vtamb+var[2]*(vtamb**2)+var[3]*(vtamb**3)+var[4]*(vtamb**4))/(1+var[5]*vtamb+var[6]*(vtamb**2)+var[7]*(vtamb**3))
print(f"Tamb = {Tamb}")
print(f"Vt2 = {T2}")
deltaT = []
for i in range(len(v)):
    d = (Teq[i] - T2)
    deltaT.append(d)
p = []
for i in range(len(v)):
    j = m2[i]*deltaT[i]
    p.append(j)
q = []
for i in range(len(v)):
    g = Teq[i]
    q.append(g)
print(p)
print(q)
n =[30, 30, 30, 30, 30]
m = [0.5, 0.5, 0.5, 0.5, 0.5]
dx = np.array(n)
dy = np.array(m)
x, y = p, q
plt.scatter(x, y, zorder=10)
plt.xlabel('m2.(Teq-T2) (g.ºC)')
plt.ylabel('Teq (ºC)')
from scipy import odr
data = odr.RealData(x, y)
odreg = odr.ODR(data, odr.models.unilinear)
odreg.set_job(fit_type=2)
ans = odreg.run()
a, b = ans.beta
da, db = ans.sd_beta
print(f'coef. angular = ({a}+-{da})')
print(f'coef. linear = ({b}+-{db})')
rotulo = "regressão linear"
X = np.linspace(min(x), max(x), num=200)
Y = a * X + b
plt.plot(X, Y, color='brown', alpha=0.4, label=rotulo)
plt.errorbar(x, y, yerr=dy, xerr = dx,  fmt='.k');
plt.savefig("C:\\Users\\sonic\\OneDrive\\Documentos\\F229\\Exp04\\python\\calorímetro\\graficommq")
C = -1/a - m1
print(f"Calor específico do calorimetro {C}")