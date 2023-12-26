import sys

# Initialize distance as infinity
INF = float("inf")

# Initialize variables to track the current node and its neighbors
current_node = None
current_distance = INF
current_neighbors = {}


def emit_update_node_info_that_is_no_longer_updating(
    current_node, current_distance, current_neighbors
):
    if current_node is not None:
        # Emit the node with its updated distance and neighbors
        print(f"{current_node}\t{current_distance}\t{current_neighbors}")


for line in sys.stdin:
    # Parse input
    node, distance, neighbor = line.strip().split("\t")
    try:
        distance = int(distance)
    except ValueError:
        distance = INF

    # Update information if a new node is encountered
    if node != current_node:
        emit_update_node_info_that_is_no_longer_updating(
            current_node, current_distance, current_neighbors
        )
        # Reset variables for the new node
        current_node = node
        current_distance = INF
        current_neighbors = {}

    # Update distance and neighbors
    if distance < current_distance:
        current_distance = distance
    current_neighbors[neighbor] = distance

# Emit the last node
emit_update_node_info_that_is_no_longer_updating(
    current_node, current_distance, current_neighbors
)
