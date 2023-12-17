from sys import stdin
from typing import *


def solve(grid, start):
    queue = [start]
    visited = set({})
    while len(queue):
        curr = queue.pop(0)
        y, x, direction = curr
        if (y < 0 or y > Y or x < 0 or x > X):
            continue
        if curr in visited:
            continue

        visited.add(curr)
        o = grid[y][x]

        if direction == RIGHT:
            if o == "." or o == "-":
                queue.append((y, x + 1, RIGHT))
            elif o == "|":
                queue.append((y - 1, x, UP))
                queue.append((y + 1, x, DOWN))
            elif o == "/":
                queue.append((y - 1, x, UP))
            elif o == "\\":
                queue.append((y + 1, x, DOWN))
        elif direction == DOWN:
            if o == "." or o == "|":
                queue.append((y + 1, x, DOWN))
            elif o == "-":
                queue.append((y, x + 1, RIGHT))
                queue.append((y, x - 1, LEFT))
            elif o == "/":
                queue.append((y, x - 1, LEFT))
            elif o == "\\":
                queue.append((y, x + 1, RIGHT))
        elif direction == LEFT:
            if o == "." or o == "-":
                queue.append((y, x - 1, LEFT))
            elif o == "|":
                queue.append((y - 1, x, UP))
                queue.append((y + 1, x, DOWN))
            elif o == "/":
                queue.append((y + 1, x, DOWN))
            elif o == "\\":
                queue.append((y - 1, x, UP))
        elif direction == UP:
            if o == "." or o == "|":
                queue.append((y - 1, x, UP))
            elif o == "-":
                queue.append((y, x + 1, RIGHT))
                queue.append((y, x - 1, LEFT))
            elif o == "/":
                queue.append((y, x + 1, RIGHT))
            elif o == "\\":
                queue.append((y, x - 1, LEFT))

    return len(set((y, x) for y, x, _ in visited))  # Discard the direction


grid = []
for i, line in enumerate(stdin):
    grid.append(line.rstrip())

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
Y = len(grid) - 1
X = len(grid[0]) - 1

ans1 = solve(grid, (0, 0, RIGHT))
ans2 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if y == 0:  # Top row
            ans2 = max(ans2, solve(grid, (y, x, DOWN)))
        elif y == Y:  # Bottom row
            ans2 = max(ans2, solve(grid, (y, x, UP)))
        if x == 0:  # Leftmost column
            ans2 = max(ans2, solve(grid, (y, x, RIGHT)))
        elif x == X:  # Rightmost column
            ans2 = max(ans2, solve(grid, (y, x, LEFT)))

print(ans1, ans2)
