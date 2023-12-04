from sys import stdin

cards = []
for i, line in enumerate(stdin):
    cards.append([i+1,line.rstrip()])

originalCards = cards.copy()
total = 0    
cardCount = {cNumber: 1 for cNumber, _ in cards}
for newCard in cards:        
    cardNumber, card = newCard    
    toAdd = cardCount[cardNumber]
    total += toAdd
    winningNumbersStart = card.find(":")
    winningNumbersEnd = card.find("|")
    winningNumbers = set(map(int, card[winningNumbersStart+2:winningNumbersEnd-1].split()))
    ourNumbers = list(map(int, card[winningNumbersEnd+1::].split()))
        
    matches = 0
    for number in ourNumbers:
        if number in winningNumbers:
            matches += 1
    
    for i in range(matches):
        cardCount[cardNumber + 1 + i] += cardCount[cardNumber]
    
print(total)