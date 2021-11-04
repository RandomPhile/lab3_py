import numpy as np
import csv
import matplotlib.pyplot as plt

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
		out += V_pt[j] * k_tr(t - t_pt[j],T)
	return out

def r_sinc(t,t_pt,V_pt,T):
	out = 0
	for j in range(len(t_pt)):
		out += V_pt[j] * k_sinc(t - t_pt[j],T)
	return out

def reconstruct(t,V,T,delay):
	t_pt = np.array([])
	V_pt = np.array([])

	t_i = delay

	while t_i>min(t):
		t_i -= T
	while t_i<max(t):
		index = np.argmin(abs(t - t_i))
		t_pt = np.append(t_pt, t[index]-T/2)
		V_pt = np.append(V_pt, V[index])
		t_i += T

	return t_pt, V_pt, r_tr(t,t_pt,V_pt,T), r_sinc(t,t_pt,V_pt,T)
	

def plot_figure(t,V1,V2,t_pt,r_tr,r_sinc,V_pt,t_min,t_max,n,save=False):
	##rimuovi dati al di fuori dei limiti temporali
	index_t = (t < t_min) | (t > t_max)
	index_t_pt = (t_pt < t_min) | (t_pt > t_max)
	V1 = np.delete(V1, index_t)
	V2 = np.delete(V2, index_t)
	r_tr = np.delete(r_tr, index_t)
	r_sinc = np.delete(r_sinc, index_t)
	t = np.delete(t, index_t)
	V_pt = np.delete(V_pt, index_t_pt)
	t_pt = np.delete(t_pt, index_t_pt)

	##crea nuova figura
	fig = plt.figure()
	ax0,ax1 = fig.subplots(2,1)

	# ax0.axis([-0.002, 0.002, -.5, .5])
	# ax1.axis([-0.020, -0.016, -.5, .5])

	ax0.plot(t,V1, 'b-', label='Segnale', linewidth=0.7)
	ax0.plot(t,V2, 'g-', label='Campionamento', linewidth=0.5)
	ax0.plot(t_pt,V_pt, 'k+', label='Punti campionati')

	ax1.plot(t,V1, 'b-', label='Segnale', linewidth=0.7)
	ax1.plot(t,V2, 'g-', label='Campionamento', linewidth=0.5)
	ax1.plot(t_pt,V_pt, 'k+', label='Punti campionati')

	ax0.plot(t, r_tr, 'r-', linewidth=0.7)
	ax1.plot(t, r_sinc, 'r-', linewidth=0.7)

	ax1.set_xlabel('t [s]')
	ax0.set_ylabel('V [V]')
	ax1.set_ylabel('V [V]')

	ax0.minorticks_on()
	ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
	ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')

	ax1.minorticks_on()
	ax1.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
	ax1.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')
	fig.tight_layout()
	
	ax0.legend(['#'+str(n)], loc=1)
	if save:
		fig.savefig('fig/fig'+str(n)+'.eps', format='eps')
	fig.show()
