from sys import stdin
from typing import *

grid = []
for i, line in enumerate(stdin):
    grid.append([c for c in line.rstrip()])

for y in range(len(grid)):
    for x in range(len(line)):
        if grid[y][x] == "S":
            sY, sX = y,x

queue = [(sY, sX)]
grid[sY][sX] = "."
for steps in range(64):    
    nPlots = set({})
    while len(queue):
        y, x = queue.pop(0)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in directions:
            nY, nX = y + d[0], x + d[1]
            if nY < 0 or nY >= len(grid) or nX < 0 or nX >= len(grid[0]):
                continue
            if grid[nY][nX] == ".":
                nPlots.add((nY, nX))
    queue = list(nPlots)
print(len(queue))