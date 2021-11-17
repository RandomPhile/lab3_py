import csv
from scipy.optimize import curve_fit
from math import *
import numpy as np
import matplotlib.pyplot as plt
colori = ['b','g','r','c','m','y','k']

#generazione segnale 1kHz

ampiezza = 5.14   #V
up_time = 15.24e-6 #s
#down_time = 1e-3 - up_time
duty_up = 100*up_time/1e-3
duty_down = 100-duty_up
print(duty_up,':',duty_down)
