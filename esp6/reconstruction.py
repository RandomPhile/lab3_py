import numpy as np
import matplotlib.pyplot as plt
from functions import *

parametri = [
{'name': 'reconstructionExample/sine_100_Hz', 'T': 0.001, 'delay': -0.0001, 'err': False},
{'name': 'misure2/scope_0', 'T': 1/1005.3, 'delay': 0.00033, 'err': False},
{'name': 'misure2/scope_1', 'T': 1/1005.3, 'delay': 0.00052, 'err': False},
{'name': 'misure2/scope_2', 'T': 1/1005.3, 'delay': 0.00011, 'err': False},
{'name': 'misure2/scope_3', 'T': 1/1005.3, 'delay': 0.00038, 'err': True},
{'name': 'misure2/scope_4', 'T': 1/1005.3, 'delay': 0.00045, 'err': False},
{'name': 'misure2/scope_5', 'T': 1/1005.3, 'delay':-0.00003, 'err': False},
{'name': 'misure2/scope_6', 'T': 1/1005.3, 'delay': 0.00020, 'err': False},
{'name': 'misure2/scope_7', 'T': 1/1005.3, 'delay': 0.00044, 'err': False},
]


for n in [1]:#[[1,2,3,4,5,6,7,8]:
	print(n)
	name,T,delay,err = parametri[n]['name'],parametri[n]['T'],parametri[n]['delay'],parametri[n]['err']

	t,V1,V2 = data_from_csv(name,True)
	t_pt,V_pt,r_tr,r_sinc = reconstruct(t,V2,T,delay,err)

	plot_figure(t,V1,V2,t_pt,r_tr,r_sinc,V_pt,-0.02,0.02,n,save=False)
