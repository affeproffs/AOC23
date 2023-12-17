from functools import cache
from sys import stdin
from typing import *

@cache
def moveRocks(line):
    line = ["#"] + list(line)
    n = len(line)
    for i in range(n):
        if line[i] == "#":
            free = i + 1
        elif line[i] == "O":
            line[i] = "."
            line[free] = "O"
            free += 1

    return line[1:]

def getAns(grid):
    ans = 0
    for i, line in enumerate(grid):
        ans += (len(grid) - i) * line.count("O")
    return ans

grid = []
for i, line in enumerate(stdin):
    grid.append((c for c in line.rstrip()))

grid = tuple(grid)
visited = {}
loop = []
for cycle in range(1_000_000_000):    
    if (grid in visited):
        if grid in loop:
            break # Found a complete cycle, e.g. A -> B -> C -> A
        loop.append(grid)
        grid = visited[grid]
        continue
    originalGrid = grid

    northTilt = [moveRocks(line) for line in zip(*grid)]
    westTilt = [moveRocks(line) for line in zip(*northTilt)]        
    southTilt = [moveRocks(line) for line in zip(*reversed(westTilt))]            
    eastTilt = [tuple(reversed(moveRocks(line))) for line in reversed(list(zip(*reversed(southTilt))))]
    grid = tuple(eastTilt)
    visited[originalGrid] = grid
    loop.clear()

remaining = 1_000_000_000 - cycle
finalGrid = loop[remaining % len(loop)]
print(getAns(finalGrid))