from sys import stdin
from typing import *

def transpose(m):
    newM = [[c for c in line] for line in m]
    return ["".join(l) for l in list(zip(*newM))]

def diff(s1, s2):
    return sum([1 for c1, c2 in zip(s1,s2) if c1 != c2])

def hasReflection(pattern):
    l, r = 0, 1
    usedSmudge = False
    result = 0
    while l >= 0 and r < len(pattern):
        differance = diff(pattern[l], pattern[r])        
        # Found a match!
        if differance == 0 or differance == 1 and not usedSmudge:
            result += 1
            l -= 1
            if differance == 1:
                usedSmudge = True
        else:
            result = 0
            l = r
            usedSmudge = False
        r += 1    

    if (result != 0 and r == len(pattern)):
        return r - result, usedSmudge        
    return result, usedSmudge

patterns = [[]]
for i, line in enumerate(stdin):
    if (line.count("#") != 0 or line.count(".") != 0):
        patterns[-1].append(line.rstrip())
    else:
        patterns.append([])

horizontal, vertical = 0, 0
for pattern in patterns:
    # Top to bottom
    hori, smudge = hasReflection(pattern)
    if hori and smudge: 
        horizontal += hori
        continue

    # Bottom to top
    hori, smudge = hasReflection(list(reversed(pattern)))
    if hori and smudge:         
        horizontal += len(pattern) - hori
        continue

    transposed = transpose(pattern) # Switch rows and cols
    
    # Left to right
    vert, smudge = hasReflection(transposed)
    if vert and smudge: 
        vertical += vert
        continue
    
    # Right to left
    vert, smudge = hasReflection(list(reversed(transposed)))
    if vert and smudge: 
        vertical += len(transposed) - vert
        continue

    assert False, f"Should never happen. Found no solution using smudge, pattern: {pattern}"

total = vertical + (horizontal * 100) 
print(total)