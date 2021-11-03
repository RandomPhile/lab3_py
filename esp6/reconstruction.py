from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
from functions import *
colori = ['b','g','r','c','m','y','k']

T = 1/1005.3
delay = 0.0005

#V1 segnale sinusoidale; V2 segnale sample and hold
t,V1,V2 = data_from_csv('reconstructionExample/sine_100_Hz.csv')

plt.plot(t,V1, 'b-', label='data')
plt.plot(t,V2, 'r-', label='data')

t_pt,V_pt,r = reconstruct(t,V2,T,delay)

plt.plot(t_pt,V_pt, 'ko', label='data')

plt.plot(t, r)

plt.xlabel('t')
plt.ylabel('V')
#plt.legend()
plt.show()
