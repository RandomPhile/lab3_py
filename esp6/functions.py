import numpy as np
import csv

def data_from_csv(name_csv,two_channels=True):
	t = np.array([])
	V1 = np.array([])
	V2 = np.array([])

	with open(name_csv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)

		skip = 0
		for row in reader:
			if skip >= 1:
				t = np.append(t, float(row['x-axis']))
				V1 = np.append(V1, float(row['1']))
				if two_channels:
					V2 = np.append(V2, float(row['2']))
			skip += 1
	if two_channels:
		return t,V1,V2
	else:
		return t,V1