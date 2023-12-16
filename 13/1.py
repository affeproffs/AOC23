from sys import stdin
from typing import *

def transpose(m):
    newM = []
    for line in m:
        newM.append([])
        for c in line:
            newM[-1].append(c)
    return ["".join(l) for l in list(zip(*newM))]

def hasReflection(pattern):
    l, r = 0, 1
    result = 0
    while l >= 0 and r < len(pattern):
        # Found a match!
        if pattern[l] == pattern[r]:
            result += 1
            l -= 1
        else:
            result = 0
            l = r
        r += 1
    if (result != 0):
        if l < 0:
            return result
        return r - result    
    return result

patterns = [[]]
for i, line in enumerate(stdin):
    if (line.count("#") != 0 or line.count(".") != 0):
        patterns[-1].append(line.rstrip())
    else:
        patterns.append([])

hori, vert = 0, 0
for pattern in patterns:
    horizontal = hasReflection(pattern)
    transposed = transpose(pattern)
    vertical = hasReflection(transposed)
    if horizontal: hori += horizontal
    if vertical: vert += vertical
total = vert + (hori * 100)
print(total)