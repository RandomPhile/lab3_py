import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

'''
l'onda quadra scende in 26.2 microsecondi
periodo 22ms

'''
R1 = np.array([10e3, 1e3 ])
R2 = np.array([10e3, 10e3])

rapporto = R1/R2

T   = np.array([22.1, ])*1e-3
f = 2*pi/T
Vpp = np.array([21.4, 21.19])