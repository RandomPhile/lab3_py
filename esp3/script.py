from bode_functions import *
from math import *
import numpy as np
import matplotlib.pyplot as plt


R = 1e5; C = 1e-8
tau = R*C
f3db = 1/(2*pi*tau)

R_osc=1e6; C_osc=120e-12

f_exp  = np.array([5    ,10    ,20    ,50    ,100    ,130    ,160    ,200    ,500    ,1e3    ,2e3])

V_in   = np.array([3    ,3     ,3     ,2.98  ,3      ,2.99   ,2.98   ,3      ,3      ,3      ,3])
dV_in  = np.array([37.5 ,37    ,37.5  ,50    ,40     ,43     ,43     ,43     ,31     ,43     ,43])*0.5e-3
V_out  = np.array([2.48 ,2.48  ,2.4   ,2.03  ,1.42   ,1.16   ,.962   ,.77    ,.231   ,.07    ,.0183])
dV_out = np.array([50   ,50    ,50    ,43    ,30     ,30     ,30     ,30     ,30     ,20     ,14])*0.5e-3
dt     = np.array([3    ,2.82  ,2.6   ,2.34  ,1.86   ,1.66   ,1.51   ,1.32   ,.726   ,.408   ,.22])*1e-3


#modello
f = np.logspace(0,3.5)
w = 2*pi*f
Z_eq = R/(1-1j*w*tau);
Z    = R_osc/(1-1j*w*R_osc*(C+C_osc));
G   = Z*Z_eq/(R*(Z_eq+R+Z));
#dati sperimentali
G_exp = bode(f_exp, dt, V_in, V_out, dV_in, dV_out)

fig = plt.figure()
ax0,ax1 = fig.subplots(2,1)

bode_plot(f, G, ax0,ax1, colore='orange')
bode_plot(f_exp, G_exp, ax0,ax1, colore='red', primo=False, errori=True)

ax0.legend({'Dati','Modello'})

plt.show()

