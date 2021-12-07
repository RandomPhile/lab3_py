import numpy as np
import matplotlib.pyplot as plt
from functions import *
from base import *
from scipy.optimize import curve_fit

#N = np.arange(1,13)
N =          np.array([1,    2,    3,    4,    5,    6,    7,    8,    9,    10,   11,    12])
t =     np.array([58.0, 60.4, 66.0, 69.8, 74.6, 79.2, 80.0, 83.2, 88.0, 93.0, 96.6,  101.6])*1e-9
t_max = np.array([59.6, 60.8, 67.8, 71.1, 76.8, 79.6, 84.8, 83.8, 88.4, 93.6, 97.4,  102.0])*1e-9
dt = np.abs(t_max-t)/2


t_mod = lambda x,m,q : m*x+q
t_mod0 = lambda x,m : m*x

popt, pcov = curve_fit(t_mod, N, t, sigma=dt)
#m0, pcov0 = curve_fit(t_mod0, N, t, sigma=dt)

m, q = popt
dm, dq = np.sqrt(np.diag(pcov))
#dm0= np.sqrt(np.diag(pcov0))


fig = plt.figure()
ax = fig.subplots()
ax.errorbar(N, t*1e9, yerr=dt*1e9, fmt=' ', color='b', marker='o', ms=2, label='Data')
ax.plot(N,t_mod(N,m,q)*1e9, label=r'Linear fit: $m=(4.0\pm0.1)$ns')
#ax.plot(N,t_mod0(N,m0))

print('m = ',m,'+-',dm)
print('q = ',q,'+-',dq)
ax.set_xlabel(r'$N$: # of logic gates')
ax.set_ylabel(r'Propagation delay $t_d$ [ns]')

ax.legend()
grid(ax)
#fig.savefig('fig/fit.eps', format='eps')
fig.show()