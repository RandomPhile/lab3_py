import math
'''
libreria per incertezze in python:
Variabile = m(valore, incertezza)
Variabile.n = valore; Variabile.s = incertezza
'''
from uncertainties import ufloat as m
from uncertainties.umath import *

def media_cursori(minimo, massimo):
	return m((massimo+minimo)/2, abs(massimo-minimo)/2)

def prints(*args):
	out = []
	for arg in args:
		if type(arg)==float or type(arg)==int:
			out.append("{:.2e}".format(arg))
		else:
			out.append(arg)
	print(*out)


#Follower con resistenza in serie
R1, R2 = 1e6, 10e6
dVin_DC1  = m(-12.5e-3,6e-3)
dVout_DC1 = m(-80.5e-3,13e-3)
dVin_phi1  = m(4.8e-6,2e-6)
dVout_phi1 = m(25e-6,3e-6)

dVin_DC2  = m(-12e-3,6e-3)
dVout_DC2 = m(-533e-3,17e-3)
dVin_phi2  = m(505e-6,3e-6)
dVout_phi2 = m(582e-6,6e-6)

dPhi1 = (dVout_phi1-dVin_phi1)*2*math.pi/1e-3
dPhi2 = (dVout_phi2-dVin_phi2)*2*math.pi/1e-3

print(dPhi1, dPhi2)

R1, R2 = 10e3, 100e3#ohm
#Amplificatore invertente
Vin  = media_cursori(0.491, 0.505)*2
Vout = media_cursori(4.99, 5.05)*2 * (-1)#perchè sfasato di pi

G = Vout/Vin
print('\nInvertente    ', Vin, Vout, G)

#Amplificatore non-invertente
Vin  = media_cursori(0.4875, 0.5075)*2
Vout = media_cursori(5.525, 5.675)*2

G = Vout/Vin
print('\nNon-Invertente', Vin, Vout, G)

#Amplificatore differenziale con sfasamento DeltaPhi=pi
V1 = media_cursori(0.2488, 0.2563)*2
V2 = media_cursori(0.2413, 0.2513)*2 * (-1)
Vout = media_cursori(4.95, 5.175)*2 * (-1)

Vdiff = V2-V1
G = Vout/Vdiff
print('\nDifferenziale', Vdiff, Vout, G)

#Derivatore
R, C = 1e3, 10e-9
f_teo = 1/(2*math.pi*R*C)
f_mis = 16.6e3
Tau_teo = R*C
Tau_mis = 1/(2*math.pi*f_mis)

prints('\nDerivatore    ', f_teo, f_mis, Tau_teo, Tau_mis)
