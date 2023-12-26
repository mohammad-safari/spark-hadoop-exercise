import sys

data = [tuple(line.strip().split("\t")) for line in sys.stdin]
data.sort(key=lambda x: x[0])
for row in data:
    print(row[0], row[1], row[2], sep="\t")
