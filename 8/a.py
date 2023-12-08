import math
from sys import stdin
from typing import *
import re

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

total = 0
path = ""
maps = {}
for i, line in enumerate(stdin):
    if (i == 0):
        path = line.rstrip()
    if (i >1):
        line = line.rstrip()
        start = line[:3]
        left, right = line[7:len(line)-1].split(", ")
        maps[start] = (left, right)

pathIndex = 0
curr = list(filter(lambda k: k.endswith("A"), maps.keys()))
startingNodes = curr.copy()
stepsCount = {}

while len(stepsCount.keys()) != len(startingNodes):
    for i, c in enumerate(curr):
        if c.endswith("Z") and stepsCount.get(c) == None:
            stepsCount[startingNodes[i]] = total
    curr = [maps[c][0 if path[pathIndex] == "L" else 1] for c in curr]
    pathIndex = (pathIndex + 1)  % len(path)
    total += 1

values = stepsCount.values() 
total = 1
for value in values:
    total = lcm(total, value)
print(total)