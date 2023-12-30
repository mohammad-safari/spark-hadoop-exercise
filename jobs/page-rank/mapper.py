#!/usr/bin/env python3
import sys

DAMPING_FACTOR = 0.85
TOTAL_NODES = 5  # Update with the actual number of nodes in your graph

for line in sys.stdin:
    parts = line.strip().split('\t')
    page, page_rank, adjacency_list = parts[0], parts[1], parts[2] if len(parts)>1 else None

    # Convert values to float for calculations
    page_rank = float(page_rank)
    adjacency_list = adjacency_list.split(",")

    # Emit the original structure
    print(f"{page}\t{page_rank}\t{','.join(adjacency_list)}")

    # Distribute PageRank to neighbors
    if adjacency_list:
        pagerank_value = DAMPING_FACTOR / TOTAL_NODES + (1 - DAMPING_FACTOR) * (page_rank / len(adjacency_list))
        for neighbor in adjacency_list:
            print(f"{neighbor}\t{pagerank_value}\t{','.join(adjacency_list)}")  # Empty adjacency list

    # Handle nodes with no outgoing links
    if not adjacency_list:
        pagerank_value = DAMPING_FACTOR / TOTAL_NODES
        print(f"{page}\t{pagerank_value}\t{','.join(adjacency_list)}")  # Emit a placeholder value for nodes with no outgoing links
