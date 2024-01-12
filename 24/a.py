from sys import stdin


def intersects(p1, p2):
    p1x, p1y, _, p1xv, p1yv, _ = p1
    p2x, p2y, _, p2xv, p2yv, _ = p2
    dx = p2x - p1x
    dy = p2y - p1y
    det = p2xv * p1yv - p2yv * p1xv
    if det == 0:
        return False
    u = (dy * p2xv - dx * p2yv) / det
    v = (dy * p1xv - dx * p1yv) / det
    return (u, v) if u > 0 and v > 0 else False


hails = []
for i, line in enumerate(stdin):
    at = line.find("@")
    x, y, z = map(int, line[:at].split(","))
    vx, vy, vz = map(int, line.rstrip()[at+1:].split(","))
    hails.append((x, y, z, vx, vy, vz))


minCord = 200000000000000
maxCord = 400000000000000
intersections = 0
for i, p1 in enumerate(hails):
    for p2 in hails[i+1:]:
        inter = intersects(p1, p2)
        if inter:
            u, v = inter
            x, y = p2[0] + p2[3] * v, p2[1] + p2[4] * v

            if minCord <= x <= maxCord and minCord <= y <= maxCord:
                intersections += 1

print(intersections)
