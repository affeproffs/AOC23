from sys import stdin
from typing import *
import re

"""
    Return the whole number found in the schematic at line and character index
"""
def findNumber(line, characterIndex):
    for number in re.finditer(r'\d+', line):
        if number.end() >= characterIndex:
            return int(number.group())

schematic: List[str] = []
for line in stdin:
    schematic.append(f".{line.rstrip()}.")
lineLength = len(schematic[0])
schematic.insert(0, "." * lineLength)
schematic.append("." * lineLength)

total = 0
for i, line in enumerate(schematic):
    for star in re.finditer(r'\*', line):
        startingIndex = star.start()
        endingIndex = star.end()
        charactersAbove = schematic[i-1][startingIndex-1:endingIndex + 1]
        sideCharacters = line[startingIndex-1] + "." + line[endingIndex]
        charactersBelow = schematic[i+1][startingIndex-1:endingIndex + 1]
        surroundingCharacters = [charactersAbove, sideCharacters, charactersBelow]        
        totalSurroundingNumbers = 0
        for characters in surroundingCharacters:
            totalSurroundingNumbers += len(re.findall(r'\d+', characters))        
        
        if (totalSurroundingNumbers == 2):
            gearRatio = 1
            for number in re.finditer(r'\d+', charactersAbove):
                gearRatio *= findNumber(schematic[i-1], startingIndex + number.start())
            for number in re.finditer(r'\d', sideCharacters):
                if (number.start() == 0):
                    gearRatio *= findNumber(schematic[i], startingIndex - 1)
                else:
                    gearRatio *= findNumber(schematic[i], startingIndex + 1)                
            for number in re.finditer(r'\d+', charactersBelow):

                gearRatio *= findNumber(schematic[i+1], startingIndex + number.start())    
            total += gearRatio

print(total)