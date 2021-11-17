import numpy as np
import matplotlib.pyplot as plt
from functions import *
from base import *

#N = np.arange(1,13)
N =          np.array([1,    2,    3,    4,    5,    6,    7,    8,    9,    10,   11,    12])
t_diff =     np.array([58,   60.4, 69.8, 66,   80,   74.6, 83.2, 79.2, 93,   88,   101.6, 96.6])*1e-9
t_diff_max = np.array([59.6, 60.8, 71.1, 67.8, 84.8, 76.8, 83.8, 79.6, 93.6, 88.4, 102,   97.4])*1e-9

fig = plt.figure()
ax = fig.subplots()
ax.plot(N, t_diff)

fig.show()
