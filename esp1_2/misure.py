import math
#import numpy as np

def media(medio, massimo):
	return misura(medio, abs(massimo-medio))

class misura(object):
	"""docstring for misura"""
	def __init__(self, v,e):
		super(misura, self).__init__()
		self.v = v
		self.e = e
	def per(self, B):
		out_v = self.v * B.v
		out_e = abs(out_v)*math.sqrt((self.e/self.v)**2 + (B.e/B.v)**2)
		return misura(out_v,out_e)


def num(n):
	return misura(n,0)

def piu(A,B):
	out_v = A.v + B.v
	out_e = math.sqrt(A.e**2 + B.e**2)
	return misura(out_v,out_e)

def per(A,B):
	out_v = A.v * B.v
	out_e = abs(out_v)*math.sqrt((A.e/A.v)**2 + (B.e/B.v)**2)
	return misura(out_v,out_e)

def div(A,B):
	out_v = A.v / B.v
	out_e = abs(out_v)*math.sqrt((A.e/A.v)**2 + (B.e/B.v)**2)
	return misura(out_v,out_e)


#Amplificatore invertente
R1, R2 = 10e3, 100e3#ohm

Vin = media(0.491, 0.505)
Vout = media(-4.99, -5.05)

G = div(Vout,Vin)

print('G: ',G.v,' dG: ',G.e)



#Amplificatore non-invertente
R1, R2 = 10e3, 100e3#ohm

Vin = media(0.4875, 0.5075)
Vout = media(5.525, 5.675)

G = div(Vout,Vin)

print('G: ',G.v,' dG: ',G.e)


#Amplificatore differenziale
R1, R2 = 10e3, 100e3#ohm
Vdiff = [0,0]

V1 = media(0.2488, 0.2563)
V2 = media(-0.2413, -0.2513)

Vdiff[0] = V2[0] - V1[0]
Vout = media(-4.95, -5.175)

G = Vout[0]/Vdiff[0]
#print('G: ',G,' dG: ',dG)


#Amplificatore 
R = 1e3
C = 10e-9
#w0*R*C=1
f_mis = 16.6e3#Hz
f_teo = 1/(2*np.pi*R*C)

#print(f_mis, f_teo)
'''


x=cos(wt)
y=cos(2wt)=

'''
'''
plt.plot(x, y, label='Plot')
plt.xlabel('Vin [V]')
plt.ylabel('Vout [V]')
plt.legend()
plt.show()
'''