from sys import stdin
from typing import *
import re

handRanks = {
    "highCard": 1,
    "pair": 2,
    "twoPair": 3,
    "threeOfAKind": 4,
    "fullHouse": 5,
    "fourOfAKind": 6,
    "fiveOfAKind": 7,
}

strengthOrder = "AKQT98765432J"

def getHandRank(hand: str) -> int:    
    isFiveOfAKind = hand.count(hand[0]) == 5 
    if (isFiveOfAKind): return handRanks["fiveOfAKind"]
    isFourOfAKind = hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4
    if (isFourOfAKind): 
        if (hand.count("J") == 1 or hand.count("J") == 4): return handRanks["fiveOfAKind"]
        return handRanks["fourOfAKind"]
    differentCards = set(hand)
    if (len(differentCards) == 2):
        if (hand.count("J") == 2 or hand.count("J") == 3):
            return handRanks["fiveOfAKind"]
        return handRanks["fullHouse"]
    if (len(differentCards) == 3):
        if (hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3):
            if (hand.count("J") == 1): return handRanks["fourOfAKind"]            
            if (hand.count("J") == 3): return handRanks["fourOfAKind"]
            return handRanks["threeOfAKind"]
        
        if (hand.count("J") == 1): return handRanks["fullHouse"]
        if (hand.count("J") == 2): return handRanks["fourOfAKind"]
        return handRanks["twoPair"]
    if (len(differentCards) == 4):
        if (hand.count("J") == 1 or hand.count("J") == 2): return handRanks["threeOfAKind"]        
        return handRanks["pair"]
    if (hand.count("J") == 1): return handRanks["pair"]
    return handRanks["highCard"]

def getStrongerHand(hand1: str, hand2: str) -> str:
    for i in range(len(hand1)):
        if (strengthOrder.index(hand1[i]) < strengthOrder.index(hand2[i])):
            return hand1
        elif (strengthOrder.index(hand1[i]) > strengthOrder.index(hand2[i])):
            return hand2
    return hand1

bids = {}
handsByRank = {}
for i, line in enumerate(stdin):
    hand, bid = line.rstrip().split()
    bids[hand] = int(bid)    
    if (getHandRank(hand) not in handsByRank):
        handsByRank[getHandRank(hand)] = [hand]
    else:
        handsByRank[getHandRank(hand)].append(hand)



finalRanks = []
for rank in sorted(handsByRank.keys()):    
    sortedHands = []
    for i in range(len(handsByRank[rank])):
        weakestHand = None
        for j in range(len(handsByRank[rank])):            
            if (handsByRank[rank][j] in sortedHands):
                continue
            if (weakestHand == None):
                weakestHand = handsByRank[rank][j]
            weakestHand = weakestHand if getStrongerHand(weakestHand, handsByRank[rank][j]) == handsByRank[rank][j] else handsByRank[rank][j]
        sortedHands.append(weakestHand)
    finalRanks.extend(sortedHands)
    
print(finalRanks)
total = 0
for i, hand in enumerate(finalRanks):
    total += bids[hand] * (i + 1)
print(total)