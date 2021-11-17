import numpy as np
import matplotlib.pyplot as plt
from functions6 import *
from base import *

dati = [[
{'name': 'dati/sin/scope_0', 'T': 1/1005.3, 'delay': 0.00033},
{'name': 'dati/sin/scope_1', 'T': 1/1005.3, 'delay': 0.00052},
{'name': 'dati/sin/scope_2', 'T': 1/1005.3, 'delay': 0.00011},
{'name': 'dati/sin/scope_3', 'T': 1/1005.3, 'delay': 0.0003}],
[{'name': 'dati/triang/scope_0', 'T': 1/1005.3, 'delay': 0.0004},
{'name': 'dati/triang/scope_1', 'T': 1/1005.3, 'delay':-0.00003},
{'name': 'dati/triang/scope_2', 'T': 1/1005.3, 'delay': 0.00020},
{'name': 'dati/triang/scope_3', 'T': 1/1005.3, 'delay': 0.00044}]
]

parte = 1
save = 0

t_max = 0.02
t_min = -t_max

fig1 = plt.figure()
fig2 = plt.figure()
axes1 = fig1.subplots(2,2)
axes2 = fig2.subplots(2,2)

for n in [0,1,2,3]:
	print('#',n)
	ax1 = axes1[int(n/2)][n%2]
	ax2 = axes2[int(n/2)][n%2]

	name,T,delay = dati[parte][n]['name'],dati[parte][n]['T'],dati[parte][n]['delay']
	t,V1,V2 = data_from_csv(name,True)
	t_pt,V_pt,r_tr,r_sinc = reconstruct(t,V2,T,delay)
	plot_single(t,V1,V2,t_pt,V_pt,r_tr, t_min, t_max, n, ax1)
	plot_single(t,V1,V2,t_pt,V_pt,r_sinc, t_min, t_max, n, ax2)
	grid(ax1); grid(ax2)

fig1.tight_layout()
fig2.tight_layout()
if save:
	if parte==0:
		fig1.savefig('fig/sin_linear.eps', format='eps')
		fig2.savefig('fig/sin_sinc.eps', format='eps')
	if parte==1:
		fig1.savefig('fig/triang_linear.eps', format='eps')
		fig2.savefig('fig/triang_sinc.eps', format='eps')
fig1.show()
fig2.show()