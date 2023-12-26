import sys

# Initialize distance as infinity
INF = float("inf")

for line in sys.stdin:
    if "id" in line:
        continue
    # Parse CSV input
    node, neighbor, distance, _ = line.strip().split(";")
    try:
        distance = int(distance)
    except ValueError:
        distance = INF

    # Emit the node and its current distance
    print(f"{node}\t{distance}\t{neighbor}")

    # If the distance is not infinity(reachable), emit distances to neighbors
    if distance < INF:
        print(f"{neighbor}\t{distance}\t{{}}")  # Empty neighbors for the reducer
