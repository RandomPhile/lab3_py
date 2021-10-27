import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']


R1 = np.array([10e3, 1e3 , 10e3])
R2 = np.array([10e3, 10e3, 1e3 ])

rapporto = R1/R2
print(rapporto)

t_discesa = np.array([26.2, 28.9, 29])*1e-6

T   = np.array([22.1, 3.81, 61.1])*1e-3
f = 2*pi/T
Vpp = np.array([21.4, 21.19, 20.94])

fig, ax0 = plt.subplots()
ax0.plot(rapporto, Vpp, 'b*', label='ampiezza')
ax1 = ax0.twinx()

ax1.plot(rapporto, T, 'r*', label='periodo')

ax1.legend()

print(log(21))
#plt.show()#
