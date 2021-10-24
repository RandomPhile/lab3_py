from regressione_lineare import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

#oscillatore smorzato
R = 100e3; C = 10e-9; 
R1 = np.array([10e6, 1e6, 1e6, 1e6 , 1e6  , 1e6])
R2 = np.array([100 , 100, 1e3, 10e3, 100e3, 0])

epsilon = R2/R1
print(epsilon)

t = np.array([
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9]
])

V = np.array([
	[1,4,9,16,25,36,49,64,81],
	[1,4,9,16,25,36,49,64,81]
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


#fig1.show()
#fig2.show()
