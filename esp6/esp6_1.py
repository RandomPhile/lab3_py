import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']



with open('dati/scope_1.csv', newline='') as csvfile:
	V1 = np.array([])
	V2 = np.array([])
	reader = csv.DictReader(csvfile)

	i = 0
	for row in reader:
		#if i>25 and i<280:
		if i>290 and i<600:
			V1 = np.append(V1, float(row['1']))
			V2 = np.append(V2, float(row['2']))
		i+=1

V1 = V1[2:]
V2 = V2[2:]

I = (V1/R)*10**3
V = V2

plt.plot(V, I, 'b-', label='data')


popt, pcov = curve_fit(I_func, V, I)#bounds=([], [])
plt.plot(V, I_func(V, *popt), 'r-', label='fit: R_L=%5.3f, alpha=%5.3f' % tuple(popt))


plt.xlabel('V')
plt.ylabel('I')
plt.legend()
plt.show()