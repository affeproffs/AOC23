from sys import stdin
from typing import *

def manhattanDist(p1, p2, expansion):
    baseDistance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    # Check how many expanded rows/cols we pass
    rowsPassed = 0
    for row in rowsToExpand:
        if p1[0] < row < p2[0] or p2[0] < row < p1[0]:
            rowsPassed += 1
    colsPassed = 0
    for col in colsToExpand:
        if p1[1] < col < p2[1] or p2[1] < col < p1[1]:
            colsPassed += 1
    return baseDistance + ((colsPassed + rowsPassed) * expansion) - ((colsPassed + rowsPassed) if expansion > 1 else 0)

ans1, ans2 = 0, 0
image = []
for i, line in enumerate(stdin):
    image.append(line.rstrip())

# find row, cols to expand
rowsToExpand, colsToExpand = [], []
for y in range(len(image)):
    shouldExpand = True
    for x in range(len(image[0])):
        if image[y][x] != ".":
            shouldExpand = False
            break
    if shouldExpand: rowsToExpand.append(y)

for x in range(len(image[0])):
    shouldExpand = True
    for y in range(len(image)):
        if image[y][x] != ".":
            shouldExpand = False
            break
    if shouldExpand: colsToExpand.append(x)

# galaxy number => (y, x)
galaxies = {}
galaxyCount = 1
for y in range(len(image)):
    for x in range(len(image[0])):
        if image[y][x] == "#":
            galaxies[galaxyCount] = (y, x)
            galaxyCount += 1

for fromGalaxy in galaxies.keys():    
    toGalaxy = fromGalaxy + 1    
    while toGalaxy < galaxyCount:
        ans1 += manhattanDist(galaxies[fromGalaxy], galaxies[toGalaxy], 1)
        ans2 += manhattanDist(galaxies[fromGalaxy], galaxies[toGalaxy], 1_000_000)        
        toGalaxy += 1

print(ans1, ans2)