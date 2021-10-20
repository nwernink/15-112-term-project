# this file holds the key pressed functions for the poker game
from pokerml import *
from montecarloodds import *
import sqlite3

# called when betting occurs
def betKeyPressed(app):

    if app.pokerBetAmount > app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney:
        app.pokerBetAmount = round(app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney, 2)
        
    app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney -= round(app.pokerBetAmount, 2)
    app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet += round(app.pokerBetAmount, 2)
    if app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum == 0:
        app.accountBalance -= round(app.pokerBetAmount, 2)
    
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (app.accountBalance, app.username))
    conn.commit()
    conn.close()

    app.pokerBetClicked = False
    app.pokerPotSize += round(app.pokerBetAmount, 2)
    previousBetAmount = round(app.pokerBetAmount, 2)
    app.pokerBetAmount = round(app.bigBlind + app.pokerCallAmount - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)
    
    # changes the biggest bet
    app.pokerHighestBet = round(app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)
    app.pokerNumOfChecks = 1

# called when a call/check occurs
def callKeyPressed(app):

    app.pokerCallClicked = False
    app.pokerCallAmount = round(app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)
    if app.pokerCallAmount > app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney:
        app.pokerCallAmount = round(app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney, 2)
    app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney -= round(app.pokerCallAmount, 2)
    app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet += round(app.pokerCallAmount, 2)

    if app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum == 0:
        app.accountBalance -= round(app.pokerCallAmount, 2)

    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (app.accountBalance, app.username))
    conn.commit()
    conn.close()

    app.pokerPotSize += round(app.pokerCallAmount, 2)
    app.pokerNumOfChecks += 1

# called when a fold occurs
def foldKeyPressed(app):

    app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerIn = False
    app.pokerFoldClicked = False
    app.pokerPlayersLeft -= 1

# changes action index to the next player in the hand
def changeActionIndex(app):
    
    # changes the action index until it reaches someone still in the hand
    if app.pokerActionIndex == len(app.pokerPlayers) - 1:
        app.pokerActionIndex = 0
    else:
        app.pokerActionIndex += 1
    while app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerIn == False:
        if app.pokerActionIndex == len(app.pokerPlayers) - 1:
            app.pokerActionIndex = 0
        else:
            app.pokerActionIndex += 1

# generates message when a bet occurs
def betMessage(app, previousActionIndex):
    if app.pokerPlayerImages[previousActionIndex][1] == 0:
        app.pokerCurrentMessage = f"{app.username} raises bet to ${round(app.pokerHighestBet, 2)}, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"
    elif app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
        app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} raises bet to ${round(app.pokerHighestBet, 2)}, {app.username}'s turn"
    else:
        app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} raises bet to ${round(app.pokerHighestBet, 2)}, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"

# generates message when a fold occurs
def foldMessage(app, previousActionIndex):

    if (app.pokerFlop) and (not app.donePreFlopBetting):
        app.pokerPlayerOdds = omniscientPlayerOddsPreFlop(app)
    elif (app.pokerTurn) and (not app.donePreTurnBetting):
        app.pokerPlayerOdds = omniscientPlayerOddsPreTurn(app)
    elif (app.pokerRiver) and (not app.donePreRiverBetting):
        app.pokerPlayerOdds = omniscientPlayerOddsPreRiver(app)
    elif app.endPokerBetting:
        app.pokerPlayerOdds = omniscientPlayerOddsPostRiver(app)

    if app.pokerPlayersLeft == 1:
        app.pokerActionIndex = app.smallBlindIndex

        # calculate ML
        calculateUserBetDifference(app)

        app.newPokerRound = True
        app.endOfHand = True
        app.endHandEarly = True

        winner = -1
        for i in range(len(app.pokerPlayers)):
            if app.pokerPlayers[app.pokerPlayerImages[i][1]].playerIn == True:
                winner = i
        
        app.pokerPlayers[app.pokerPlayerImages[winner][1]].playerMoney += app.pokerPotSize
        if app.pokerPlayers[app.pokerPlayerImages[winner][1]].playerNum == 0:
            app.accountBalance += app.pokerPotSize
            conn = sqlite3.connect("user.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (app.accountBalance, app.username))
            conn.commit()
            conn.close()

        if app.pokerPlayerImages[previousActionIndex][1] == 0:
            app.pokerCurrentMessage = f"{app.username} folds, CPU {app.pokerPlayerImages[winner][1]} wins the hand"
        elif app.pokerPlayerImages[winner][1] == 0:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} folds, {app.username} wins the hand"
        else:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} folds, CPU {app.pokerPlayerImages[winner][1]} wins the hand"

    else:
        if app.pokerPlayerImages[previousActionIndex][1] == 0:
            app.pokerCurrentMessage = f"{app.username} folds, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"
        elif app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} folds, {app.username}'s turn"
        else:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} folds, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"

# generates message when a call occurs
def callMessage(app, previousActionIndex):

    if app.pokerCallAmount > 0 and (app.pokerNumOfChecks != app.pokerPlayersLeft):
        if app.pokerPlayerImages[previousActionIndex][1] == 0:
            app.pokerCurrentMessage = f"{app.username} calls ${round(app.pokerCallAmount, 2)}, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"
        elif app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} calls ${round(app.pokerCallAmount, 2)}, {app.username}'s turn"
        else:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} calls ${round(app.pokerCallAmount, 2)}, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"
    
    elif app.pokerNumOfChecks != app.pokerPlayersLeft:
        if app.pokerPlayerImages[previousActionIndex][1] == 0:
            app.pokerCurrentMessage = f"{app.username} checks, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"
        elif app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} checks, {app.username}'s turn"
        else:
            app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} checks, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"

# called when betting occurs
def pokerBetKeyPressed(app):
    
    previousActionIndex = app.pokerActionIndex

    betKeyPressed(app)

    changeActionIndex(app)

    betMessage(app, previousActionIndex)

# called when a fold occurs
def pokerFoldKeyPressed(app):

    previousActionIndex = app.pokerActionIndex

    foldKeyPressed(app)

    changeActionIndex(app)

    foldMessage(app, previousActionIndex)

# called when a call/check occurs
def pokerCallKeyPressed(app):

    previousActionIndex = app.pokerActionIndex

    callKeyPressed(app)

    changeActionIndex(app)

    callMessage(app, previousActionIndex)