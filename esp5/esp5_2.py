from functions5 import *
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt

'''
ampiezza 1.48V 
dt       6.25ms
f        160Hz
'''
#A = 1.65/4#V
A = 1.48/4#V
f = 160#Hz
T = 1/f
w_s = 2*pi/T

t,V = data_from_csv('dati/scope_3',False)
t -= T/4
#V += 0.1/4

def V_mod(t, mu):
	return A*( 2*np.cos(w_s*t) - (mu/(4*w_s))*np.sin(3*w_s*t) )

fig1 = plt.figure()
ax0 = fig1.subplots()
ax0.plot(t,V, 'b-', label=r'$V$', linewidth=1)

popt, pcov = curve_fit(V_mod, t, V)

ax0.plot(t, V_mod(t, 0), 'k-', label=r'$\mu=0$', linewidth=1)
ax0.plot(t, V_mod(t, *popt), 'r-', label=r'Fit: $\mu=%5.2f$' % tuple(popt), linewidth=1)

ax0.set_xlabel('t [s]')
ax0.set_ylabel('V [V]')

ax0.minorticks_on()
ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')
ax0.legend()


fig1.show()