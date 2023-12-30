import sys

input_file_name = sys.argv[1] if len(sys.argv) > 1 else "movie-links.txt"
output_file_name =  sys.argv[2] if len(sys.argv) > 2 else "movie-links.txt"

with open(input_file_name, "r", encoding='latin1') as input_file, open(output_file_name, "w") as output_file:
    lines = input_file.readlines()
    my_dict = {}

    for line in lines:
        page1, page2 = line.strip().split(' --> ')
        my_dict.setdefault(page1, []).append(page2)

    for key, values in my_dict.items():
        output_file.write(f"{key}\t1\t{','.join(values)}\n")
