#!/usr/bin/env python3
import sys

current_page = None
current_page_rank = 0.0
current_adjacency_list = {}

DAMPING_FACTOR = 0.85
TOTAL_NODES = 5  # Update with the actual number of nodes in your graph

for line in sys.stdin:
    parts = line.strip().split('\t')
    page, page_rank, adjacency_list = parts[0], parts[1], parts[2] if len(parts)>1 else None

    # Convert values to float for calculations
    page_rank = float(page_rank)
    adjacency_list = adjacency_list.split(",")

    # Update the current page's PageRank
    if page == current_page:
        current_page_rank += page_rank
    else:
        if current_page is not None:
            # Emit the updated PageRank and original structure
            new_page_rank = DAMPING_FACTOR / TOTAL_NODES + (1 - DAMPING_FACTOR) * current_page_rank
            print(f"{current_page}\t{current_page_rank}\t{','.join(adjacency_list)}")

        # Reset for the new page
        current_page = page
        current_page_rank = page_rank
        current_adjacency_list = adjacency_list

# Emit the last page's information
new_page_rank = DAMPING_FACTOR / TOTAL_NODES + (1 - DAMPING_FACTOR) * current_page_rank
print(f"{current_page}\t{current_page_rank}\t{','.join(adjacency_list)}")
