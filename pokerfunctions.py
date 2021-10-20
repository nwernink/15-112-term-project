# this file holds the functionality of the poker game

import math, random, copy

# creates a deck of cards in a list
def cardDeck():

    ranks = "23456789TJQKA"
    suits = "CDHS"
    deck = []

    # loop through all of the ranks and suits and append them to the card list
    for i in range(len(ranks)):
        for j in range(len(suits)):
            deck.append(ranks[i] + suits[j])

    return deck

# draws card give a string of two characters and the center point
def drawCard(canvas, card, centerX, centerY):

    # gets the suit and the color for the card
    if card[1] == "C":
        suit, color = "\u2663", "black"
    elif card[1] == "D":
        suit, color = "\u2662", "red"
    elif card[1] == "H":
        suit, color = "\u2665", "red"
    elif card[1] == "S":
        suit, color = "\u2660", "black"

    # gets the fill color for the card
    if color == "black":
        fill = "black"
    else:
        fill = "red"

    # draws the card with the suit and rank
    canvas.create_rectangle(centerX - 12.5, centerY - 20, centerX + 12.5,
                centerY + 20, fill = fill)
    canvas.create_text(centerX - 6.5, centerY - 15, text = suit, fill = "white")

    if card[0] == "T":
        canvas.create_text(centerX, centerY, text = 10, fill = "white")
    else:
        canvas.create_text(centerX, centerY, text = card[0], fill = "white")

    canvas.create_text(centerX + 7.5, centerY + 15, text = suit, fill = "white")

# deals cards to all players
def dealCards(app, deck):

    playerHands = []
    cardDeck = deck

    # loops through the number of players and gives each two cards randomly
    for i in range(len(app.pokerPlayers)):
        
        cardOne = random.choice(cardDeck)
        cardDeck.remove(cardOne)
        cardTwo = random.choice(cardDeck)
        cardDeck.remove(cardTwo)

        app.pokerPlayers[i].playerHand.append(cardOne)
        app.pokerPlayers[i].playerHand.append(cardTwo)

    # sets the remaining cards to the card deck
    app.remainingDeck = cardDeck

# deals the flop
def dealFlop(app, deck):

    cardDeck = deck

    # burn one card
    burnCard = random.choice(cardDeck)
    cardDeck.remove(burnCard)

    # deal the first card
    cardOne = random.choice(cardDeck)
    cardDeck.remove(cardOne)

    # deal the second card
    cardTwo = random.choice(cardDeck)
    cardDeck.remove(cardTwo)

    # deal the third card
    cardThree = random.choice(cardDeck)
    cardDeck.remove(cardThree)

    # set the three cards to the board and the remaining deck to the poker deck
    app.pokerBoard = [cardOne, cardTwo, cardThree]
    app.remainingDeck = cardDeck

# deals the turn
def dealTurn(app, deck):

    cardDeck = deck

    # burn one card
    burnCard = random.choice(cardDeck)
    cardDeck.remove(burnCard)

    # deal the turn card
    turnCard = random.choice(cardDeck)
    cardDeck.remove(turnCard)

    # set the turn card to the board and the remaining deck to the poker deck
    app.pokerBoard.append(turnCard)
    app.remainingDeck = cardDeck

# deals the river
def dealRiver(app, deck):

    cardDeck = deck

    # burn one card
    burnCard = random.choice(cardDeck)
    cardDeck.remove(burnCard)

    # deal the turn card
    riverCard = random.choice(cardDeck)
    cardDeck.remove(riverCard)

    # set the turn card to the board and the remaining deck to the poker deck
    app.pokerBoard.append(riverCard)
    app.remainingDeck = cardDeck

