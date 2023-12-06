from sys import stdin
from typing import *
import re


total = 1
allInput = []
for i, line in enumerate(stdin):
    allInput.append(list(map(int,list(filter(bool, line[line.find(":")+1::].rstrip().split(" "))))))

for time, distance in zip(allInput[0], allInput[1]):
    ways = 0
    for holdingTime in range(time):
        travelTime = time - holdingTime
        travelDistance = travelTime * holdingTime
        
        if (travelDistance > distance):
            ways += 1
    #print(time, ways)
    total *= ways
    

print(total)