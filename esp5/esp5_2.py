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
#A = 1.635/2#V
A = 1.48/2#V
f = 160.4#Hz
T = 1/f
w_s = 2*pi/T

t,V = data_from_csv('dati/scope_3',False)
t -= T/4
V += 0.1/4

def V_mod_A(t, A):
	return A*np.cos(w_s*t)

A_fit,c = curve_fit(V_mod_A, t, V)
print(A_fit[0]*2)

def V_mod(t, mu):
	return A*( np.cos(w_s*t) - (mu/(4*w_s))*np.sin(3*w_s*t) )

fig1 = plt.figure()
ax0 = fig1.subplots()
ax0.plot(t,V, 'b-', label=r'$V$', linewidth=1)

popt, pcov = curve_fit(V_mod, t, V)

V_mod0 = V_mod_A(t, A_fit)
V_mod1 = V_mod(t, popt[0])

ax0.plot(t, (V-V_mod0)*100, 'k-', label=r'$\mu=0$', linewidth=1)

ax0.plot(t, V_mod_A(t, A_fit), 'k-', label=r'$\mu=0$', linewidth=1)
#ax0.plot(t, V_mod(t, *popt), 'r-', label=r'Fit: $\mu=%5.2f$' % tuple(popt), linewidth=1)

ax0.set_xlabel('t [s]')
ax0.set_ylabel('V [V]')

grid(ax0)
ax0.legend()

fig1.show()