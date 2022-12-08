handValues={
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "Y": "paper",
    "X": "rock",
    "Z": "scissors"
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
        if playerBHand == "rock":
           playerALocalScore += (scoring["rock"] + scoring["draw"])
           playerBLocalScore += (scoring["rock"] + scoring["draw"])
        if playerBHand == "paper":
           playerALocalScore += (scoring["rock"] + scoring["lose"])
           playerBLocalScore += (scoring["paper"] + scoring["win"])
        if playerBHand == "scissors":
           playerALocalScore += (scoring["rock"] + scoring["win"])
           playerBLocalScore += (scoring["scissors"] + scoring["lose"])
    if playerAHand == "paper":
        if playerBHand == "rock":
           playerALocalScore += (scoring["paper"] + scoring["win"])
           playerBLocalScore += (scoring["rock"] + scoring["lose"])
        if playerBHand == "paper":
           playerALocalScore += (scoring["paper"] + scoring["draw"])
           playerBLocalScore += (scoring["paper"] + scoring["draw"])
        if playerBHand == "scissors":
           playerALocalScore += (scoring["paper"] + scoring["lose"])
           playerBLocalScore += (scoring["scissors"] + scoring["win"])
    if playerAHand == "scissors":
        if playerBHand == "rock":
           playerALocalScore += (scoring["scissors"] + scoring["lose"])
           playerBLocalScore += (scoring["rock"] + scoring["win"])
        if playerBHand == "paper":
           playerALocalScore += (scoring["scissors"] + scoring["win"])
           playerBLocalScore += (scoring["paper"] + scoring["lose"])
        if playerBHand == "scissors":
           playerALocalScore += (scoring["scissors"] + scoring["draw"])
           playerBLocalScore += (scoring["scissors"] + scoring["draw"])
    
    print("Round " + str(index + 1) + ": Player 1 - " + str(playerALocalScore) + " / Player 2 - " + str(playerBLocalScore))
    
    playerAScore += playerALocalScore
    playerBScore += playerBLocalScore

file = open("data.txt")
lines = file.readlines()

for index, line in enumerate(lines):
    gameHands = line.replace("\n","").split(" ")    
    check_winner(handValues[gameHands[0]], handValues[gameHands[1]], index)


print("Player One Score: " + str(playerAScore))
print("Player Two Score: " + str(playerBScore))