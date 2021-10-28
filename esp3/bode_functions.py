from math import pi
import numpy as np

def bode(f, dt, V_in, V_out, dV_in, dV_out):
	mod_G = V_out/V_in
	phi_G = dt * f*2*pi
	dmod_G = mod_G * np.sqrt((dV_in/V_in)**2 + (dV_out/V_out)**2)
	dphi_G = np.ones(f.size) * 2*pi/180

	#G = mod_G * e**(1j*phi_G)
	return [mod_G,phi_G,dmod_G,dphi_G]

def bode_plot(f, G, ax0,ax1, colore='None', primo=True,errori=False):
	if primo:
		pass
	else:
		ax0.set_autoscale_on(False)
		ax1.set_autoscale_on(False)

	if errori:
		mod, phi, dmod, dphi = G[0], G[1], G[2], G[3]
	else:
		mod, phi = abs(G), np.angle(G)

	if errori:
		ax0.errorbar(f,mod,dmod, linestyle='none', color=colore, fmt='o', markersize=2, capsize=2)
	else:
		ax0.plot(f,mod, color=colore)
	ax0.set_xscale('log'); ax0.set_yscale('log')

	if primo:
		ax0_dB = ax0.twinx()
		ax0_dB.plot(f,20*np.log10(mod), linestyle='none', color=colore)
		ax0_dB.set_ylabel('|G| (dB)')

	if errori:
		ax1.errorbar(f,phi*180/pi,dphi*180/pi, linestyle='None',color=colore, fmt='o', markersize=2, capsize=2)
	else:
		ax1.plot(f,phi*180/pi, color=colore)
	ax1.set_xscale('log')

	
	ax0.set_ylabel('|G|')
	ax1.set_ylabel('ϕ (deg)')
	ax1.set_xlabel('f (Hz)')
	
	

	ax0.minorticks_on()
	ax0.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
	ax0.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')

	ax1.minorticks_on()
	ax1.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
	ax1.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')

