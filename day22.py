#DONE
f = open("day22.txt", "r")
currLine = f.readline().rstrip().strip()
currLine = f.readline().rstrip().strip()
i=2
player1Deck = []
while i < 27:
    player1Deck.append(int(currLine))
    currLine = f.readline().rstrip().strip()
    i+=1
currLine = f.readline().rstrip().strip()
currLine = f.readline().rstrip().strip()
i=29
player2Deck = []
while i < 54:
    player2Deck.append(int(currLine))
    currLine = f.readline().rstrip().strip()
    i+=1
while len(player1Deck) > 0 and len(player2Deck) > 0:
    player1Card = player1Deck.pop(0)
    player2Card = player2Deck.pop(0)
    if player1Card > player2Card:
        player1Deck.append(player1Card)
        player1Deck.append(player2Card)
    else:
        player2Deck.append(player2Card)
        player2Deck.append(player1Card)
#we know player1 won
i=1
winnerScore = 0
while len(player1Deck) > 0:
    cardVal = player1Deck.pop()
    cardVal = cardVal * i
    i+=1
    winnerScore+=cardVal
print(winnerScore)