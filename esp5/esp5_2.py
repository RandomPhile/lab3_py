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
f = 160#Hz
T = 1/f
w_s = 2*pi/T
print(w_s)
t,V = data_from_csv('dati/scope_3',False)

def V_fit0(t, A, phi_A, C, w_s):
	return A * np.cos(1000*w_s*t + phi_A) + C

def V_fit(t, A, phi_A, B, phi_B, C):
	return A * np.cos(w_s*t + phi_A) + B * np.cos(3*w_s*t + phi_B) + C

fig1 = plt.figure()
ax0 = fig1.subplots()

fit_out0, c0 = curve_fit(V_fit0, t, V)
fit_out, c = curve_fit(V_fit, t, V)

print(fit_out0,fit_out)

V_mod0 = V_fit0(t, *fit_out0)
V_mod = V_fit(t, *fit_out)
ax0.plot(t,V, 'b-', label=r'$V$', linewidth=1)
ax0.plot(t, V_mod0, 'r-', label=r'Fit', linewidth=1)
ax0.plot(t, (V-V_mod0)*100, 'g-', label=r'residui*50', linewidth=1)


# ax0.plot(t, V_mod_A(t, A_fit), 'k-', label=r'$\mu=0$', linewidth=1)
# #ax0.plot(t, V_mod(t, *popt), 'r-', label=r'Fit: $\mu=%5.2f$' % tuple(popt), linewidth=1)

ax0.set_xlabel('t [s]')
ax0.set_ylabel('V [V]')

grid(ax0)
ax0.legend()

fig1.show()