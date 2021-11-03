from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
from functions import *
colori = ['b','g','r','c','m','y','k']

T = 1/1005.3
delay = 0.00055
duty = 0.001

#V1 segnale sinusoidale; V2 segnale sample and hold
#t,V1,V2 = data_from_csv('reconstructionExample/sine_100_Hz')
t,V1,V2 = data_from_csv('misure2/scope_0',True,-0.02,0.02)


plt.plot(t,V1, 'b-', label='data')
plt.plot(t,V2, 'r-', label='data')

t_pt,V_pt,r_tr,r_sinc = reconstruct(t,V2,T,delay,duty)

plt.plot(t_pt + duty/2,V_pt, 'ko', label='data')

plt.plot(t, r_tr)

plt.xlabel('t')
plt.ylabel('V')
#plt.legend()

plt.minorticks_on()
plt.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
plt.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')
plt.show()
