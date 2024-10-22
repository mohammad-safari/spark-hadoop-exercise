#!/usr/bin/env python3
import sys

current_page = None
current_page_rank = 0.0
current_adjacency_list = {}

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
        if adjacency_list:
            print(f"{current_page}\t{current_page_rank}\t{adjacency_list}")
        else:
            print(f"{current_page}\t{current_page_rank}")


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