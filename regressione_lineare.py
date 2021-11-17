from math import pi
import numpy as np

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