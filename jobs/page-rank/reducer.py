#!/usr/bin/env python3
import sys
import os

current_page = None
current_page_rank = 0.0
current_adjacency_list = {}

DAMPING_FACTOR = os.getenv("DAMPING_FACTOR", 0.85)
TOTAL_NODES = os.getenv("TOTAL_NODES", 3)


def parse_input(line):
    parts = line.strip().split("\t")
    page, page_rank, adjacency_list = (
        parts[0],
        parts[1],
        parts[2] if len(parts) > 2 else None,
    )
    return page, page_rank, adjacency_list


def calculate_and_emit_rank(current_page, current_page_rank, adjacency_list):
    if current_page is not None:
        new_page_rank = (
            DAMPING_FACTOR / TOTAL_NODES + (1 - DAMPING_FACTOR) * current_page_rank
        )
        print(f"{current_page}\t{new_page_rank}\t{adjacency_list}")


for line in sys.stdin:
    page, page_rank, adjacency_list = parse_input(line)

    try:
        page_rank = float(page_rank)
    except ValueError:
        continue

    if page != current_page:
        # emit the updated page rank and original structure before changing current page
        calculate_and_emit_rank(current_page, current_page_rank, current_adjacency_list)
        # change current page to new page
        current_page, current_page_rank, current_adjacency_list = (
            page,
            page_rank,
            adjacency_list,
        )
        continue

    # update the current page's rank
    current_page_rank += page_rank
    if adjacency_list:
        # due to consistency of adjacent for each node,
        # and some incomplete info(effects) produced by mapper
        # update neighbours info as soon as it is available
        current_adjacency_list = adjacency_list

calculate_and_emit_rank(current_page, current_page_rank, current_adjacency_list)