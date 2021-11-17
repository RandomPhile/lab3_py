import numpy as np
import matplotlib.pyplot as plt

def plot_single(t,V1,V2,t_pt,V_pt,r, t_min,t_max, n, ax):
	legend_list = [r'$50\ $Hz', r'$100\ $Hz', r'$200\ $Hz', r'$900\ $Hz', 
				   r'$900\ $Hz', r'$200\ $Hz', r'$100\ $Hz', r'$50\ $Hz']
	##rimuovi dati al di fuori dei limiti temporali
	index_t = (t < t_min) | (t > t_max)
	index_t_pt = (t_pt < t_min) | (t_pt > t_max)
	V1 = np.delete(V1, index_t)
	V2 = np.delete(V2, index_t)
	r = np.delete(r, index_t)
	t = np.delete(t, index_t)
	V_pt = np.delete(V_pt, index_t_pt)
	t_pt = np.delete(t_pt, index_t_pt)

	# ax0.axis([-0.002, 0.002, -.5, .5])
	# ax1.axis([-0.020, -0.016, -.5, .5])

	ax.plot(t,V1, 'b-', label='Segnale', linewidth=0.7)
	ax.plot(t,V2, 'g-', label='Campionamento', linewidth=0.5)
	ax.plot(t_pt,V_pt, 'k+', label='Punti campionati')

	ax.plot(t, r, 'r-', linewidth=0.7)

	ax.set_xlabel('t [s]')
	ax.set_ylabel('V [V]')
	ax.legend([legend_list[n]], loc=1)
	
	#fig.tight_layout()