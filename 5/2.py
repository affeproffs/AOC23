from sys import stdin
from typing import *
import re


total = 0
seeds: Set[Tuple[int]] = set({})
maps: List[List[int]] = []
for i, line in enumerate(stdin):
    if (i == 0):
        allSeeds = list(map(int, line[line.find(":") + 2::].split()))
        for idx in range(0, len(allSeeds), 2):
            seeds.add((allSeeds[idx], allSeeds[idx+1] - 1))
    else:
        isNewMap = line.find("map")        
        if (isNewMap != -1):
            maps.append([])
            continue
        
        values = line.split(" ")        
        if (len(values) != 3):
            continue

        destination, source, range = map(int, values)
        maps[len(maps)-1].append([destination, source, range])

for newMap in maps:
    newSeeds = set({})
    for seed in seeds:
        minSeed = seed[0]
        seedRange = seed[1]
        maxSeed = minSeed + seedRange
        
        mappedRanges = set({})
        for mapper in newMap:
            destination, source, range = mapper
           
            # If seed is below mapper or seed is above mapper range
            if maxSeed < source or minSeed > source + range:
                continue

            # Some overlap achieved at this point.
            overlapMin = max(minSeed, source)
            overlapMax = min(maxSeed, source + range)
            diff = overlapMin - source
            newSeed = destination + diff
            newSeeds.add((destination + diff, overlapMax - overlapMin))
            mappedRanges.add((overlapMin, overlapMax - overlapMin))

        # If no overlap was found, re-add the same seed
        if (len(mappedRanges) == 0):
            newSeeds.add(seed)
        else:
            # Find any span in minseed + seedrange that is not in mappedRanges
            mappedRangesCopy = list(mappedRanges)
            minReach = mappedRangesCopy[0][0]
            maxReach = mappedRangesCopy[-1][0] + mappedRangesCopy[-1][1]

            # Anything below minReach needs to be added to newSeeds
            if minReach > minSeed:                
                newSeeds.add((minSeed, minReach - minSeed))

            # Anything above maxReach needs to be added to newSeeds
            if maxReach < maxSeed:
                newSeeds.add((maxReach + 1, maxSeed - maxReach))
    seeds = newSeeds.copy()

# For some reason the answer was the 2nd seed in the list, not the first.
print(min(seeds), sorted(seeds))