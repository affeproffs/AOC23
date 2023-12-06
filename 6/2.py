from sys import stdin
from typing import *
import re


total = 1
allInput = []
for i, line in enumerate(stdin):
    afterColon = line[line.find(":")+1::].rstrip()
    numbers = re.findall(r"\d+", afterColon)
    allInput.append(int("".join(numbers)))

time, distance = allInput
ways = 0
# find cutoff with binarysearch?
# *2+1?
l, r = 0, time
while (l < r):
    m = (l + r) // 2
    if (m * (time - m) > distance):
        r = m
    else:
        l = m + 1
total = time - (l * 2)

print(total + 1)
