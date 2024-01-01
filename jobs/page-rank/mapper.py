#!/usr/bin/env python3
import sys
import os

TOTAL_NODES = os.getenv("TOTAL_NODES", 3)
DAMPING_FACTOR = os.getenv("DAMPING_FACTOR", 0.85)

def parse_input(line):
    parts = line.strip().split("\t")
    return parts[0], parts[1], parts[2] if len(parts) > 1 else None


def emit_rank(page, page_rank, adjacency_list):
    if not adjacency_list:
        print(f"{page}\t{page_rank}")
    else:
        print(f"{page}\t{page_rank}\t{','.join(adjacency_list)}")


for line in sys.stdin:
    current_page, current_page_rank, current_adjacency_list = parse_input(line)

    try:
        current_page_rank = float(current_page_rank)
    except ValueError:
        continue

    # emit the original structure
    current_adjacency_list = current_adjacency_list.split(",")
    emit_rank(current_page, DAMPING_FACTOR/TOTAL_NODES, current_adjacency_list)

    # distribute this page effect to page rank neigbors neighbors
    propagating_page_rank_effect = current_page_rank / len(current_adjacency_list)
    for neighbor in current_adjacency_list:
        emit_rank(neighbor, propagating_page_rank_effect, None)
