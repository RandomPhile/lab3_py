import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

T = 1/1005.3
delay = 0.0005

with open('reconstructionExample/sine_100_Hz.csv', newline='') as csvfile:
	t = np.array([])
	V1 = np.array([])
	V2 = np.array([])
	reader = csv.DictReader(csvfile)

	t_campionati = np.array([])
	V_campionati = np.array([])

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
			t_campionati = np.append(t_campionati, t[j] - delay)
			V_campionati = np.append(V_campionati, V2[j])

plt.plot(t,V1, 'b-', label='data')
plt.plot(t,V2, 'r-', label='data')
plt.plot(t_campionati,V_campionati, 'ko', label='data')

def k_tr(t_list):
	out = np.array([])
	for t in t_list:
		if abs(t) < T:
			out = np.append(out, 1-abs(t)/T)
		else:
			out = np.append(out, 0)
	return out

def r(t):
	out = 0
	for j in range(len(t_campionati)):
		out += -V_campionati[j] * k_tr(t + t_campionati[j])
	return out

plt.plot(t, r(t))

plt.xlabel('t')
plt.ylabel('V')
#plt.legend()
plt.show()