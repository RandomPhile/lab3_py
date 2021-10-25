from math import *
import numpy as np
import matplotlib.pyplot as plt

R = np.array([100e3, 1e6])
C = 10e-9
R1, R2 = 1e6, 100
RC = np.array([
	[100e3, 10e-9],
	[1e6  , 10e-9]
])

V1 = np.array([.630, 1.35, 3.85])
V2 = np.array([.640, 1.34, 1.2])
T  = np.array([6.32, 64.8, 20.3])*1e-3

f_exp = 1/T
f_teo = 1/(2*pi*R*C)

print(f_exp)
print(f_teo)

dt = np.array([1.591, 16.1, 5])*1e-3
phi_exp = dt*f_exp*2*pi
phi_teo = pi/2

print(phi_exp)
print(phi_teo)

'''
Con R_A = 100k, R_B = 1M -> stabile con ellisse 

Con R_A = 1M, R_B = 100k -> instabile, 

'''