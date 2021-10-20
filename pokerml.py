# this file holds the machine learning aspect of the AIs
import sqlite3

# calculates user bet difference as a percent of the buy in
def calculateUserBetDifference(app):

    totalOpponentBet = 0
    count = 0
    userIndex = -1

    for i in range(len(app.pokerPlayers)):
        if app.pokerPlayers[i].playerNum != 0:
            totalOpponentBet += app.pokerPlayers[i].playerBet
            count += 1
        else:
            userIndex = i
    
    averageOpponentBet = totalOpponentBet / count
    userBet = app.pokerPlayers[userIndex].playerBet
    betVariation = (userBet - averageOpponentBet)/app.pokerBuyIn
    mlComponent = betVariation

    if betVariation > .1:
        mlComponent = .1

    app.pokerML += mlComponent
    app.pokerMLWeight += 1

    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET player_ml = (?) WHERE username = (?)", (app.pokerML, app.username))
    cursor.execute("UPDATE users SET ml_weight = (?) WHERE username = (?)", (app.pokerMLWeight, app.username))
    conn.commit()
    conn.close()

# calculates ML odd adjustments for AIs
def pokerMLOddsAdjustment(app):

    if app.myPokerPlayer.playerIn == False:
        return 0
    else:
        if app.pokerMLWeight >= 100:
            if app.pokerML >= 1:
                return .5
            elif app.pokerML <= -1:
                return -.5
            else:
                return app.pokerML/2
        else:
            if app.pokerML >= 0:
                oddsAdjustment = app.pokerML * (app.pokerMLWeight/100)
                if oddsAdjustment >= 1:
                    return .5
                else:
                    return oddsAdjustment/2
            else:
                oddsAdjustment = app.pokerML * (app.pokerMLWeight/100)
                if oddsAdjustment <= -1:
                    return -.5
                else:
                    return oddsAdjustment/2