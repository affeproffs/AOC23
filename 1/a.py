from sys import stdin
import re

toNumber = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

total = 0
for line in stdin:
    a = re.findall(
        r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    toAdd = int(str(toNumber[a[0]]) + str(toNumber[a[-1]]))
    total += toAdd
print(total)
