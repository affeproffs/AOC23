from sys import stdin
from typing import *

def getNeighbourPipes(y, x):
    o = lines[y][x]

    upO = (y-1, x, lines[y-1][x])
    upValid = upO[-1] in pipeMap["down"] and o in pipeMap["up"]

    leftO = (y, x-1, lines[y][x-1])
    leftValid = leftO[-1] in pipeMap["right"] and o in pipeMap["left"]

    rightO = (y, x+1, lines[y][x+1])
    rightValid = rightO[-1] in pipeMap["left"] and o in pipeMap["right"]

    downO = (y+1, x, lines[y+1][x])
    downValid = downO[-1] in pipeMap["up"] and o in pipeMap["down"]

    objects = [(upO, upValid), (leftO, leftValid),
               (rightO, rightValid), (downO, downValid)]
    return list(map(lambda o: o[0], filter(lambda o: o[1], objects)))

# Returns the area of the loop
def shoelace(borders: List[Tuple[int, int]]):
    loop = borders.copy() + [borders[0]]
    lSum, rSum = 0, 0
    for i in range(len(loop) - 1):        
        lSum += loop[i][0] * loop[i+1][1]
        rSum += loop[i][1] * loop[i+1][0]
    return abs(lSum - rSum) / 2

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

visited = set()
loop = []
isDone = False
steps = 0
curr = (sY, sX)
while not isDone:
    neighbourPipes = getNeighbourPipes(*curr)    
    steps += 1
    visited.add(curr)
    loop.append(curr)
    for pipe in neighbourPipes:
        y, x, o = pipe        
        if (o == "S" and steps > 2):
            isDone = True
            break
        if ((y, x) not in visited):
            curr = (y, x)

A = shoelace(loop)
B = len(loop)

# A = area, I = internal nodes, B = border nodes
# Pick's theorem --> A = I + B/2 - 1
I = int(A - (B/2) + 1) # Inverted Pick's theorem

ans1 = steps // 2
ans2 = I

print("part 1:", ans1)
print("part 2:", ans2) 
