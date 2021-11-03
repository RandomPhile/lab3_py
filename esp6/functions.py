import numpy as np
import csv

def data_from_csv(name_csv,two_channels=True):
	t = np.array([])
	V1 = np.array([])
	V2 = np.array([])

	with open(name_csv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)

		skip = 0
		for row in reader:
			if skip >= 1:
				t = np.append(t, float(row['x-axis']))
				V1 = np.append(V1, float(row['1']))
				if two_channels:
					V2 = np.append(V2, float(row['2']))
			skip += 1
	if two_channels:
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

def r(t,t_pt,V_pt,T):
	out = 0
	for j in range(len(t_pt)):
		out += -V_pt[j] * k_tr(t + t_pt[j],T)
	return out

def reconstruct(t,V,T,delay):
	offset = 3
	t_pt = np.array([])
	V_pt = np.array([])

	for j in range(offset, len(t)-offset):
		if j%40==0:
			t_pt = np.append(t_pt, t[j] - delay)
			V_pt = np.append(V_pt, V[j])

	return t_pt, V_pt, r(t,t_pt,V_pt,T)
