from sys import stdin
from typing import *

def HASH(s):
    result = 0
    for char in s:
        result += ord(char)
        result *= 17
        result = result % 256
    return result

def addLense(s: str):
    dash = s.find("-")
    operation = "=" if dash == -1 else "-"    
    if operation == "-":
        label = s[:dash]
        box = HASH(label)
        if label in boxes[box]:
            boxes[box].pop(label)
    else:
        label, focal = s.split("=")
        box = HASH(label)
        boxes[box][label] = int(focal)

def score(boxes):
    total = 0
    for i, box in enumerate(boxes):
        for j, value in enumerate(box.values()):            
            total += (i + 1) * (j + 1) * value
    return total


hashes = []
for i, line in enumerate(stdin):
    hashes.extend(line.rstrip().split(","))

boxes = [{} for _ in range(256)] # [box][label] => value
for h in hashes:
    addLense(h)
print(score(boxes))