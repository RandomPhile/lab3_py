import csv
import numpy as np

def grid(ax):
	ax.minorticks_on()
	ax.grid(b=True, which='major', color='#d3d3d3', linestyle='-')
	ax.grid(b=True, which='minor', color='#d3d3d3', linestyle=':')

def data_from_csv(name_csv,two_channels=True,t_min=-1e20,t_max=1e20):
	t = np.array([])
	V1 = np.array([])
	V2 = np.array([])

	with open(name_csv+'.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)

		skip = 0
		for row in reader:
			if skip >= 1:
				t = np.append(t, float(row['x-axis']))
				V1 = np.append(V1, float(row['1']))
				if two_channels:
					V2 = np.append(V2, float(row['2']))
			skip += 1

	index = []
	for i in range(len(t)):
		if t[i]<t_min or t[i]>t_max:
			index.append(i)
	t = np.delete(t, index)
	V1 = np.delete(V1, index)

	if two_channels:
		V2 = np.delete(V2, index)
		return t,V1,V2
	else:
		return t,V1

