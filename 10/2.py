from sys import stdin
from typing import *

ans1, ans2 = 0, 0
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

innerDirection = {
    "down": "left",
    "right": "down",
    "up": "right",
    "left": "up",
}
pipeMap = {
    "left": ["-", "J", "7", "S"],
    "right": ["-", "L", "F", "S"],
    "down": ["|", "7", "F", "S"],
    "up": ["|", "L", "J", "S"],
}
pipes = ["|", "-", "L", "J", "7", "F"]


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


visited = set()
isDone = False
steps = 0
curr = (sY, sX)

# Idea: keep track of "inner side", e.g. going down in beginning it's "right", etc
"""
    inner:
        down -> right
        right -> up
        up -> left
        left -> down

    # check inner direction:
        - Are you part of main loop? continue
        - Have we already counted you? continue
        - else:
            - add to list of potential enclosed tiles
            - continue in same direction until we meet tile in main loop
                if we find such tile, add the distance travelled
                also add all such tiles to alreadyCounted
"""
mainLoop = []
while not isDone:
    neighbourPipes = getNeighbourPipes(*curr)
    # print(lines[curr[0]][curr[1]])
    steps += 1
    visited.add(curr)
    mainLoop.append(curr)
    for pipe in neighbourPipes:
        y, x, o = pipe
        # print("neighbouring pipe:", pipe)
        if (o == "S" and steps > 2):
            isDone = True
            break
        if ((y, x) not in visited):
            curr = (y, x)
            # break

counted = set()


def findEnclosure(innerCords, direction):
    potentialTiles = [innerCords]
    curr = innerCords
    y, x = curr
    logging = False
    # Keep track of # of times a tile is visited in this function
    # if the count == 4 -> add it to counted
    try:
        while curr not in visited:
            y, x = curr
            if (y == 5 and x == 8):
                logging = True
            if (logging):
                print("visiting", curr)
            lines[y][x]  # To throw error if we go outside bounds

            if direction == "right":
                curr = (y, x+1)
            elif direction == "left":
                curr = (y, x-1)
            elif direction == "up":
                curr = (y-1, x)
            elif direction == "down":
                curr = (y+1, x)
            else:
                assert False, "Direction not allowed"
            potentialTiles.append(curr)
    except:
        return

    if (logging):
        print("potential tiles:", potentialTiles)
    for tile in potentialTiles:
        print("potential tile:", tile, lines[tile[0]][tile[1]])
        if (tile not in visited):
            print("tile added:", tile)
            counted.add(tile)


""" 
Starts from top left.
foundStart = False
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (foundStart):
            break
        if (y, x) in visited:
            sY, sX = y, x
            foundStart = True
    if (foundStart):
        break """


""" print(mainLoop)
i = mainLoop.index((sY, sX))
print("Index:", i)
mainLoop = mainLoop[i:] + mainLoop[:i]
print(mainLoop) """

for i, step in enumerate(mainLoop[1:]):
    direction = getDirection(mainLoop[i], mainLoop[i+1])
    inner = innerDirection[direction]
    innerCords = getInnerCords(step, inner)
    """ if (innerCords in visited):
        continue """
    """ elif (innerCords in counted):
        continue """
    # Potential enclosure
    findEnclosure(innerCords, inner)
    """ print(lines[step[0]][step[1]], direction, inner,
          lines[innerCords[0]][innerCords[1]]) """


def getNeighbourCords(y, x):
    return [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]


minY, minX = len(lines), len(lines[0])
maxY, maxX = 0, 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y, x) in visited:
            maxY = max(maxY, y)
            maxX = max(maxX, x)
            minY = min(minY, y)
            minX = max(minX, x)

""" for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y > maxY or x > maxX or y < minY or x < minX):
            continue 
        if (not y or not x or y == len(lines) - 1 or x == len(lines[0]) - 1):
            continue
        isZero = (y, x) not in visited and (y, x) not in counted
        if not isZero:
            continue
        surroundingCords = getNeighbourCords(y, x)
        nextToEnclosed = False
        surroundedByEnclosed = len(list(filter(bool,
                                               map(lambda cord: cord in counted, surroundingCords))))

        if surroundedByEnclosed >= 2:
            nextToEnclosed = True
        # for cord in surroundingCords:
        #   if cord in counted:
        #       nextToEnclosed = True
        if nextToEnclosed:
            counted.add((y, x)) """


def debugPrint():
    print("BEFORE")
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            print(lines[y][x], end="")
        print("")

    print("\n\nAFTER")
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (y, x) not in visited and (y, x) not in counted:
                print("O", end="")
            elif (y, x) in visited:
                print(lines[y][x], end="")
            elif (y, x) in counted:
                print("I", end="")
        print("")


debugPrint()
print(len(counted))
