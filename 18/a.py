from sys import stdin
from typing import *

"""
    This solution utilizes shoelace formula and pick's theorem.
"""


def shoelace(borders: List[Tuple[int, int]]):
    """ Returns the area of the loop """
    loop = borders.copy() + [borders[0]]
    lSum, rSum = 0, 0
    for i in range(len(loop) - 1):
        lSum += loop[i][0] * loop[i+1][1]
        rSum += loop[i][1] * loop[i+1][0]
    return abs(lSum - rSum) / 2


toDirection = "RDLU"
plan: List[Tuple[str, str, str]] = []
for i, line in enumerate(stdin):
    direction, length, color = line.split()
    plan.append((toDirection.index(direction), int(length), color))


ans1, ans2 = 0, 0
for part2 in [False, True]:
    graph = [(0, 0)]
    edges = 0
    for (direction, length, color) in plan:
        ny, nx = graph[-1]
        if part2:
            length = int(color[color.find("#") + 1:-2], 16)
            direction = int(color[-2])
        directions = ((length, 0), (0, length), (-length, 0), (0, -length))
        dx, dy = directions[direction]
        ny += dy
        nx += dx

        edges += length
        graph.append((ny, nx))
    A = shoelace(graph)
    B = len(graph)

    # A = area, I = internal nodes, B = border nodes
    # Pick's theorem states that A = I + B/2 - 1
    interior = int(A - (edges/2) + 1)  # Inverted Pick's theorem
    if part2:
        ans2 = edges + interior
    else:
        ans1 = edges + interior

print(ans1, ans2)
