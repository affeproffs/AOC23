import math
from sys import stdin
from typing import *
import re

total = 0
histories: List[List[int]] = []
for i, line in enumerate(stdin):
    histories.append(list(map(int,line.strip().split(" "))))

for history in histories:
    sequences = [history.copy()]
    # Construct sequences
    while sequences[-1].count(0) != len(sequences[-1]):
        newSequence = []
        for i, number in enumerate(sequences[-1][:-1]):
            newSequence.append(sequences[-1][i+1] - number)        
        sequences.append(newSequence)

    sequences[-1].append(0)
    sequences.reverse()
    for i, sequence in enumerate(sequences):
        if (i == 0):
            continue        
        sequences[i].insert(0, sequence[0] - sequences[i-1][0])    
    total += sequences[-1][0]

print(total)