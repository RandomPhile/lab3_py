from functions5 import *
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt

'''
Saw : 1/100 Hz, 3Vpp
'''

R = 100#Ohm

def I_func(V, R_L, alpha):
	return (V)/(R_L * (1 + alpha * V**2))

t,Vin,Vout = data_from_csv('dati/scope_1')

fig1 = plt.figure()
ax0 = fig1.subplots()
ax0.plot(t,Vin, 'b-', label=r'$V_{in}$', linewidth=1)
ax0.plot(t,Vout, 'g-', label=r'$V_{out}$', linewidth=1)
ax0.set_xlabel('t [s]')
ax0.set_ylabel('V [V]')

ax0.minorticks_on()
ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')
ax0.legend()

I = (Vin/R)
V = Vout/2
popt, pcov = curve_fit(I_func, V, I)

fig2 = plt.figure()
ax0 = fig2.subplots()
ax0.plot(V,I*1e3, 'b-', label='Curva I-V misurata', linewidth=1)
ax0.plot(V, I_func(V, *popt)*1e3, 'r-', label=r'Fit: $R_L=%5.2f\ \Omega$, $\alpha=%5.2f V^{-2}$' % tuple(popt), linewidth=1)
ax0.set_xlabel('V [V]')
ax0.set_ylabel('I [mA]')

ax0.minorticks_on()
ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')
ax0.legend()
save = 0
fig1.tight_layout()
fig2.tight_layout()
if save:
	fig1.savefig('fig/V_t.eps', format='eps')
	fig2.savefig('fig/I_V.eps', format='eps')
plt.show()