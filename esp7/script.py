import numpy as np
import matplotlib.pyplot as plt
from functions import *
from base import *

def reg_lin(x, y):
	N = len(x)
	x_mean = np.mean(x)
	y_mean = np.mean(y)

	m_num = ((x - x_mean) * (y - y_mean)).sum()
	m_den = ((x - x_mean)**2).sum()
	m = m_num / m_den
	
	q = y_mean - (m*x_mean)

	y_line = q + m*x

	return m, q, y_line

#N = np.arange(1,13)
N =          np.array([1,    2,    3,    4,    5,    6,    7,    8,    9,    10,   11,    12])
t_diff =     np.array([58.0, 60.4, 66.0, 69.8, 74.6, 79.2, 80.0, 83.2, 88.0, 93.0, 96.6,  101.6])*1e-9
t_diff_max = np.array([59.6, 60.8, 67.8, 71.1, 76.8, 79.6, 84.8, 83.8, 88.4, 93.6, 97.4,  102.0])*1e-9
dt_diff = np.abs(t_diff_max-t_diff)/2

fig = plt.figure()
ax = fig.subplots()
ax.errorbar(N, t_diff, yerr=dt_diff, fmt=' ', color='b', marker='o', ms=3)
m,q,t_diff_fit = reg_lin(N, t_diff)
ax.plot(N, t_diff_fit)
print(m,q)

grid(ax)
fig.show()