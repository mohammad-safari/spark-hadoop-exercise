import sys

# Initialize distance as infinity
INF = float("inf")

for line in sys.stdin:
    # Parse CSV input
    parts = line.strip().split("\t")
    node = parts[0]
    distance = parts[1]
    # Set neighbours variable only if the node has some
    neighbours = parts[2] if len(parts) > 2 and parts[2] != "0" else 0
    # Propagate computed path at previous step, or set beginning of path
    path = parts[3] if len(parts) == 4 else node

    try:
        distance = int(distance)
    except ValueError:
        continue

    # Emit the node and its current distance to keep the graph structure for future iterations
    print(f"{node}\t{distance}\t{neighbours}\t{path}")

    # If the any other node is reachable, emit distances to neighbors
    if neighbours:
        neighbours = neighbours.strip().split(",")

        # For each neighbor, print its updated distance to the source node
        for neighbour in neighbours:
            neighbor_node, neighbor_distance = neighbour.strip().split(":", 1)

            try:
                neighbor_distance = int(neighbor_distance)
            except ValueError:
                continue

            neighbor_distance += distance
            neighbor_path = "{}>{}".format(path, str(neighbor_node))

            print(f"{neighbor_node}\t{neighbor_distance}\t{neighbor_path}")
