from sys import stdin
from typing import *

LOW = 0
HIGH = 1

# dict[name] => ["%" or "&", [destinations], status (on/off for flipflop, {name: mostRecentPulse})]
modules = {}
conjunctions = set({})
for i, line in enumerate(stdin):
    name, destinations = line.rstrip().split("->")
    name = name.strip()
    destinations = destinations.strip().split(", ")
    if "%" in name:
        modules[name[1:]] = ["%", destinations, LOW]
    elif "&" in name:
        conjunctions.add(name[1:])
        modules[name[1:]] = ["&", destinations, {}]
    else:
        assert "broadcaster" in name, f"Found some weird module with name: {name}"
        modules["broadcaster"] = ["broadcaster", destinations]

# Initialize all conjunctions sources to low pulse
for name, values in modules.items():
    destinations = values[1]
    for dest in destinations:        
        if dest in conjunctions:
            modules[dest][-1][name] = LOW

pulseCount = [0,0]
for _ in range(1000):
    pulses = [("broadcaster", LOW, "button")] # (receiver, pulse, sender)
    while len(pulses):
        name, pulse, sender = pulses.pop(0)    
        pulseCount[pulse] += 1        
        if name not in modules:
            continue
        module = modules[name]
        mType, destinations = module[:2]
        if mType == "%":
            status = module[2]
            if pulse == LOW:
                newPulse = LOW if status == HIGH else HIGH
                for dest in destinations:
                    pulses.append((dest, newPulse, name))
                modules[name][-1] = newPulse
        elif mType == "&":
            recentPulses = module[2]
            recentPulses[sender] = pulse
            allHighPulses = all([p == HIGH for p in recentPulses.values()])
            newPulse = LOW if allHighPulses else HIGH
            for dest in destinations:
                pulses.append((dest, newPulse, name))
        elif mType == "broadcaster":
            for dest in destinations:
                pulses.append((dest, pulse, name))
        else:
            assert False, f"Weird module type: {mType}"

print(pulseCount, pulseCount[0] * pulseCount[1])