from math import *
import numpy as np
import matplotlib.pyplot as plt

R1, R2 = 1e6, 100
RC = [
	[100e3, 10e-9],
	[1e6  , 10e-9]
]

V1 = [.630 1.35 3.85];
V2 = [.640 1.34 1.2];
T  = [6.32 64.8 20.3]*1e-3;

f_exp = 1./T
f_teo = 1./(2*pi*R.*C)
