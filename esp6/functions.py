import numpy as np
import csv

def data_from_csv(name_csv,two_channels=True,t_min=-1e20,t_max=1e20):
	t = np.array([])
	V1 = np.array([])
	V2 = np.array([])

	with open(name_csv+'.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)

		skip = 0
		for row in reader:
			if skip >= 1:
				t = np.append(t, float(row['x-axis']))
				V1 = np.append(V1, float(row['1']))
				if two_channels:
					V2 = np.append(V2, float(row['2']))
			skip += 1

	index = []
	for i in range(len(t)):
		if t[i]<t_min or t[i]>t_max:
			index.append(i)
	t = np.delete(t, index)
	V1 = np.delete(V1, index)

	if two_channels:
		V2 = np.delete(V2, index)
		return t,V1,V2
	else:
		return t,V1

def k_tr(t_,T):
	out = np.array([])
	for t in t_:
		if abs(t) < T:
			out = np.append(out, 1-abs(t)/T)
		else:
			out = np.append(out, 0)
	return out

def k_sinc(t_,T):
	return np.sinc(t_/T)

def r_tr(t,t_pt,V_pt,T):
	out = 0
	for j in range(len(t_pt)):
		out += -V_pt[j] * k_tr(t + t_pt[j],T)
	return out

def r_sinc(t,t_pt,V_pt,T):
	out = 0
	for j in range(len(t_pt)):
		out += -V_pt[j] * k_sinc(t + t_pt[j],T)
	return out

def reconstruct(t,V,T,delay,duty):
	t_pt = np.array([])
	V_pt = np.array([])

	#t_i = 0 - 0.0001
	t_i = 0 + 0.00025

	while t_i>min(t):
		t_i -= duty

	while t_i<max(t):
		index = np.argmin(abs(t - t_i))
		t_pt = np.append(t_pt, t[index]-delay)
		V_pt = np.append(V_pt, V[index])
		t_i += duty

	return t_pt, V_pt, r_tr(t,t_pt,V_pt,T), r_sinc(t,t_pt,V_pt,T)
