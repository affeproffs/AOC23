from sys import stdin
from typing import *
import re

schematic: List[str] = []
for line in stdin:
    schematic.append(f".{line.rstrip()}.")
lineLength = len(schematic[0])
schematic.insert(0, "." * lineLength)
schematic.append("." * lineLength)

total = 0
for i, line in enumerate(schematic):
    for number in re.finditer(r'\d+', line):        
        startingIndex = number.start()
        endingIndex = number.end()
        charactersAbove = schematic[i-1][startingIndex-1:endingIndex + 1]
        sideCharacters = line[startingIndex-1] + line[endingIndex]
        charactersBelow = schematic[i+1][startingIndex-1:endingIndex + 1]
        surroundingCharacters = charactersAbove + sideCharacters + charactersBelow
        totalSurroundingNumbers = sum(map(len, re.findall(r'\d+', surroundingCharacters)))
        isPartNumber = surroundingCharacters.count(".") + totalSurroundingNumbers != len(surroundingCharacters)
        if (isPartNumber):
            total += int(number.group())
        

print(total)