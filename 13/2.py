from sys import stdin
from typing import *

def transpose(m):
    newM = []
    for line in m:
        newM.append([])
        for c in line:
            newM[-1].append(c)
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


hori, vert = 0, 0
for pattern in patterns:
    horizontal, horiSmudge = hasReflection(pattern)
    if horizontal and horiSmudge: 
        hori += horizontal
        continue

    # try starting from the back
    horizontal, horiSmudge = hasReflection(list(reversed(pattern)))    
    if horizontal and horiSmudge:         
        hori += len(pattern) - horizontal
        continue

    transposed = transpose(pattern) # Switch rows and cols
    
    vertical, vertSmudge = hasReflection(transposed)
    if vertical and vertSmudge: 
        vert += vertical
        continue
    
    # try starting from the back
    vertical, vertSmudge = hasReflection(list(reversed(transposed)))
    if vertical and vertSmudge: 
        vert += len(transposed) - vertical
        continue

    assert False, f"Should never happen. Found no solution using smudge, pattern: {pattern}"

total = vert + (hori * 100) 
print(total)


