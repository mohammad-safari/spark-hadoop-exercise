import sys

# Initialize distance as infinity
INF = float("inf")

# Initialize variables to track the current node and its neighbors
current_dist = None
current_node = None
current_path = None
current_neighbours = 0


def emit_update_node_info_that_is_no_longer_updating(
    current_node, current_distance, current_neighbors
):
    if current_node is not None:
        # Emit the node with its updated distance and neighbors
        print(f"{current_node}\t{current_distance}\t{current_neighbors}")


for line in sys.stdin:
    # Parse input
    parts = line.strip().split('\t')

    node = parts[0]
    distance = parts[1]
    if len(parts) == 3:
        # The line corresponds to a "child" distance update information.
        path = parts[2]
        neighbours = 0
    if len(parts) == 4:
        # Else, it's a complete node.
        path = parts[3]
        neighbours = parts[2] if parts[2] != "0" else 0

    try:
        distance = int(distance)
    except ValueError:
        continue

    # For each node, collect all distance updates. If a new distance is smaller
    # than the current one, update the node distance and the path

    if current_node == node:
        # If one of the parents of the node provides a quicker path, choose it
        if distance < current_dist:
            current_dist = distance
            current_path = path
        # Don't assume that the full node line will come first : update neigh-
        # bour info as soon as it is available
        if neighbours != 0:
            current_neighbours = neighbours
    else:
        # We change nodes, so we output the result of the reduce process for the
        # last one
        if current_node:
            print(f'{current_node}\t{current_dist}\t{current_neighbours}\t{current_path}')
        current_node = node
        current_dist = distance
        current_path = path
        current_neighbours = neighbours

if current_node == node:
    print (f'{current_node}\t{current_dist}\t{current_neighbours}\t{current_path}')
