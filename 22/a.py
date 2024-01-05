from copy import deepcopy
from functools import cache
import heapq
import random
from string import ascii_letters
from sys import stdin
from typing import *


def moveBrick(start, end, name):
    if abs(start[0] - end[0]) > 0:  # Z changing
        lz, hz = min(start[0], end[0]), max(start[0], end[0])
        y, x = start[1], start[2]
        for z in range(lz, hz + 1):
            taken[z][y][x] = name
    elif abs(start[1] - end[1]) > 0:  # Y changing
        ly, hy = min(start[1], end[1]), max(start[1], end[1])
        z, x = start[0], start[2]
        for y in range(ly, hy + 1):
            taken[z][y][x] = name
    elif abs(start[2] - end[2]) > 0:  # X changing
        lx, hx = min(start[2], end[2]), max(start[2], end[2])
        z, y = start[0], start[1]
        for x in range(lx, hx + 1):
            taken[z][y][x] = name
    else:
        assert start == end, f"Some weird brick: {start}-{end}"
        z, y, x = start
        taken[z][y][x] = name


def addBrick(*args): moveBrick(*args)


def removeBrick(*args): moveBrick(*args, name=None)


def blocksInRange(start, end, name):
    blocks = set({})
    if abs(start[0] - end[0]) > 0:  # Z changing
        lz, hz = min(start[0], end[0]), max(start[0], end[0])
        y, x = start[1], start[2]
        for z in range(lz, hz + 1):
            if taken[z][y][x]:
                blocks.add(taken[z][y][x])
    elif abs(start[1] - end[1]) > 0:  # Y changing
        ly, hy = min(start[1], end[1]), max(start[1], end[1])
        z, x = start[0], start[2]
        for y in range(ly, hy + 1):
            if taken[z][y][x]:
                blocks.add(taken[z][y][x])
    elif abs(start[2] - end[2]) > 0:  # X changing
        lx, hx = min(start[2], end[2]), max(start[2], end[2])
        z, y = start[0], start[1]
        for x in range(lx, hx + 1):
            if taken[z][y][x]:
                blocks.add(taken[z][y][x])
    else:
        assert start == end, f"Some weird brick: {start}-{end}"
        z, y, x = start
        if taken[z][y][x]:
            blocks.add(taken[z][y][x])
    blocks.discard(name)
    return blocks


def fallingBricks(name, supports, standsOn):
    @cache
    def falling(name):
        bricks = set([name])
        if name not in supports:
            return bricks
        onMe = supports[name].copy()
        for brick in onMe:
            supports[name].discard(brick)
            standsOn[brick].discard(name)
            bricksItStandsOn = standsOn[brick]
            if len(bricksItStandsOn) == 0:
                bricks.update(falling(brick))
        return bricks

    fallen = falling(name)
    fallen.discard(name)
    return len(fallen)


bricks = []  # z, y, x
for i, line in enumerate(stdin):
    tilde = line.find("~")
    start = reversed(line[:tilde].split(","))
    end = reversed(line.rstrip()[tilde+1:].split(","))
    heapq.heappush(bricks, (tuple(map(int, start)),
                   tuple(map(int, end)), "".join(random.choice(ascii_letters) for _ in range(10))))

taken = [[[None for _ in range(10)] for _ in range(10)]
         for _ in range(350)]  # taken[z][y][x]

for start, end, name in bricks:
    addBrick(start, end, name)


# Construct settled bricks
settledBricks = []
while bricks:
    newBricks = []
    while bricks:
        start, end, name = heapq.heappop(bricks)
        if start[0] == 1 or end[0] == 1:  # Touching ground
            heapq.heappush(settledBricks, (start, end, name))
            continue
        # Try to go lower
        nStart = (start[0] - 1, start[1], start[2])
        nEnd = (end[0] - 1, end[1], end[2])
        blockingBlocks = blocksInRange(nStart, nEnd, name)
        if blockingBlocks:
            # Can't go lower
            heapq.heappush(settledBricks, (start, end, name))
            continue
        removeBrick(start, end)
        addBrick(nStart, nEnd, name)
        heapq.heappush(newBricks, (nStart, nEnd, name))
    bricks = newBricks

supports = {}
standsOn = {}
for (start, end, name) in settledBricks:
    nStart = (start[0] - 1, start[1], start[2])
    nEnd = (end[0] - 1, end[1], end[2])
    blocksUnder = blocksInRange(nStart, nEnd, name)
    for bu in blocksUnder:
        if bu not in supports:
            supports[bu] = set()
        if name not in standsOn:
            standsOn[name] = set()
        supports[bu].add(name)
        standsOn[name].add(bu)

ans1, ans2 = 0, 0
while settledBricks:
    _, _, name = heapq.heappop(settledBricks)
    if name in supports:
        bricksOnMe = supports[name]
        for brick in bricksOnMe:
            bricksItStandsOn = standsOn[brick]
            if len(bricksItStandsOn) <= 1:
                # Would cause bricks to fall
                ans2 += fallingBricks(name, deepcopy(supports),
                                      deepcopy(standsOn))
                break
        else:
            ans1 += 1
    else:
        ans1 += 1

print(ans1, ans2)
