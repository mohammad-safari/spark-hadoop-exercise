#!/usr/bin/env python3
import sys

# Initialize distance as infinity
INF = float("inf")

# Initialize variables to track the optimizing node and its neighbors
# for case that partition-reducer mapping is not one to one
optimizing_dist = None
optimizing_node = None
optimizing_path = None
optimizing_neighbours = 0


def parse_input(line):
    parts = line.strip().split("\t")
    node = parts[0]
    distance = parts[1]
    # the line corresponds to a "child" distance update information.
    # else, it's a complete node.
    path, neighbours = (
        (parts[2], 0)
        if len(parts) == 3
        else (parts[3], parts[2] if parts[2] != "0" else 0)
    )
    return node, distance, neighbours, path


def emit_node_info_and_graph_path(node, distance, neighbors, path):
    if node:
        print(f"{node}\t{distance}\t{neighbors}\t{path}")


for line in sys.stdin:
    current_node, current_distance, current_neighbours, current_path = parse_input(line)

    try:
        current_distance = int(current_distance)
    except ValueError:
        continue

    if optimizing_node != current_node:
        # emit best path to prevous node till here if available
        emit_node_info_and_graph_path(
            optimizing_node, optimizing_dist, optimizing_neighbours, optimizing_path
        )
        optimizing_node, optimizing_dist, optimizing_path, optimizing_neighbours = (
            current_node,
            current_distance,
            current_path,
            current_neighbours,
        )
        continue

    if current_distance < optimizing_dist:
        optimizing_dist, optimizing_path = current_distance, current_path
    # due to consistency of neighbors for each node,
    # and some incomplete node info produced by mapper
    # update neighbours info as soon as it is available
    if current_neighbours != 0:
        optimizing_neighbours = current_neighbours

emit_node_info_and_graph_path(
    optimizing_node, optimizing_dist, optimizing_neighbours, optimizing_path
)
