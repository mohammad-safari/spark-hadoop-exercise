import sys
import csv

MAX_VALUE="10000000"

input_file_name = sys.argv[1] if len(sys.argv) > 1 else 'graph-cze.csv'
output_file_name =  sys.argv[2] if len(sys.argv) > 2 else 'graph-cze.txt'

with open(input_file_name, 'r', newline='') as input_file, open(output_file_name, 'w') as output_file:
    csvreader = csv.reader(input_file, delimiter=';')
    header = next(csvreader)
    my_dict = {}

    for row in csvreader:
        key = row[0]
        value = f"{row[1]}:{row[2]}"
        my_dict.setdefault(key, []).append(value)

    # select min node as start node
    min_key = min(my_dict.keys())
    min = min_key
    # also include destination
    # flat_values = [i for j in my_dict.values() for i in j]
    # min_value = min([value.split(":")[0] for value in flat_values])
    # min = min(min_value, min_key)

    for key, values in my_dict.items():
        value = ','.join(values)
        output_file.write(f'{key}\t0\t{value}\n' if key == min else f'{key}\t{MAX_VALUE}\t{value}\n')
