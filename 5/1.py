from sys import stdin
from typing import *
import re


total = 0
seeds = []
maps: List[List[int]] = []
for i, line in enumerate(stdin):
    if (i == 0):
        seeds = list(map(int, line[line.find(":") + 2::].split()))
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
    newSeeds = []
    for seed in seeds:
        foundMap = False
        #print("Seed:", seed)
        # Find source map, if none -> add original
        for mapper in newMap:
            destination, source, range = mapper
            #print(destination, source, range)
            if (seed >= source and seed <= source + range):
                diff = seed - source
                newSeed = destination + diff
                #print(f"Found match in map for seed: {seed}, map: {mapper}, new seed: {newSeed}")
                if (newSeed == 42):
                    print("Here we add 42")
                newSeeds.append(newSeed)
                foundMap = True
                continue
        if not foundMap:
            newSeeds.append(seed)
    print(newSeeds)
    seeds = newSeeds

print(min(seeds), seeds)
    

#print(total)