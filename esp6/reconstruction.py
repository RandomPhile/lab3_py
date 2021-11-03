from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
from functions import *
colori = ['b','g','r','c','m','y','k']

#V1 segnale sinusoidale; V2 segnale sample and hold
#t,V1,V2 = data_from_csv('reconstructionExample/sine_100_Hz')

parametri = [
{'name': 'reconstructionExample/sine_100_Hz', 'T': 0.001, 'delay': 0.0005, 't_offset': -0.0001, 'alias': False},
{'name': 'misure2/scope_0', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00040, 'alias': False},
{'name': 'misure2/scope_1', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00057, 'alias': False},
{'name': 'misure2/scope_2', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00017, 'alias': False},
{'name': 'misure2/scope_3', 'T': 1/1005.3, 'delay':-0.0005, 't_offset': -0.0006, 'alias': True},
{'name': 'misure2/scope_4', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00052, 'alias': True},
{'name': 'misure2/scope_5', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00002, 'alias': True},
{'name': 'misure2/scope_6', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00024, 'alias': True},
{'name': 'misure2/scope_7', 'T': 1/1005.3, 'delay': 0.00055, 't_offset': 0.00051, 'alias': True},
]

n = 3
name = parametri[n]['name']
T = parametri[n]['T']
delay = parametri[n]['delay']
t_offset = parametri[n]['t_offset']
alias = parametri[n]['alias']

t,V1,V2 = data_from_csv(name,True,-0.02,0.02)
t_pt,V_pt,r_tr,r_sinc = reconstruct(t,V2,T,delay,t_offset,alias)

fig = plt.figure()
ax0,ax1 = fig.subplots(2,1)

ax0.plot(t,V1, 'b-', label='Segnale', linewidth=1)
ax0.plot(t,V2, 'g-', label='Campionamento')
ax0.plot(t_pt,V_pt, 'k+', label='Punti campionati')

ax1.plot(t,V1, 'b-', label='Segnale', linewidth=1)
ax1.plot(t,V2, 'g-', label='Campionamento')
ax1.plot(t_pt,V_pt, 'k+', label='Punti campionati')

ax0.plot(t, r_tr, 'r-', linewidth=0.7)
ax1.plot(t, r_sinc, 'r-', linewidth=0.7)

#ax0.axis([-0.002, 0.002, -1, 1])
#ax1.axis([-0.020, -0.016, -1, 1])

ax1.set_xlabel('t [s]')
ax0.set_ylabel('V [V]')
ax1.set_ylabel('V [V]')
#ax0.legend()

ax0.minorticks_on()
ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')

ax1.minorticks_on()
ax1.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
ax1.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')
plt.show()
