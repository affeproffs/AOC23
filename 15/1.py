from sys import stdin
from typing import *

def HASH(s):
    result = 0
    for char in s:
        result += ord(char)
        result *= 17
        result = result % 256
    return result
ans1, ans2 = 0, 0

hashes = []
for i, line in enumerate(stdin):
    hashes.extend(line.rstrip().split(","))

for h in hashes:
    ans1 += HASH(h)
print(ans1, ans2)