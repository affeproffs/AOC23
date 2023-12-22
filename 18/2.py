from sys import stdin
from typing import *


ans1, ans2 = 0, 0

toDirection = {
    0: "R",
    1: "D",
    2: "L",
    3: "U"
}


def shoelace(borders: List[Tuple[int, int]]):
    """ Returns the area of the loop """
    loop = borders.copy() + [borders[0]]
    lSum, rSum = 0, 0
    for i in range(len(loop) - 1):
        lSum += loop[i][0] * loop[i+1][1]
        rSum += loop[i][1] * loop[i+1][0]
    return abs(lSum - rSum) / 2


plan: List[Tuple[str, str, str]] = []
for i, line in enumerate(stdin):
    direction, length, color = line.split()
    plan.append((direction, length, color))


graph = [(0, 0)]
edges = 0
for (direction, length, color) in plan:
    ny, nx = graph[-1]
    length = int(color[color.find("#") + 1:-2], 16)
    direction = toDirection[int(color[-2])]
    print(length, direction)
    if (direction == "R"):
        nx += int(length)
    elif (direction == "L"):
        nx -= int(length)
    elif (direction == "U"):
        ny -= int(length)
    elif (direction == "D"):
        ny += int(length)
    else:
        assert False, "Unknown direction"
    edges += int(length)
    graph.append((ny, nx))


print(graph)
A = shoelace(graph)
B = len(graph)

# A = area, I = internal nodes, B = border nodes
# Pick's theorem --> A = I + B/2 - 1
I = int(A - (edges/2) + 1)  # Inverted Pick's theorem
ans1 = edges + I
print(ans1, ans2)
