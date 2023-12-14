from functools import cache
from sys import stdin, setrecursionlimit
from typing import *

setrecursionlimit(10000)

@cache
def attempt(springs: str, groups: tuple[int]):
    if len(groups) == 0:
        if springs.count("#") == 0:
            return 1
        return 0
    brokenSpringsToPlace = sum(groups) + len(groups) - 1 
    if brokenSpringsToPlace > len(springs):
        return 0

    childrenAttempts = 0
    isDot = springs[0] == "."
    isQuestionMark = springs[0] == "?"
    
    if isDot or isQuestionMark: 
        childrenAttempts += attempt(springs[1:], groups) # Replacing "?" and "." with "."

    # Find and replace immediate ?#-chain
    dotStart = springs.find(".")
    if (dotStart == -1): dotStart = 3e9
    dotsInTheWay = dotStart < groups[0]
    if dotsInTheWay:
        return childrenAttempts
        
    atEnd = len(springs) <= groups[0]
    inTheMiddle = len(springs) > groups[0]
    # Found valid placement of next chain of "#"
    if (atEnd or (inTheMiddle and springs[groups[0]] != "#")):
        groupCopy = list(groups)
        groupCopy.pop(0)
        childrenAttempts += attempt(springs[groups[0]+1:], tuple(groupCopy), ) # Replacing "?" and "#" with "#"
    return childrenAttempts    


lines: List[Tuple[str, List[int]]] = []
for i, line in enumerate(stdin):
    line = line.rstrip()
    springs, groups = line.split()
    lines.append((springs, list(map(int,groups.split(",")))))

ans1, ans2 = 0, 0
for i, line in enumerate(lines):
    springs, groups = line    
    part1 = attempt(springs, tuple(groups))
    part2 = attempt("?".join([springs] * 5), tuple(groups * 5))
    ans1 += part1
    ans2 += part2
    print(f"Line {i + 1}, answer part 1: {part1}, part 2: {part2}")
    
print(ans1, ans2)
