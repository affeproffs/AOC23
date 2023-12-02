from sys import stdin

res = 0
for line in stdin:
    MAX_RED = 0
    MAX_GREEN = 0
    MAX_BLUE = 0   
    tokens = line.split()
    gameId = int(tokens[1][:-1])
    sets = tokens[2::]
    for i in range(0, len(sets) - 1, 2):
        amount, color = sets[i], sets[i+1]
        if ("red" in color and int(amount) > MAX_RED):
            MAX_RED = int(amount)
        elif ("blue" in color and int(amount) > MAX_BLUE):
            MAX_BLUE = int(amount)
        elif ("green" in color and int(amount) > MAX_GREEN):
            MAX_GREEN = int(amount)
    res += MAX_BLUE * MAX_GREEN * MAX_RED

print(res)