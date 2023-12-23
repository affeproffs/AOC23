from sys import stdin
from typing import *

total = 0
isWorkflow = True
workflows = {}  # name --> [conditions]
parts = []
for i, line in enumerate(stdin):
    if len(line.rstrip()) == 0:
        isWorkflow = not isWorkflow
        continue
    if isWorkflow:
        name = line[:line.find("{")]
        conditions = line.rstrip()[line.find("{") + 1:-1].split(",")
        workflows[name] = conditions
    else:
        x, m, a, s = line.rstrip()[1:-1].split(",")
        parts.append(tuple([int(item[2:]) for item in [x, m, a, s]]))

total = 0
for part in parts:
    x, m, a, s = part
    workflow = "in"
    res = ""
    while res != "R" and res != "A":
        rules = workflows[workflow]
        for rule in rules:
            isLastRule = ":" not in rule
            if isLastRule:
                res = rule
            else:
                res = rule[rule.find(":")+1:]
                condition: str = rule[:rule.find(":")]
                condition = condition.replace("x", str(x))
                condition = condition.replace("m", str(m))
                condition = condition.replace("a", str(a))
                condition = condition.replace("s", str(s))
                isTrue = eval(condition)
                if isTrue:
                    break

        if res == "A":
            total += sum(part)
        elif res != "R":
            workflow = res

print(total)
