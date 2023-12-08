import math
from sys import stdin
from typing import *
import re

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
curr = "AAA"
while not curr.endswith("Z"):    
    curr = maps[curr][0 if path[pathIndex] == "L" else 1]
    pathIndex = (pathIndex + 1)  % len(path)
    total += 1

print(total)