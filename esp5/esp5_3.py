import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt

from tabulate import tabulate
from texttable import Texttable
import latextable

R, C = 100e3, 100e-9
tau = R*C

R1 = np.array([1e3, 10e3, 10e3])
R2 = np.array([10e3, 10e3, 1e3 ])

r = R1/(R2+R1)
print(r)

logr = np.log((1+r)/(1-r))
r_mod = np.linspace(min(r), max(r))
print(r_mod)
logr_mod = np.log((1+r_mod)/(1-r_mod))
T_mod = 2*tau*logr_mod

t_discesa = np.array([28.9, 26.2, 29])*1e-6

T   = np.array([3.81, 22.1, 61.1])*1e-3
f = 2*pi/T
Vpp = np.array([21.19, 21.4, 20.94])

fig, ax0 = plt.subplots()
#ax1 = ax0.twinx()

ax0.plot(r, T, 'r*', label='periodo')
ax0.plot(r_mod, T_mod, 'b-', label='modello')

f = lambda r: np.log((1+r)/(1-r))
f_inverse = lambda t: (np.exp(t)-1)/(np.exp(t)+1)

ax0.set_xscale('function', functions=(f, f_inverse))
x_labels = np.linspace(0.1, 0.9, 10)
print(x_labels)
ax0.set_xticks(x_labels)
ax0.set_xticklabels(x_labels)

ax0.minorticks_on()
ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')

ax0.legend()

plt.show()


rows = [['R1','R2','r','f']]
for i in [0,1,2]:
	rows.append([R1[i],R2[i],r[i],f[i]])


table = Texttable()
table.set_cols_align(['c'] * 4)
table.set_deco(Texttable.HEADER | Texttable.VLINES)
table.add_rows(rows)

print(tabulate(rows, headers='firstrow'))

print(tabulate(rows, headers='firstrow', tablefmt='latex'))