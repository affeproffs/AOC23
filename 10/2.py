from sys import stdin
from typing import *

def getDirection(curr, next):
    fromY, fromX = curr
    toY, toX = next

    if toX > fromX:
        return "right"
    elif toX < fromX:
        return "left"
    elif toY > fromY:
        return "down"
    else:
        return "up"


def getInnerCords(curr, innerDir):
    y, x = curr
    if (innerDir == "up"):
        return (y-1, x)
    if (innerDir == "down"):
        return (y+1, x)
    if (innerDir == "left"):
        return (y, x-1)
    if (innerDir == "right"):
        return (y, x+1)


def getNeighbourPipes(y, x):
    currO = lines[y][x]

    upO = (y-1, x, lines[y-1][x])
    upValid = upO[-1] in pipeMap["down"] and currO in pipeMap["up"]

    leftO = (y, x-1, lines[y][x-1])
    leftValid = leftO[-1] in pipeMap["right"] and currO in pipeMap["left"]

    rightO = (y, x+1, lines[y][x+1])
    rightValid = rightO[-1] in pipeMap["left"] and currO in pipeMap["right"]

    downO = (y+1, x, lines[y+1][x])
    downValid = downO[-1] in pipeMap["up"] and currO in pipeMap["down"]

    objects = [(upO, upValid), (leftO, leftValid),
               (rightO, rightValid), (downO, downValid)]
    return list(map(lambda o: o[0], filter(lambda o: o[1], objects)))

lines = []
for i, line in enumerate(stdin):
    lines.append("." + line.strip() + ".")

lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))

sX, sY = 0, 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            sY, sX = i, j
            break


pipeMap = {
    "left": ["-", "J", "7", "S"],
    "right": ["-", "L", "F", "S"],
    "down": ["|", "7", "F", "S"],
    "up": ["|", "L", "J", "S"],
}

visited = set()
isDone = False
steps = 0
curr = (sY, sX)
while not isDone:
    neighbourPipes = getNeighbourPipes(*curr)
    steps += 1
    visited.add(curr)  
    for pipe in neighbourPipes:
        y, x, o = pipe
        if (o == "S" and steps > 2):
            isDone = True
            break
        if ((y, x) not in visited):
            curr = (y, x)
            break

count = 0
""" A point is inside the enclosed loop if it isn't part of the loop,
    AND there are a odd number of vertical pipes to the left of it. 
"""
for y in range(len(lines)):
    isEnclosed = False
    for x in range(len(lines[0])):
        cord = (y, x)
        o = lines[y][x]        
        if cord in visited and (o == '|' or o == '7' or o == 'F' or o == "S"):
            isEnclosed = not isEnclosed        
        count += 1 if cord not in visited and isEnclosed else 0        

print(count)