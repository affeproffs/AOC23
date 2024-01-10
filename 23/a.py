from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

graph = []
for i, line in enumerate(stdin):
    graph.append([c for c in line.rstrip()])

y, x = 0, graph[0].index(".")
slopes = ["^", "v",  "<", ">",]
m, n = len(graph), len(graph[0])


def traverse(y, x, steps, visited, part1):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if ((y, x) in visited):
        return 0
    elif y < 0 or y == m or x < 0 or x == n:
        return 0
    elif graph[y][x] == "#":
        return 0
    elif part1 and graph[y][x] in slopes:
        si = slopes.index(graph[y][x])
        directions = [directions[si]]
    elif y == m - 1:
        # Found end
        return steps

    visited.add((y, x))
    attempts = []
    for yd, xd in directions:
        ny = y + yd
        nx = x + xd
        attempts.append(traverse(ny, nx, steps + 1, visited, part1))
    visited.discard((y, x))
    return max(attempts)


ans1, ans2 = traverse(y, x, 0, set(), True), traverse(y, x, 0, set(), False)
print(ans1, ans2)
