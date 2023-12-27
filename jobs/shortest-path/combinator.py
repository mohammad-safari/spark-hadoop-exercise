import sys

current_node = None
current_distance = float('inf')
current_neighbors = {}

for line in sys.stdin:
    node, distance, neighbors = line.strip().split('\t')
    distance = int(distance)
    neighbors = eval(neighbors)  # Convert string to dictionary

    if node != current_node:
        if current_node is not None:
            print(f"{current_node}\t{current_distance}\t{current_neighbors}")

        current_node = node
        current_distance = float('inf')
        current_neighbors = {}

    if distance < current_distance:
        current_distance = distance
    current_neighbors.update(neighbors)

if current_node is not None:
    print(f"{current_node}\t{current_distance}\t{current_neighbors}")
