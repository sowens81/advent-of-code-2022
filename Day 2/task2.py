handValues={
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "Y": "paper",
    "X": "rock",
    "Z": "scissors"
}

result={
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}


scoring={
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lose": 0,
    "draw": 3,
    "win": 6
}

playerAScore=0
playerBScore=0

def check_winner(playerAHand, playerBHand, index):
    global playerAScore
    global playerBScore
    
    playerALocalScore=0
    playerBLocalScore=0
    
    
    if playerAHand == "rock":
        if playerBHand == "lose":
           playerALocalScore += (scoring["rock"] + scoring["win"])
           playerBLocalScore += (scoring["scissors"] + scoring["lose"])
        if playerBHand == "draw":
           playerALocalScore += (scoring["rock"] + scoring["draw"])
           playerBLocalScore += (scoring["rock"] + scoring["draw"])
        if playerBHand == "win":
           playerALocalScore += (scoring["rock"] + scoring["lose"])
           playerBLocalScore += (scoring["paper"] + scoring["win"])
    if playerAHand == "paper":
        if playerBHand == "lose":
           playerALocalScore += (scoring["paper"] + scoring["win"])
           playerBLocalScore += (scoring["rock"] + scoring["lose"])
        if playerBHand == "draw":
           playerALocalScore += (scoring["paper"] + scoring["draw"])
           playerBLocalScore += (scoring["paper"] + scoring["draw"])
        if playerBHand == "win":
           playerALocalScore += (scoring["paper"] + scoring["lose"])
           playerBLocalScore += (scoring["scissors"] + scoring["win"])
    if playerAHand == "scissors":
        if playerBHand == "lose":
           playerALocalScore += (scoring["scissors"] + scoring["win"])
           playerBLocalScore += (scoring["paper"] + scoring["lose"])
        if playerBHand == "draw":
           playerALocalScore += (scoring["scissors"] + scoring["draw"])
           playerBLocalScore += (scoring["scissors"] + scoring["draw"])
        if playerBHand == "win":
           playerALocalScore += (scoring["scissors"] + scoring["lose"])
           playerBLocalScore += (scoring["rock"] + scoring["win"])
    
    print("Round " + str(index + 1) + ": Player 1 (" + playerAHand + " ) " + str(playerALocalScore) + " / Player 2 (" + playerBHand + " ) " + str(playerBLocalScore))
    
    playerAScore += playerALocalScore
    playerBScore += playerBLocalScore

file = open("data.txt")
lines = file.readlines()

for index, line in enumerate(lines):
    gameHands = line.replace("\n","").split(" ")
    check_winner(handValues[gameHands[0]], result[gameHands[1]], index)


print("Player One Score: " + str(playerAScore))
print("Player Two Score: " + str(playerBScore))