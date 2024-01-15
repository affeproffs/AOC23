from collections import defaultdict, deque
from sys import stdin


def findPaths(component):
    """
        BFS and count which wires are crossed.
    """
    visited = set()
    curr = component
    q = deque([('dummy', curr)])

    while q:
        prev, curr = q.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        c1, c2 = sorted([prev, curr])
        visCount[c2][c1] += 1
        for connected in connections[curr]:
            q.append((curr, connected))
    return visited


connections = defaultdict(set)
for i, line in enumerate(stdin):
    left, right = line.rstrip().split(":")
    for to in right.split():
        connections[left].add(to)
        connections[to].add(left)

"""
    Traverse from every component to every other component,
    keep track of # of times a wire is crossed.

    Cut the most crossed wire. Repeat 3x.
"""
components = list(connections.keys())
for i in range(3):
    visCount = defaultdict(lambda: defaultdict(int))

    for c in components:
        findPaths(c)

    fromC, connectedTo = sorted(
        visCount.items(), key=lambda i: max(i[1].values()))[-1]
    toC = max(connectedTo.items(), key=lambda i: i[1])[0]
    # Cut the wire
    connections[fromC].discard(toC)
    connections[toC].discard(fromC)

groups = []
for c in components:
    group = findPaths(c)
    if group not in groups:
        groups.append(group)
assert len(groups) == 2, f"Found more than 2 groups, was {len(groups)}"
print(len(groups[0]) * len(groups[1]))