# calculates the score of a five card hand
def calculateHandScore(fiveCardHand):
    
    score = 0
    ranks = []
    suits = []
    for card in fiveCardHand:
        ranks.append(card[0])
        suits.append(card[1])

    cardScores = {"2" : 2, "3" : 3, "4": 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
                    "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}

    sortedRanks = []
    for rank in ranks:
        sortedRanks.append(cardScores[rank])
    sortedRanks.sort()

    # checks to see if the hand has a straight
    isStraight = True
    if (sortedRanks[4] == 14) and (sortedRanks[0] == 2) and (sortedRanks[1] == 3) and (sortedRanks[2] == 4) and (sortedRanks[3] == 5):
        isStraight = True
    else:
        prevRank = 0
        for rank in sortedRanks:
            if prevRank == 0:
                prevRank = rank  
            elif rank - 1 != prevRank:
                isStraight = False
                break
            prevRank = rank

    # checks to see if the hand has a four of a kind
    isFourOfKind = True
    fourOfKindCard = 0
    for rank in sortedRanks:
        if sortedRanks.count(rank) != 4:
            isFourOfKind = False
        else:
            isFourOfKind = True
            fourOfKindCard = rank
            break

    # checks to see if the hand has a full house
    isFullHouse = False
    fullHouseCard = 0
    secondFullHouse = 0
    if (sortedRanks[0] == sortedRanks[1]) and (sortedRanks[2] == sortedRanks[3] == sortedRanks[4]):
        isFullHouse = True
        fullHouseCard = sortedRanks[2]
        secondFullHouse = sortedRanks[0]
    elif (sortedRanks[0] == sortedRanks[1] == sortedRanks[2]) and (sortedRanks[3] == sortedRanks[4]):
        isFullHouse = True
        fullHouseCard = sortedRanks[0]
        secondFullHouse = sortedRanks[3]

    # checks to see if the hand has a flush
    isFlush = True
    prevCardSuit = suits[0]
    for suit in suits:
        if suit != prevCardSuit:
            isFlush = False
            break
        else:
            prevCardSuit = suit

    backToString = []
    for rank in sortedRanks:
        for string in cardScores:
            if cardScores[string] == rank:
                backToString.append(string)


    if isStraight and isFlush:
        score = 80000000000 + sortedRanks[4]
        return score, f"Straight Flush with {backToString[4]} high card"

    elif isFourOfKind:
        if sortedRanks[4] == fourOfKindCard:
            score = 70000000000 + fourOfKindCard*100 + sortedRanks[0] 
            return score, f"Four of a Kind with {backToString[sortedRanks.index(fourOfKindCard)]}s and a {backToString[0]}"
        else:
            score = 70000000000 + fourOfKindCard*100 + sortedRanks[4] 
            return score, f"Four of a Kind with {backToString[sortedRanks.index(fourOfKindCard)]}s and a {backToString[4]}"
    
    elif isFullHouse:
        score = 60000000000 + fullHouseCard*100 + secondFullHouse
        return score, f"Full House with {backToString[sortedRanks.index(fullHouseCard)]}s and {backToString[sortedRanks.index(secondFullHouse)]}s"

    elif isFlush:
        score = 50000000000 + sortedRanks[4]*100000000 + sortedRanks[3]*1000000 + sortedRanks[2]*10000 + sortedRanks[1]*100 + sortedRanks[0]
        return score, f"Flush with a {backToString[4]}, {backToString[3]}, {backToString[2]}, {backToString[1]}, and a {backToString[0]}"

    elif isStraight:
        score = 40000000000 + sortedRanks[4]
        return score, f"Straight with a {backToString[4]} as the high card"




    # checks to see if the hand has a three of a kind
    isThreeOfKind = True
    threeOfKindCard = 0
    threeSortedRanksCopy = copy.copy(sortedRanks)
    for rank in sortedRanks:
        if sortedRanks.count(rank) != 3:
            isThreeOfKind = False
        else:
            isThreeOfKind = True
            threeOfKindCard = rank
            break
    if isThreeOfKind:
        threeKindIndex = sortedRanks.index(threeOfKindCard)
        sortedRanks.remove(threeOfKindCard)
        sortedRanks.remove(threeOfKindCard)
        sortedRanks.remove(threeOfKindCard)
        threeOfKindHigh = sortedRanks[1]
        threeKindHighIndex = threeSortedRanksCopy.index(threeOfKindHigh)
        threeOfKindLow = sortedRanks[0]
        threeKindLowIndex = threeSortedRanksCopy.index(threeOfKindLow)

    if isThreeOfKind:
        score = 30000000000 + threeOfKindCard*10000 + threeOfKindHigh*100 + threeOfKindLow
        return score, f"Three of Kind with {backToString[threeKindIndex]}s, a {backToString[threeKindHighIndex]} and a {backToString[threeKindLowIndex]}"


    # checks to see if the hand has a two pair
    isTwoPair = True
    copiedRanks = copy.copy(sortedRanks)
    twoPairFirstCard = 0
    twoPairSecondCard = 0
    for rank in copiedRanks:
        if copiedRanks.count(rank) == 2:
            twoPairFirstIndex = sortedRanks.index(rank)
            copiedRanks.remove(rank)
            copiedRanks.remove(rank)
            twoPairFirstCard = rank
            break
    if len(copiedRanks) == 3:
        for rank in copiedRanks:
            if copiedRanks.count(rank) == 2:
                twoPairSecondIndex = sortedRanks.index(rank)
                isTwoPair = True
                twoPairSecondCard = rank
                copiedRanks.remove(rank)
                copiedRanks.remove(rank)
                twoPairHighCard = copiedRanks[0]
                twoPairHighIndex = sortedRanks.index(twoPairHighCard)
                break
            else:
                isTwoPair = False
    else:
        isTwoPair = False

    if isTwoPair:
        if twoPairFirstCard > twoPairSecondCard:
            score = 20000000000 + twoPairFirstCard*10000 + twoPairSecondCard*100 + twoPairHighCard
            return score, f"Two Pair with {backToString[twoPairFirstIndex]}s, {backToString[twoPairSecondIndex]}s, and a {backToString[twoPairHighIndex]}"
        else:
            score = 20000000000 + twoPairSecondCard*10000 + twoPairFirstCard*100 + twoPairHighCard
            return score, f"Two Pair with {backToString[twoPairSecondIndex]}s, {backToString[twoPairFirstIndex]}s, and a {backToString[twoPairHighIndex]}"


    # checks to see if the hand has a pair
    pairCopiedRanks = copy.copy(sortedRanks)
    isPair = False
    pairCard = 0
    for rank in sortedRanks:
        if sortedRanks.count(rank) == 2:
            isPair = True
            pairCard = rank
            pairCardIndex = sortedRanks.index(pairCard)

            sortedRanks.remove(rank)
            sortedRanks.remove(rank)

            pairHighCard = sortedRanks[2]
            pairHighIndex = pairCopiedRanks.index(pairHighCard)
            pairMiddleCard = sortedRanks[1]
            pairMiddleIndex = pairCopiedRanks.index(pairMiddleCard)
            pairLowCard = sortedRanks[0]
            pairLowIndex = pairCopiedRanks.index(pairLowCard)
            break 
     
    if isPair:
        score = 10000000000 + pairCard*1000000 + pairHighCard*10000 + pairMiddleCard*100 + pairLowCard
        return score, f"One Pair with {backToString[pairCardIndex]}s, a {backToString[pairHighIndex]}, {backToString[pairMiddleIndex]}, and a {backToString[pairLowIndex]}"
    else:
        score = sortedRanks[4]*100000000 + sortedRanks[3]*1000000 + sortedRanks[2]*10000 + sortedRanks[1]*100 + sortedRanks[0]
        return score, f"High Card of {backToString[4]} with a {backToString[3]}, {backToString[2]}, {backToString[1]}, and a {backToString[0]}"

# chooses the best five card hand give a hand and the board
def chooseBestHand(hand, board):
    cards = hand + board
    bestHandDict = {}
    

    handsList = [ [0,1,2,3,4], [0,1,2,3,5], [0,1,2,3,6], [0,1,2,4,5], [0,1,2,4,6],
    [0,1,2,5,6], [0,1,3,4,5], [0,1,3,4,6], [0,1,3,5,6], [0,1,4,5,6], [0,2,3,4,5],
    [0,2,3,4,6], [0,2,3,5,6], [0,2,4,5,6], [0,3,4,5,6], [1,2,3,4,5], [1,2,3,4,6],
    [1,2,3,5,6], [1,2,4,5,6], [1,3,4,5,6], [2,3,4,5,6] ]

    bestHandList = []
    for hand in handsList:
        cardsInHand = []
        for card in hand:
            cardsInHand.append(cards[card])
        bestHandList.append((calculateHandScore(cardsInHand)[0], cardsInHand))

    bestHand = []
    bestHandScore = 0
    for hand in bestHandList:
        if hand[0] > bestHandScore:
            bestHandScore = hand[0]
            bestHand = hand[1]


    return bestHand, bestHandScore

# changes the small and big blinds
def changeBlinds(app):

    # check and change small blind index
    if app.smallBlindIndex == len(app.pokerPlayers) - 1:
        app.smallBlindIndex = 0
    else:
        app.smallBlindIndex += 1

    # check and change big blind index
    if app.bigBlindIndex == len(app.pokerPlayers) - 1:
        app.bigBlindIndex = 0
    else:
        app.bigBlindIndex += 1

# draw the poker cheat section below the table 
def drawPokerCheatSection(app, canvas):

    # divide the page into two sections: the table and the user interface
    canvas.create_line(0, 580, app.width, 580)

    # loops through all the players displays each person's hand
    for i in range(len(app.pokerPlayers)):
        # lists out each player
        if i == 0:
            canvas.create_text(100 + i*(app.width - 200)/7, 600,
                text = f'{app.username}')
        else:
            canvas.create_text(100 + i*(app.width - 200)/7, 600,
                text = f'CPU {i}')

        # draws each player hand ounce the cards have been dealt
        if app.pokerDeal == False:
            drawCard(canvas, app.pokerPlayers[i].playerHand[0],
                90 + i*(app.width - 200)/7, 650)
            drawCard(canvas, app.pokerPlayers[i].playerHand[1],
                90 + i*(app.width - 200)/7 + 20, 665)

            odds = app.pokerPlayerOdds[i]
            canvas.create_text(100 + i*(app.width - 200)/7, 725,
                text = f'{odds}%')

# draws the cards on the poker table
def drawPokerTableCards(app, canvas):

    # draw the flop if it has been dealt
    if app.dealtFlop:
        drawCard(canvas, app.pokerBoard[0], app.width/2 - 90,
                app.height/2 - 90)
        drawCard(canvas, app.pokerBoard[1], app.width/2 - 50,
                app.height/2 - 90)
        drawCard(canvas, app.pokerBoard[2], app.width/2 - 10,
                app.height/2 - 90)
    # draw the turn if it has been dealt
    if app.dealtTurn:
        drawCard(canvas, app.pokerBoard[3], app.width/2 + 40,
                app.height/2 - 90)
    
    # draw the river if it has been dealt
    if app.dealtRiver:
        drawCard(canvas, app.pokerBoard[4], app.width/2 + 90,
                app.height/2 - 90)

# draws small blind icon 
def drawSmallBlind(app, canvas):

    if app.smallBlindIndex == 0:
        canvas.create_oval(app.width/2 + 185, 260, app.width/2 + 215, 290,
                fill = "blue")
        canvas.create_text(app.width/2 + 200, 275, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 1:
        canvas.create_oval(app.width/2 + 310, app.height/2 - 90,
                app.width/2 + 340, app.height/2 - 60, fill = "blue")
        canvas.create_text(app.width/2 + 325, app.height/2 - 75, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 2:
        canvas.create_oval(app.width/2 + 310, app.height/2,
                app.width/2 + 340, app.height/2 + 30, fill = "blue")
        canvas.create_text(app.width/2 + 325, app.height/2 + 15, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 3:
        canvas.create_oval(app.width/2 + 185, 445, app.width/2 + 215, 475,
                fill = "blue")
        canvas.create_text(app.width/2 + 200, 460, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 4:
        canvas.create_oval(app.width/2 - 185, 445, app.width/2 - 215, 475,
                fill = "blue")
        canvas.create_text(app.width/2 - 200, 460, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 5:
        canvas.create_oval(app.width/2 - 310, app.height/2,
                app.width/2 - 340, app.height/2 + 30, fill = "blue")
        canvas.create_text(app.width/2 - 325, app.height/2 + 15, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 6:
        canvas.create_oval(app.width/2 - 310, app.height/2 - 90,
                app.width/2 - 340, app.height/2 - 60, fill = "blue")
        canvas.create_text(app.width/2 - 325, app.height/2 - 75, text = "SB",
                font = "Times 15 bold", fill = "white")

    elif app.smallBlindIndex == 7:
        canvas.create_oval(app.width/2 - 185, 260, app.width/2 - 215, 290,
                fill = "blue")
        canvas.create_text(app.width/2 - 200, 275, text = "SB",
                font = "Times 15 bold", fill = "white")

# draws big blind icon
def drawBigBlind(app, canvas):

    if app.bigBlindIndex == 0:
        canvas.create_oval(app.width/2 + 185, 260, app.width/2 + 215, 290,
                fill = "yellow")
        canvas.create_text(app.width/2 + 200, 275, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 1:
        canvas.create_oval(app.width/2 + 310, app.height/2 - 90,
                app.width/2 + 340, app.height/2 - 60, fill = "yellow")
        canvas.create_text(app.width/2 + 325, app.height/2 - 75, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 2:
        canvas.create_oval(app.width/2 + 310, app.height/2,
                app.width/2 + 340, app.height/2 + 30, fill = "yellow")
        canvas.create_text(app.width/2 + 325, app.height/2 + 15, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 3:
        canvas.create_oval(app.width/2 + 185, 445, app.width/2 + 215, 475,
                fill = "yellow")
        canvas.create_text(app.width/2 + 200, 460, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 4:
        canvas.create_oval(app.width/2 - 185, 445, app.width/2 - 215, 475,
                fill = "yellow")
        canvas.create_text(app.width/2 - 200, 460, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 5:
        canvas.create_oval(app.width/2 - 310, app.height/2,
                app.width/2 - 340, app.height/2 + 30, fill = "yellow")
        canvas.create_text(app.width/2 - 325, app.height/2 + 15, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 6:
        canvas.create_oval(app.width/2 - 310, app.height/2 - 90,
                app.width/2 - 340, app.height/2 - 60, fill = "yellow")
        canvas.create_text(app.width/2 - 325, app.height/2 - 75, text = "BB",
                font = "Times 15 bold", fill = "black")

    elif app.bigBlindIndex == 7:
        canvas.create_oval(app.width/2 - 185, 260, app.width/2 - 215, 290,
                fill = "yellow")
        canvas.create_text(app.width/2 - 200, 275, text = "BB",
                font = "Times 15 bold", fill = "black")

# draws player bets
def drawPlayerBets(app, canvas):

    if app.pokerDeal == False:
        # player in spot 0
        canvas.create_text(app.width/2 + 200, 240, fill = "black", font = "Times 15 bold",
                text = f"${round(app.pokerPlayers[app.pokerPlayerImages[0][1]].playerBet, 2)}")
        
        # player in spot 1
        canvas.create_text(app.width/2 + 380, app.height/2 - 75, fill = "black", font = "Times 15 bold",
                text = f"${round(app.pokerPlayers[app.pokerPlayerImages[1][1]].playerBet, 2)}")
        
        if len(app.pokerPlayers) > 2:
            # player in spot 2
            canvas.create_text(app.width/2 + 380, app.height/2 + 15, fill = "black", font = "Times 15 bold",
                    text = f"${round(app.pokerPlayers[app.pokerPlayerImages[2][1]].playerBet, 2)}")

        if len(app.pokerPlayers) > 3:
            # player in spot 3
            canvas.create_text(app.width/2 + 200, 500, fill = "black", font = "Times 15 bold",
                    text = f"${round(app.pokerPlayers[app.pokerPlayerImages[3][1]].playerBet, 2)}")

        if len(app.pokerPlayers) > 4:
            # player in spot 4
            canvas.create_text(app.width/2 - 200, 500, fill = "black", font = "Times 15 bold",
                    text = f"${round(app.pokerPlayers[app.pokerPlayerImages[4][1]].playerBet, 2)}")
        
        if len(app.pokerPlayers) > 5:
            # player in spot 5
            canvas.create_text(app.width/2 - 380, app.height/2 + 15, fill = "black", font = "Times 15 bold",
                    text = f"${round(app.pokerPlayers[app.pokerPlayerImages[5][1]].playerBet, 2)}")
        
        if len(app.pokerPlayers) > 6:
            # player in spot 6
            canvas.create_text(app.width/2 - 380, app.height/2 - 75, fill = "black", font = "Times 15 bold",
                    text = f"${round(app.pokerPlayers[app.pokerPlayerImages[6][1]].playerBet, 2)}")

        if len(app.pokerPlayers) > 7:
            # player in spot 7
            canvas.create_text(app.width/2 - 200, 240, fill = "black", font = "Times 15 bold",
                    text = f"${round(app.pokerPlayers[app.pokerPlayerImages[7][1]].playerBet, 2)}")

# draws poker betting option buttons
def drawPokerButtons(app, canvas):

    if app.pokerCallClicked:
        call = "Times 27 bold"
    else:
        call = "Times 25"

    if app.pokerBetClicked:
        bet = "Times 27 bold"
    else:
        bet = "Times 25"

    if app.pokerFoldClicked:
        fold = "Times 30 bold"
    else:
        fold = "Times 25"

    if (app.mode == "pokerMode") and (app.pokerDeal == False) and (app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum == 0) and (not app.endOfHand):
        # draw check/call button
        canvas.create_rectangle(app.width/2 - 70, app.height/2 - 50,
                app.width/2 + 70, app.height/2, fill = "white",
                outline = "darkgreen", width = 5)
        canvas.create_text(app.width/2, app.height/2 - 25, text = "Check/Call",
                font = call, fill = "darkgreen")

        # draw bet button
        canvas.create_rectangle(app.width/2 - 160, app.height/2 - 50,
                app.width/2 - 80, app.height/2, fill = "white",
                outline = "darkgreen", width = 5)
        canvas.create_text(app.width/2 - 120, app.height/2 - 25, text = "Bet",
                font = bet, fill = "darkgreen")

        # draw fold button
        canvas.create_rectangle(app.width/2 + 80, app.height/2 - 50,
                app.width/2 + 160, app.height/2, fill = "white",
                outline = "red", width = 5)
        canvas.create_text(app.width/2 + 120, app.height/2 - 25, text = "Fold",
                font = fold, fill = "red")
        
        # draw betting interface
        if app.pokerBetClicked:
            canvas.create_rectangle(app.width/2 - 80, app.height/2 + 20,
                app.width/2 + 80, app.height/2 + 60, fill = "white", 
                outline = "darkgreen", width = 5)
            canvas.create_text(app.width/2, app.height/2 + 40,
                text = f'Bet amount: ${app.pokerBetAmount}', fill = "black")

        elif app.pokerCallClicked:
            canvas.create_rectangle(app.width/2 - 80, app.height/2 + 20,
                app.width/2 + 80, app.height/2 + 60, fill = "white", 
                outline = "darkgreen", width = 5)
            canvas.create_text(app.width/2, app.height/2 + 40,
                text = f'Call amount: ${app.pokerCallAmount}', fill = "black")

# draws the buy in, blinds, and pot size
def drawPokerBuyInBlinds(app, canvas):

    # displays the buy in amount and blinds
    canvas.create_text(app.width/2, app.height/2 + 155,
            text = f'Buy In: ${app.pokerBuyIn}   Blinds {round(app.smallBlind,2)}/{round(app.bigBlind,2)}')
    
    # displays the pot size
    if app.pokerDeal == False:
        canvas.create_text(app.width/2, app.height/2 + 85,
                text = f'Pot: ${round(app.pokerPotSize, 2)}')

# draws the poker information section below the table
def drawPokerInformationSection(app, canvas):
    
    # divide the page into two sections: the table and the user interface
    canvas.create_line(0, 580, app.width, 580)

    # draw your hand
    canvas.create_text(100, 600, text = f'{app.username}')

    # draws each player hand ounce the cards have been dealt
    if app.pokerDeal == False:
        drawCard(canvas, app.pokerPlayers[0].playerHand[0], 90, 650)
        drawCard(canvas, app.pokerPlayers[0].playerHand[1], 110, 665)

    canvas.create_text(app.width/2, 650, text = f"{app.pokerCurrentMessage}",
            font = "Times 30")
    canvas.create_text(app.width/2, 725, text = "Press the space bar to see your opponent's hands and everyone's odds")