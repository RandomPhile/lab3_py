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

r = R2/(R1+R2) + 0.0025
R_f = 10e3#Ohm
I_S = 10e-9#A
R_0 = 1e9#Ohm
beta = 40#V^-1
n = 1
chi = 1/(2*(1+I_S*R_0*beta/n))
csi = I_S*R_0*beta**3/(3*n**3*chi**4)

V_ref = np.sqrt((R_f*chi/R_0 - 2*r)/(3*R_f*csi/R_0))

V1 = np.array([.630, 1.35, 3.85])
V2 = np.array([.640, 1.34, 1.2])
T  = np.array([6.32, 64.8, 20.3])*1e-3

w_exp = 2*pi/T
w_teo = 1/(R*C) 

print(w_exp)
print(w_teo)

dt = np.array([1.591, 16.1, 5])*1e-3
phi_exp = dt*w_exp
phi_teo = pi/2

print(phi_exp)
print(phi_teo)

print(V_ref)
'''
Con R_A = 100k, R_B = 1M -> stabile con ellisse 

Con R_A = 1M, R_B = 100k -> instabile, 

'''