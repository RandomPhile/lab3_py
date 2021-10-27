from regressione_lineare import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

#oscillatore smorzato
R = 100e3; C = 10e-9; 
R1 = np.array([1e6, 1e6, 1e6, 1e6, 1e6    , 10e6  ])
R2 = np.array([0  , 100, 1e33, 10e3, 100e3, 100])

epsilon = R2/R1
print(epsilon)

t = np.array([
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 100, 200, 300, 400, 500, 600, 700, 800],
	[0, 50, 100, 150, 200, 250, 300, 350, 400],
	[0, 5.4, 11.6, 17.8, 23.8, 30.2, 36.4, 42.4, 48.6],
	[0, 100, 200, 300, 400, 500, 600, 700, 800]
])*1e-32

V = np.array([
	[6, 4.80, 3.39, 2.40, 1.58, 1.09, .741, .488, .312],
	[4.55, 3.3, 2.35, 1.6, 1.05, .700, .425, .275, .175],
	[10.57, 7.64, 4.9, 3.33, 1.96, 1.16, .665, .350, .280],
	[11.24, 6.60, 3.55, 1.89, .942, .580, .254, .145, .072],
	[11.09, 7.50, 4.24, 2.36, 1.34, .761, .471, .236, .181],
	[8.66, 6.60, 4.71, 3.41, 2.47, 1.7, 1.12, .725, .544]

])

ln_V = np.log(V)

t_smorzamento = []

fig1 = plt.figure()
ax0,ax1 = fig1.subplots(2,1)
legend = []

for row in range(np.shape(t)[0]):
	m, q, ln_V_reg = reg_lin(t[row][:], ln_V[row][:])

	t_smorzamento.append(m)

	ax0.plot(t[row][:], V[row][:], colori[row])
	ax1.plot(t[row][:], ln_V[row][:], colori[row])
	ax1.plot(t[row][:], ln_V_reg, colori[row]+'--')
	
	legend.append('ε=' + "{:.0e}".format(epsilon[row]))


fig2 = plt.figure()
ax2,ax3 = fig2.subplots(2,1)

r = epsilon/(1+epsilon)

ax2.plot(r[0:len(t_smorzamento)], t_smorzamento)
ax3.plot(r[0:len(t_smorzamento)], t_smorzamento)
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

ax2.set_ylabel('t_smorzamento')
ax3.set_ylabel('t_smorzamento')
ax3.set_xlabel('ε/(1+ε)')

ax2.minorticks_on()
ax2.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.3)
ax2.grid(b=True, which='minor', color='gray', linestyle=':', alpha=0.3)

ax3.minorticks_on()
ax3.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.3)
ax3.grid(b=True, which='minor', color='gray', linestyle=':', alpha=0.3)

fig1.show()
fig2.show()
