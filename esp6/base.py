def grid(ax):
	ax.minorticks_on()
	ax.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
	ax.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')