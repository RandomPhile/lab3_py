import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
from functions5 import *
from regressione_lineare import *
from tabulate import tabulate
from texttable import Texttable
import latextable

R, C = 100e3, 100e-9
tau = R*C

R1 = np.array([1e3, 10e3, 10e3])
R2 = np.array([10e3, 10e3, 1e3 ])

r = R1/R2
print(r)
logr = np.log(1+2*r)
r_mod = np.linspace(min(r), max(r))

logr_mod = np.log(1+2*r_mod)
T_mod = 2*tau*logr_mod

t_discesa = np.array([28.9, 26.2, 29])*1e-6

T   = np.array([3.81, 22.1, 61.1])*1e-3
f = 1/T
w = 2*pi*f
Vpp = np.array([21.19, 21.4, 20.94])

fig, ax0 = plt.subplots()
#ax1 = ax0.twinx()

ax0.plot(r, T, 'r*', label=r'Misure per $r = [0.1, 1, 10]$')
ax0.plot(r_mod, T_mod, 'b-', label=r'Modello $T(r)=2\ RC\ \ln(1+2r)$')


#ax0.plot(logr, T*1e3, 'r*', label=r'Misure per $r = [0.1, 1, 10]$')
#ax0.plot(logr_mod, T_mod*1e3, 'b-', label=r'Modello $T(r)=2\ RC\ \ln(1+2r)$')

f = lambda r: np.log(1+2*r)
f_inverse = lambda t: (np.exp(t)-1)/2

ax0.set_xscale('function', functions=(f, f_inverse))
#x_labels = np.linspace(0.1, 0.9, 10)
#print(x_labels)
ax0.set_xticks([0.1, 1, 2, 4, 6, 8,10])

#ax0.set_xticklabels(x_labels)

#CALCOLO LA PENDENZA m
'''
x,y = logr,T
x_mean = np.mean(x)
y_mean = np.mean(y)
m_num = ((x - x_mean) * (y - y_mean)).sum()
m_den = ((x - x_mean)**2).sum()
m = m_num / m_den

print(m/2, tau)
'''
ax0.set_xlabel(r'$r$'); ax0.set_ylabel('T [ms]')

grid(ax0); ax0.legend()

#fig.savefig('fig/T_r2.eps', format='eps')
plt.show()


rows = [['R1','R2','r','f']]
for i in [0,1,2]:
	rows.append([R1[i],R2[i],r[i],f[i]])


table = Texttable()
table.set_cols_align(['c'] * 4)
table.set_deco(Texttable.HEADER | Texttable.VLINES)
table.add_rows(rows)

#print(tabulate(rows, headers='firstrow'))

#print(tabulate(rows, headers='firstrow', tablefmt='latex'))