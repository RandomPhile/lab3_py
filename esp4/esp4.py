from regressione_lineare import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

import matplotlib
matplotlib.rcParams['text.usetex'] = True

#oscillatore smorzato
R = 100e3; C = 10e-9; 
R1 = np.array([1e6, 10e6, 1e6, 1e6, 1e6 , 1e6])
R2 = np.array([0  , 100 , 100, 1e3, 10e3, 100e3])

epsilon = R2/R1
#epsilon = epsilon[:-1]
print(epsilon)

t = np.array([
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 50, 100, 150, 200, 250, 300, 350, 400],
	[0, 5.4, 11.6, 17.8, 23.8, 30.2, 36.4, 42.4, 48.6]
])*1e-3

V = np.array([
	[6, 4.80, 3.39, 2.40, 1.58, 1.09, .741, .488, .312],
	[8.66, 6.60, 4.71, 3.41, 2.47, 1.7, 1.12, .725, .544],
	[4.55, 3.3, 2.35, 1.6, 1.05, .700, .425, .275, .175],
	[10.57, 7.64, 4.9, 3.33, 1.96, 1.16, .665, .350, .280],
	[11.24, 6.60, 3.55, 1.89, .942, .580, .254, .145, .072],
	[11.09, 7.50, 4.24, 2.36, 1.34, .761, .471, .236, .181]
])

ln_V = np.log(V)

t_smorzamento = []

fig1 = plt.figure()
ax0,ax1 = fig1.subplots(2,1)
legend = []

for row in range(np.shape(epsilon)[0]):
	m, q, ln_V_reg = reg_lin(t[row][:], ln_V[row][:])

	t_smorzamento.append(abs(m))

	ax0.plot(t[row][:], V[row][:], colori[row])
	ax1.plot(t[row][:], ln_V[row][:], colori[row])
	ax1.plot(t[row][:], ln_V_reg, colori[row]+'--')
	
	legend.append('ε=' + "{:.0e}".format(epsilon[row]))


fig2 = plt.figure()
ax2,ax3 = fig2.subplots(2,1)

r = epsilon/(1+epsilon)
w0 = 1/(R*C)
#calcolo r0 a partire dai valori medi di t_smorzamento e di r
r_medio = np.mean(r)
t_smorzamento_medio = np.mean(t_smorzamento)


#r0 = 0.0035

print(r0)
r_mod = np.linspace(0, max(r))
t_smorzamento_mod = r_mod * w0
t_smorzamento_mod2 = (r_mod + r0) * w0
print(t_smorzamento_mod[0])
print(t_smorzamento_mod2[0])

ax2.plot(r, t_smorzamento, 'bo')
ax2.plot(r_mod, t_smorzamento_mod, 'k-')
ax2.plot(r_mod, t_smorzamento_mod2, 'r--')
ax3.plot(r, t_smorzamento, 'bo')
ax3.plot(r_mod, t_smorzamento_mod, 'k-')
ax3.plot(r_mod, t_smorzamento_mod2, 'r--')
ax3.set_xscale('log')

ax0.legend(legend)

ax0.set_ylabel('V₁ (V)')
ax1.set_ylabel('ln(V₁/V)')
ax1.set_xlabel('t (s)')

ax0.minorticks_on()
ax0.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.3)
ax0.grid(b=True, which='minor', color='gray', linestyle=':', alpha=0.3)

ax1.minorticks_on()
ax1.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.3)
ax1.grid(b=True, which='minor', color='gray', linestyle=':', alpha=0.3)

ax2.set_ylabel(r'$1/\tau$ ($s^{-1}$)')
ax3.set_ylabel(r'$1/\tau$ ($s^{-1}$)')
ax3.set_xlabel(r'$r = \frac{\epsilon}{\epsilon + 1}$')

ax2.minorticks_on()
ax2.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.3)
ax2.grid(b=True, which='minor', color='gray', linestyle=':', alpha=0.3)

ax3.minorticks_on()
ax3.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.3)
ax3.grid(b=True, which='minor', color='gray', linestyle=':', alpha=0.3)

#fig1.show()
fig2.show()
