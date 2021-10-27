from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

R = 100


def I_func(V, R_L, alpha):
	return (V * 1e3)/(R_L * (1 + alpha * V**2))

V = np.array([1,2,3,4,5,6,7,8,9])

I = np.array([1,3,3,4,5,6,7,8,9])*2

plt.plot(V, I, 'b-', label='data')


#Senza intervallo di R_L, alpha
popt, pcov = curve_fit(I_func, V, I)
plt.plot(V, I_func(V, *popt), 'r-', label='fit: R_L=%5.3f, alpha=%5.3f' % tuple(popt))

#Con intervallo
popt, pcov = curve_fit(I_func, V, I, bounds=([400,-1], [450, 1]))
plt.plot(V, I_func(V, *popt), 'g--', label='fit: R_L=%5.3f, alpha=%5.3f' % tuple(popt))



plt.xlabel('V')
plt.ylabel('I')
plt.legend()
plt.show()