import sys
import csv

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

    for key, values in my_dict.items():
        value = ','.join(values)
        output_file.write(f'{key}\t0\t{value}\n' if key == '1' else f'{key}\t10000000\t{value}\n')
