import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

'''
ampiezza 1.48V 
dt       6.25ms
f        160Hz

'''

with open('parte1/scope_3.csv', newline='') as csvfile:
	t = np.array([])
	V = np.array([])
	reader = csv.DictReader(csvfile)

	i = 0
	for row in reader:
		#if i>25 and i<280:
		if i>2:
			t = np.append(t, float(row['x-axis']))
			V = np.append(V, float(row['1']))
		i+=1
t = t[2:]
V = V[2:]


plt.plot(t, V, 'b-', label='data')


#popt, pcov = curve_fit(I_func, V, I)#bounds=([], [])
#plt.plot(V, I_func(V, *popt), 'r-', label='fit: R_L=%5.3f, alpha=%5.3f' % tuple(popt))


plt.xlabel('t')
plt.ylabel('V')
plt.legend()
plt.show()