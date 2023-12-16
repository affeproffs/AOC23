from sys import stdin
from typing import *

def transpose(m):
    newM = [[c for c in line] for line in m]
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
    if (result != 0 and r == len(pattern)):
        return r - result
    return result

patterns = [[]]
for i, line in enumerate(stdin):
    if (line.count("#") != 0 or line.count(".") != 0):
        patterns[-1].append(line.rstrip())
    else:
        patterns.append([])

horizontal, vertical = 0, 0
for pattern in patterns:
    hori = hasReflection(pattern)
    transposed = transpose(pattern)
    vert = hasReflection(transposed)
    if hori: horizontal += hori
    if vert: vertical += vert
total = vertical + (horizontal * 100)
print(total)