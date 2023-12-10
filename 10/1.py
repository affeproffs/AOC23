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
    for j in range(len(lines)):
        if lines[i][j] == "S":
            sY, sX = i, j
            break

pipeMap = {
    "left": ["-", "J", "7", "S"],
    "right": ["-", "L", "F", "S"],
    "down": ["|", "7", "F", "S"],
    "up": ["|", "L", "J", "S"],
}
pipes = ["|", "-", "L", "J", "7", "F"]


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
while not isDone:
    neighbourPipes = getNeighbourPipes(*curr)
    print("visiting:", curr, lines[curr[0]][curr[1]])
    steps += 1
    visited.add(curr)
    for pipe in neighbourPipes:
        y, x, o = pipe
        # print("neighbouring pipe:", pipe)
        if (o == "S" and steps > 2):
            isDone = True
            break
        if ((y, x) not in visited):
            curr = (y, x)


print("Final steps:", steps / 2)
