import csv

from datetime import datetime, timedelta


def manhattan_distance(data_point1, data_point2):
    x1 = data_point1['PRCP']
    x2 = data_point2['PRCP']

    y1 = data_point1['TMAX']
    y2 = data_point2['TMAX']

    z1 = data_point1['TMIN']
    z2 = data_point2['TMIN']

    d = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
    return d

def read_dataset(filename):
    dataset = []
    with open(filename, 'r') as f:
        dictreader = csv.DictReader(f, delimiter=' ', fieldnames=['DATE', 'PRCP', 'TMAX', 'TMIN', 'RAIN'])
        for row in dictreader:
            # row is an OrderedDict, but seems like we need a regular dict
            entry = {'DATE': row['DATE'],
                     'PRCP': float(row['PRCP']),
                     'TMAX': float(row['TMAX']),
                     'TMIN': float(row['TMIN']),
                     'RAIN': row['RAIN']}
            dataset.append(entry)
    return dataset

def majority_vote(nearest_neighbors):
    votes = {'TRUE': 0,
             'FALSE': 0}

    for neighbor in nearest_neighbors:
        rain = neighbor['RAIN']
        votes[rain] += 1

    if votes['TRUE'] >= votes['FALSE']:
        return 'TRUE'
    else:
        return 'FALSE'

def k_nearest_neighbors(filename, test_point, k, year_interval):
    dataset = read_dataset(filename)

    # Filter out invalid data points that are interval or more years away from input test point
    valid_dataset = []
    for data_point in dataset:
        # Parse DATE into a Python Datetime object
        date_data_point = datetime.strptime(data_point['DATE'], '%Y-%m-%d')
        date_test_point = datetime.strptime(test_point['DATE'], '%Y-%m-%d')
        if (date_data_point < date_test_point + timedelta(days=365 * 10) and
            date_data_point > date_test_point - timedelta(days=365 * 10)):
            valid_dataset.append(data_point)

    # Create a list of tuples where first entry is the data point dictionary and second entry is the distance
    neighbors = []
    for data_point in valid_dataset:
        d = manhattan_distance(data_point, test_point)
        neighbors.append((data_point, d))

    # Sort the neighbors by their distance
    neighbors_sorted = sorted(neighbors, key=lambda x: x[1])

    # Find the closest k valid neighbors by using the Manhattan distance
    k_neighbors = []
    for i in range(k):
        data_tuple = neighbors_sorted[i]  # (data_tuple dictionary, distance)
        data_point = data_tuple[0]
        k_neighbors.append(data_point)

    # Finally, return their majority vote on whether it's raining or not in the test point
    return majority_vote(k_neighbors)


def main():
    # print(manhattan_distance({'DATE': '1951-05-19', 'TMAX': 66.0, 'PRCP': 0.0, 'TMIN': 43.0, 'RAIN': 'FALSE'},{'DATE': '1951-01-27', 'TMAX': 33.0, 'PRCP': 0.0, 'TMIN': 19.0, 'RAIN': 'FALSE'}))
    # print(manhattan_distance({'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'}, {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'}))

    # dataset = read_dataset('rain.txt')
    # print(len(dataset))
    # print(dataset[0])

    # print(majority_vote([{'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'},
    #                      {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'},
    #                      {'DATE': '2014-12-05', 'TMAX': 55.0, 'PRCP': 0.12, 'TMIN': 44.0, 'RAIN': 'TRUE'},
    #                      {'DATE': '1954-09-08', 'TMAX': 71.0, 'PRCP': 0.02, 'TMIN': 55.0, 'RAIN': 'TRUE'},
    #                      {'DATE': '2014-08-27', 'TMAX': 84.0, 'PRCP': 0.0, 'TMIN': 61.0, 'RAIN': 'FALSE'}]))
    print(k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0}, 2, 10))
    print(k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0}, 2, 10))



if __name__ == '__main__':
    main()
