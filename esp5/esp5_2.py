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
R, C = 100e3, 10e-9
print(1/(2*pi*R*C))
t,V_exp = data_from_csv('dati/scope_3',False)

######Fit solo w_s

def V_(t, A, phi_A, w_s, C):
	return A * np.cos(1000*w_s*t + phi_A) + C

######Fit anche 3w_s

def V_2(t, A, phi_A, w_s, C, mu, phi_B):
	return A * np.cos(1000*w_s*t + phi_A) - (mu*10/(4*w_s)) * np.sin(3*w_s*t + phi_B) + C


fig = plt.figure(); ax0,ax1 = fig.subplots(2,1)

fit, c = curve_fit(V_, t, V_exp)
fit2, c = curve_fit(V_2, t, V_exp)

def V_3(t, A, phi_A, w_s, C):
	return A * np.cos(1000*3*w_s*t + phi_A) + C


V = V_(t, *fit)
V2 = V_2(t, *fit2)

fit3, c = curve_fit(V_3, t, V_exp-V)
V3 = V_3(t, *fit3)
print('A             phi_A       w_s        C           mu           phi_B')
print(fit)
print(fit2)
print(fit3)




ax0.plot(t, V, 'r-', label=r'Fit senza $3w_s$', linewidth=1)
ax0.plot(t, V2, 'g-', label=r'Fit con $3w_s$', linewidth=1)
ax0.plot(t, V_exp, 'b-', label=r'Segnale misurato', linewidth=1)
ax1.plot(t, (V_exp-V)*1000, 'r-', label=r'Fit', linewidth=1)
ax1.plot(t, (V_exp-V)*1000, 'g-', label=r'Fit', linewidth=1)
ax1.plot(t, V3*1000, 'k-', label=r'Fit', linewidth=1.5)

ax2 = plt.axes([.21, .71, .15, .15])
ax2.plot(t, V_exp, 'b-', linewidth=1)
ax2.plot(t, V, 'r-',     linewidth=1)
ax2.plot(t, V2, 'g-',    linewidth=1)
ax2.set_xlim([0.0015, 0.0016])
ax2.set_ylim([0.793, 0.795])

ax0.set_ylim([-1, 1])
ax1.set_ylim([-4, 4])

ax1.set_xlabel('t [s]'); ax0.set_ylabel('V [V]'); ax1.set_ylabel('Residui [mV]'); grid(ax0); grid(ax1); grid(ax2); 
#ax0.legend()
#fig.savefig('fig/w_s.eps', format='eps')
fig.show()