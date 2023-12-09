from sys import stdin
from typing import *

histories: List[List[int]] = []
for i, line in enumerate(stdin):
    histories.append(list(map(int,line.strip().split(" "))))

ans1, ans2 = 0, 0
for part1 in [True, False]:
    for history in histories:
        if not part1:
            history.reverse()
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
            sequences[i].append(sequences[i-1][-1] + sequence[-1])   
             
        if part1: ans1 += sequences[-1][-1]
        if not part1: ans2 += sequences[-1][-1]        

print(ans1, ans2)