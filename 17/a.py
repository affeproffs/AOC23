from heapq import heapify, heappop, heappush
from sys import stdin
from typing import *

INF = 1_000_000_000

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

oppositeDirection = {
    RIGHT: LEFT,
    LEFT: RIGHT,
    DOWN: UP,
    UP: DOWN
}


def debug(path):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in path:
                print("#", end="")
            else:
                print(grid[y][x], end="")
        print()


def findMinHeatLoss(grid, maxC, minC):
    # (heatloss, y, x, direction, consecutive, path)
    queue = [(grid[1][0], 1, 0, DOWN, 1, [(0, 0)]),
             (grid[0][1], 0, 1, RIGHT, 1, [(0, 0)])]
    heapify(queue)

    # [y][x][direction][consecutive]
    heat = [[[[INF for _ in range(maxC + 1)] for _ in range(
        4)] for _ in grid[0]] for _ in grid]

    while len(queue):
        (heatloss, y, x, direction, consecutive, path) = heappop(queue)
        if heat[y][x][direction][consecutive] != INF:
            continue
        heat[y][x][direction][consecutive] = heatloss
        if (y == len(grid) - 1 and x == len(grid[0]) - 1):
            if consecutive >= minC:
                return heatloss, path + [(y, x)]
            continue
        heat[y][x][direction][consecutive] = heatloss

        possibleDirections = [RIGHT, DOWN, LEFT,
                              UP] if consecutive >= minC else [direction, oppositeDirection[direction]]
        possibleDirections.remove(oppositeDirection[direction])
        if (consecutive == maxC):
            possibleDirections.remove(direction)

        for newDirection in possibleDirections:
            if newDirection == UP:
                ny, nx = y-1, x
            elif newDirection == DOWN:
                ny, nx = y+1, x
            elif newDirection == RIGHT:
                ny, nx = y, x+1
            elif newDirection == LEFT:
                ny, nx = y, x-1
            if ny < 0 or ny == len(grid) or nx < 0 or nx == len(grid[0]):
                continue

            newHeatloss = heatloss + grid[ny][nx]
            newConsecutive = (
                consecutive + 1) if newDirection == direction else 1
            heappush(queue, (newHeatloss, ny, nx,
                             newDirection, newConsecutive, path + [(y, x)]))

    assert False, "Did not find a solution"


grid = []

for i, line in enumerate(stdin):
    grid.append([int(c) for c in line.strip()])

ans1, path1 = findMinHeatLoss(grid, 3, 1)
ans2, path2 = findMinHeatLoss(grid, 10, 4)

""" 
print("Part 1 path:")
debug(path1)
print("Part 2 path:")
debug(path2) 
"""

print(ans1, ans2)
