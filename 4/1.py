from sys import stdin
from typing import *
import re


total = 0
for line in stdin:    
    winningNumbersStart = line.find(":")
    winningNumbersEnd = line.find("|")
    winningNumbers = set(map(int, line[winningNumbersStart+2:winningNumbersEnd-1].split()))

    ourNumbers = list(map(int, line[winningNumbersEnd+1::].split()))
    points = 0
    for number in ourNumbers:
        if number in winningNumbers:
            if (not points):
                points = 1
            else:
                points *= 2
    total += points

print(total)