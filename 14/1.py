from sys import stdin
from typing import *

def solve(line):    
    line = ["#"] + line
    n = len(line)
    for i in range(n):
        if line[i] == "#":
            free = i + 1
        elif line[i] == "O":
            line[i] = "."
            line[free] = "O"
            free += 1
    ans = 0
    for i in range(n):
        ans += n - i if line[i] == "O" else 0
    return ans

grid = []
for i, line in enumerate(stdin):
    grid.append([c for c in line.rstrip()])

ans = 0
for line in zip(*grid):
    ans += solve(list(line))
print(ans)