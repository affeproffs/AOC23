from sys import stdin


def addRangeToQueue(workflow, condition, x, m, a, s):
    """
        for values which condition is true -> add to queue with possible xmas-values
        for values which condition is false -> modify xmas-values and continue
    """
    category, sign, value = condition[0], condition[1], int(
        condition[2:])
    categories = [x, m, a, s]
    c = "xmas".find(category)
    mini, maxi = categories[c]
    if sign == "<":
        nMaxi = value - 1
        categories[c] = (mini, nMaxi)
        queue.append((workflow, *categories))
        mini = value
    elif sign == ">":
        nMini = value + 1
        categories[c] = (nMini, maxi)
        queue.append((workflow, *categories))
        maxi = value
    categories[c] = (mini, maxi)
    return categories


workflows = {}  # name --> [conditions]
for line in stdin:
    if len(line.rstrip()) == 0:
        break

    name = line[:line.find("{")]
    conditions = line.rstrip()[line.find("{") + 1:-1].split(",")
    workflows[name] = conditions


# (workflow name, x, m, a, s)
queue = [("in", (1, 4000), (1, 4000), (1, 4000), (1, 4000))]
total = 0
while len(queue):
    workflow, (xMin, xMax), (mMin, mMax), (aMin,
                                           aMax), (sMin, sMax) = queue.pop(0)
    if workflow == "A":
        total += (xMax-xMin+1) * (mMax-mMin+1) * (aMax-aMin+1) * (sMax-sMin+1)
        continue
    elif workflow == "R":
        continue

    rules = workflows[workflow]
    for rule in rules:
        isLastRule = ":" not in rule
        if isLastRule:
            queue.append((rule, (xMin, xMax), (mMin, mMax),
                          (aMin, aMax), (sMin, sMax)))
        else:
            nextWorkflow = rule[rule.find(":")+1:]
            condition: str = rule[:rule.find(":")]

            (xMin, xMax), (mMin, mMax), (aMin, aMax), (sMin, sMax) = addRangeToQueue(
                nextWorkflow, condition, (xMin, xMax), (mMin, mMax), (aMin, aMax), (sMin, sMax))


print(total)
