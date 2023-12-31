#!/usr/bin/env python3
import sys

# Initialize distance as infinity
INF = float("inf")

def parse_input(line):
    parts = line.strip().split("\t")
    node = parts[0]
    distance = parts[1]
    # Set neighbours variable non zero if the node has any
    neighbours = parts[2] if len(parts) > 2 and parts[2] != "0" else 0
    # Propagate computed path at previous step, or set beginning of path
    path = parts[3] if len(parts) == 4 else node
    return node, distance, neighbours, path


def emit_node_info_and_graph_path(node, distance, neighbors, path):
    if neighbors is not None:
        print(f"{node}\t{distance}\t{neighbors}\t{path}")
    else:
        print(f"{node}\t{distance}\t{path}")


if __name__ == "__main__":
    for line in sys.stdin:
        (
            current_node,
            current_distance,
            reachable_neighbours,
            current_path,
        ) = parse_input(line)

        try:
            current_distance = int(current_distance)
        except ValueError:
            continue

        emit_node_info_and_graph_path(
            current_node, current_distance, reachable_neighbours, current_path
        )

        # If the any other node is reachable, emit distances to neighbors
        propagating_neighbors = [
            neighbour.strip().split(":", 1)
            for neighbour in (
                reachable_neighbours.strip().split(",") if reachable_neighbours else []
            )
        ]

        def filter_integer_distance(_, distance):
            return isinstance(int(distance), int)

        def preserve_neighbor_reach_path(neighbor_node, neighbor_distance):
            return (
                neighbor_node,
                current_distance + int(neighbor_distance),
                "{}>{}".format(current_path, str(neighbor_node)),
            )

        filtered_propagating_neighbors = list(
            filter(lambda tuple: filter_integer_distance(*tuple), propagating_neighbors)
        )
        filtered_propagating_neighbors_with_path = map(
            lambda tuple: preserve_neighbor_reach_path(*tuple),
            filtered_propagating_neighbors,
        )

        for (
            neighbor_node,
            neighbor_distance,
            neighbor_path,
        ) in filtered_propagating_neighbors_with_path:
            emit_node_info_and_graph_path(
                neighbor_node, neighbor_distance, None, neighbor_path
            )
