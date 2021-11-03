import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

with open('dati1/scope_0.csv', newline='') as csvfile:
	t = np.array([])
	V1 = np.array([])
	V2 = np.array([])
	reader = csv.DictReader(csvfile)

	t_campionati = []
	V_campionati = []

	i = 0
	for row in reader:
		if i>0:
			t = np.append(t, float(row['x-axis']))
			V1 = np.append(V1, float(row['1']))
			V2 = np.append(V2, float(row['2']))
		i+=1

	offset = 10

	for j in range(offset, len(t)-offset):
		if j%40==0:
			t_campionati = np.append(t_campionati, t[j])
			V_campionati = np.append(V_campionati, V2[j])

print(t, V1)

plt.plot(t,V1, 'b-', label='data')
plt.plot(t,V2, 'r-', label='data')
plt.plot(t_campionati,V_campionati, 'k*', label='data')



plt.xlabel('t')
plt.ylabel('V')
#plt.legend()
plt.show()