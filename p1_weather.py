import csv

# return the Manhattan distance between two dictionary data points from the data set
def manhattan_distance(data_point1, data_point2):
	x1 = data_point1['TMAX']
	x2 = data_point2['TMAX']
	y1 = data_point1['PRCP']
	y2 = data_point2['PRCP']
	z1 = data_point1['TMIN']
	z2 = data_point2['TMIN']
	
	d = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
	return d

# return a list of data point dictionaries read from the specified file	
def read_dataset(filename):
	all_rows = []
	with open(filename, 'r') as f:
		reader = csv.DictReader(f, delimiter=' ', fieldnames = ['DATE', 'TMAX', 'PRCP', 'TMIN', 'RAIN'])
		for row in reader:
			col1 = row['DATE']
			col2 = row['TMAX']
			col2_float= float(col2)
			col3 = row['PRCP']
			col3_float= float(col3)
			col4 = row['TMIN']
			col4_float= float(col4)
			col5 = row['RAIN']
			col = {'DATE':col1, 'TMAX':col2_float, 'PRCP':col3_float, 'TMIN':col4_float, 'RAIN':col5}
			all_rows.append(col)
	return all_rows	


# return a prediction of whether it is raining or not based on a majority vote of the list of neighbors
def majority_vote(nearest_neighbors):
	count_true = 0
	count_false = 0	
	for i in nearest_neighbors:
		if i['RAIN'] == 'TRUE':
			count_true += 1
		if i['RAIN'] == 'FALSE':
			count_false += 1

	if count_true > count_false:
		return 'TRUE'
	else:
		return 'FALSE'

# return the majority vote prediction for whether it's raining or not on the provided test point by using above functions.
def k_nearest_neighbors(filename, test_point, k, year_interval):
	from datetime import datetime
	from datetime import timedelta

	# Filter the list of dictionary points that are within the year interval
	filtered = []
	test_date = datetime.strptime(test_point['DATE'], '%Y-%m-%d')
	reader = read_dataset(filename)
	for row in reader:
		date = datetime.strptime(row['DATE'], '%Y-%m-%d')	
		interval = timedelta(days = 365 * year_interval)
		
		if test_date - interval <= date <= test_date + interval:
			filtered.append(row)	

	# Make a list of tuple of the closest points using the manhattan distance.	
	filtered_dist = []
	for data in filtered:
		d = manhattan_distance(data, test_point)	
		a = (data, d)
		filtered_dist.append(a)

	# check for a majority vote with the list of the closest neighbors.
	ans = sorted(filtered_dist, key = lambda x: x[1])
	final_list = []
	for items in ans:
		final_list.append(items[0])
	k_nearest_list = final_list[:k]
	return majority_vote(k_nearest_list)



"""
if __name__ == "__main__":
	dataset = read_dataset("rain.txt")
	print(len(dataset))
	print(dataset[0])
	print(manhattan_distance({'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'}, {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'}))



	print(majority_vote([{'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'},
{'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'},
{'DATE': '2014-12-05', 'TMAX': 55.0, 'PRCP': 0.12, 'TMIN': 44.0, 'RAIN': 'TRUE'},
{'DATE': '1954-09-08', 'TMAX': 71.0, 'PRCP': 0.02, 'TMIN': 55.0, 'RAIN': 'TRUE'},
{'DATE': '2014-08-27', 'TMAX': 84.0, 'PRCP': 0.0, 'TMIN': 61.0, 'RAIN': 'FALSE'}]))
	
	print(k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX':51.0, 'PRCP': 0.47, 'TMIN': 42.0}, 4, 10))

	print(k_nearest_neighbors('rain.txt', {'DATE': '1950-01-01', 'TMAX':51.0, 'PRCP': 0.47, 'TMIN': 42.0}, 7, 2))
"""
