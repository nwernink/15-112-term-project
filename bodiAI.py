# Agressive/Bodi poker AI
from montecarloodds import *
from pokerml import *

# runs pre flop agressive AI
def preFlopBodiAI(app, hand, numPlayersLeft, betSize = 1/100):

    handString = ""
    for card in hand:
        handString += card

    if numPlayersLeft == 7:
        try:
            handOdds = call8PlayerDict1326()[handString]
        except:
            handOdds = call8PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app)

        return preFlop7OthersBodiAIAction(handOdds, betSize), handOdds

    elif numPlayersLeft == 6:
        try:
            handOdds = call7PlayerDict1326()[handString]
        except:
            handOdds = call7PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 1.25

        return preFlop6OthersBodiAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 5:
        try:
            handOdds = call6PlayerDict1326()[handString]
        except:
            handOdds = call6PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 1.5

        return preFlop5OthersBodiAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 4:
        try:
            handOdds = call5PlayerDict1326()[handString]
        except:
            handOdds = call5PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 1.75
        
        return preFlop4OthersBodiAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 3:
        try:
            handOdds = call4PlayerDict1326()[handString]
        except:
            handOdds = call4PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 2
        
        return preFlop3OthersBodiAIAction(handOdds, betSize), handOdds
        
    elif numPlayersLeft == 2:
        try:
            handOdds = call3PlayerDict1326()[handString]
        except:
            handOdds = call3PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 2.25
        
        return preFlop2OthersBodiAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 1:
        try:
            handOdds = call2PlayerDict1326()[handString]
        except:
            handOdds = call2PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 2.5
        
        return preFlop1OtherBodiAIAction(handOdds, betSize), handOdds

# pre flop with 7 others
def preFlop7OthersBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds < .09:
            action = ("Fold")
        elif .09 <= odds < .1:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif .1 <= odds <= .15:
            action = ("Call")
        elif .15 < odds <= .175:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        elif .175 < odds <= .25:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        elif odds > .25:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(4, 5)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .13:
            action = ("Fold")
        elif .13 < odds <= .15:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds > .15:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .15:
            action = ("Fold")
        elif .15 < odds <= .2:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds > .2:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds < .2:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds < .2:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 6 others
def preFlop6OthersBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .1:
            action = ("Fold")
        elif .1 < odds <= .2:
            action = ("Call")
        elif .2 < odds <= .25:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .12:
            action = ("Fold")
        elif .12 < odds <= .15:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .175:
            action = ("Fold")
        elif .175 < odds <= .225:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .2:
            action = ("Fold")
        elif .2 < odds <= .25:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds <= .225:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 5 others
def preFlop5OthersBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .17:
            action = ("Fold")
        elif .17 < odds <= .225:
            action = ("Call")
        elif .225 < odds <= .275:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .2:
            action = ("Fold")
        elif .2 < odds <= .25:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .225:
            action = ("Fold")
        elif .225 < odds <= .275:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .25:
            action = ("Fold")
        elif .25 < odds <= .333:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds <= .35:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 4 others
def preFlop4OthersBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .19:
            action = ("Fold")
        elif .19 < odds <= .275:
            action = ("Call")
        elif .275 < odds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                randBet = random.randint(2, 3)
            else:
                action = ("Call")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .225:
            action = ("Fold")
        elif .225 < odds <= .275:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .275:
            action = ("Fold")
        elif .275 < odds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .3:
            action = ("Fold")
        elif .3 < odds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds <= .425:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 3 others
def preFlop3OthersBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .225:
            action = ("Fold")
        elif .225 < odds <= .325:
            action = ("Call")
        elif .325 < odds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .3:
            action = ("Fold")
        elif .3 < odds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .35:
            action = ("Fold")
        elif .35 < odds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .375:
            action = ("Fold")
        elif .375 < odds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds <= .5:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 2 others
def preFlop2OthersBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .3:
            action = ("Fold")
        elif .3 < odds <= .4:
            action = ("Call")
        elif .4 < odds <= .475:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call") 
    
    elif .01 < betSize <= .04:
        if odds <= .35:
            action = ("Fold")
        elif .35 < odds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds >= .65:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                randBet = random.randint(3, 5)
                action = ("Bet", randBet/100)
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .4:
            action = ("Fold")
        elif .4 < odds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .45:
            action = ("Fold")
        elif .45 < odds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds <= .55:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 1 other
def preFlop1OtherBodiAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .5:
            action = ("Fold")
        elif .5 < odds <= .6:
            action = ("Call")
        elif .6 < odds <= .7:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .55:
            action = ("Fold")
        elif .55 < odds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds >= .75:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                randBet = random.randint(3, 5)
                action = ("Bet", randBet/100)
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .6:
            action = ("Fold")
        elif .6 < odds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .65:
            action = ("Fold")
        elif .65 < odds <= .75:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds <= .75:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")


    return action

# print(preFlopBodiAI(["AC","TH"], 5, .35))

# runs pre turn agressive AI
def preTurnBodiAI(app, hand, board, numPlayersLeft, callSize = 0):

    if numPlayersLeft == 7:
        handOdds = postFlopOdds(hand, board, 7, 1000)
        handOdds += pokerMLOddsAdjustment(app)
        return preTurn7OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 6:
        handOdds = postFlopOdds(hand, board, 6, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.4
        return preTurn6OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 5:
        handOdds = postFlopOdds(hand, board, 5, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.8
        return preTurn5OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 4:
        handOdds = postFlopOdds(hand, board, 4, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.2
        return preTurn4OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 3:
        handOdds = postFlopOdds(hand, board, 3, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.6
        return preTurn3OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 2:
        handOdds = postFlopOdds(hand, board, 2, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3
        return preTurn2OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 1:
        handOdds = postFlopOdds(hand, board, 1, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3.5
        return preTurn1OtherBodiAIAction(handOdds, callSize)
    
# pre turn with 7 others
def preTurn7OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .225:
            action = ("Call")
        elif .225 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .35 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        elif handOdds > .5:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .175:
            action = ("Fold")
        elif .175 < handOdds <= .25:
            randNum = random.randint(1, 100)
            if randNum <= 85:
                action = ("Call")
            else:
                action = ("Fold")
        elif .25 < handOdds <= .35:
            action = ("Call")
        elif .35 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum >= 50:
                action = ("Call")
            else:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum >= 25:
                action = ("Call")
            elif 25 < randNum <= 50:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)

    elif .04 < callSize <= .075:
        if handOdds <= .225:
            action = ("Fold")
        elif .225 < handOdds <= .3:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .3 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .5:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .33:
            action = ("Fold")
        elif .33 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .65:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 6 others
def preTurn6OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .25:
            action = ("Call")
        elif .25 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .35 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        elif handOdds > .5:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .25:
            action = ("Fold")
        elif .25 < handOdds <= .3:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .3 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .5:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .275:
            action = ("Fold")
        elif .275 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .35 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .5:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .7:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 5 others
def preTurn5OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .275:
            action = ("Call")
        elif .275 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .35 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .25:
            action = ("Fold")
        elif .25 < handOdds <= .3:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .3 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .275:
            action = ("Fold")
        elif .275 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .35 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .7:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 4 others
def preTurn4OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .3:
            action = ("Call")
        elif .3 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .375 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .275:
            action = ("Fold")
        elif .275 < handOdds <= .325:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .325 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .3:
            action = ("Fold")
        elif .3 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .4:
            action = ("Fold")
        elif .4 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .7:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 3 others
def preTurn3OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .325:
            action = ("Call")
        elif .325 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .4 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .325:
            action = ("Fold")
        elif .325 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .4 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .45 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .425:
            action = ("Fold")
        elif .425 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .7:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 2 others
def preTurn2OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .35:
            action = ("Call")
        elif .35 < handOdds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .425 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .425 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .425:
            action = ("Fold")
        elif .425 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .5 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .475:
            action = ("Fold")
        elif .475 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .75:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 1 other
def preTurn1OtherBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .5:
            action = ("Call")
        elif .5 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .6 < handOdds <= .75:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .55 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .5:
            action = ("Fold")
        elif .5 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .65 < handOdds <= .85:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .575:
            action = ("Fold")
        elif .575 < handOdds <= .75:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .85:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# print(preTurnBodiAI(["AD","AS"], ["7H","3D","7D"], 4, 0.1))

# runs pre river agressive AI
def preRiverBodiAI(app, hand, board, numPlayersLeft, callSize = 0):

    if numPlayersLeft == 7:
        handOdds = postTurnOdds(hand, board, 7, 1000)
        handOdds += pokerMLOddsAdjustment(app)
        return preRiver7OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 6:
        handOdds = postTurnOdds(hand, board, 6, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.6
        return preRiver6OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 5:
        handOdds = postTurnOdds(hand, board, 5, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.2
        return preRiver5OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 4:
        handOdds = postTurnOdds(hand, board, 4, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.8
        return preRiver4OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 3:
        handOdds = postTurnOdds(hand, board, 3, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3.4
        return preRiver3OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 2:
        handOdds = postTurnOdds(hand, board, 2, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4
        return preRiver2OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 1:
        handOdds = postTurnOdds(hand, board, 1, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4.5
        return preRiver1OtherBodiAIAction(handOdds, callSize)

# pre river with 7 others
def preRiver7OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .25:
            action = ("Call")
        elif .25 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .35 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        elif handOdds > .5:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .2:
            action = ("Fold")
        elif .2 < handOdds <= .275:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
        elif .275 < handOdds <= .35:
            action = ("Call")
        elif .35 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum >= 66:
                action = ("Call")
            else:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum >= 25:
                action = ("Call")
            elif 25 < randNum <= 50:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)

    elif .04 < callSize <= .075:
        if handOdds <= .25:
            action = ("Fold")
        elif .25 < handOdds <= .325:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .325 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .7:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 6 others
def preRiver6OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .275:
            action = ("Call")
        elif .275 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .375 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        elif handOdds > .525:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .275:
            action = ("Fold")
        elif .275 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 40:
                action = ("Call")
            else:
                action = ("Fold")
        elif .35 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .575:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .475:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .475 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .425:
            action = ("Fold")
        elif .425 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .725:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 5 others
def preRiver5OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .3:
            action = ("Call")
        elif .3 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .375 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .275:
            action = ("Fold")
        elif .275 < handOdds <= .325:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .325 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .325:
            action = ("Fold")
        elif .325 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .425:
            action = ("Fold")
        elif .425 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .725:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 4 others
def preRiver4OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .325:
            action = ("Call")
        elif .325 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .4 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .3:
            action = ("Fold")
        elif .3 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .35 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .325:
            action = ("Fold")
        elif .325 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .4 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .425:
            action = ("Fold")
        elif .425 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .725:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 3 others
def preRiver3OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .35:
            action = ("Call")
        elif .35 < handOdds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .425 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .425 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .475:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .475 < handOdds <= .675:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .725:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 2 others
def preRiver2OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .4:
            action = ("Call")
        elif .4 < handOdds <= .475:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .475 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .4:
            action = ("Fold")
        elif .4 < handOdds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .45 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .525 < handOdds <= .675:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .5:
            action = ("Fold")
        elif .5 < handOdds <= .675:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .8:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 1 other
def preRiver1OtherBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .525:
            action = ("Call")
        elif .525 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .625 < handOdds <= .775:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .475:
            action = ("Fold")
        elif .475 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .575 < handOdds <= .675:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .6:
            action = ("Fold")
        elif .6 < handOdds <= .7:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .7 < handOdds <= .875:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .65:
            action = ("Fold")
        elif .65 < handOdds <= .8:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .925:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# print(preRiverBodiAI(["AD","AS"], ["7H","3D","7D","7S"], 4, 0.1))

# runs post river agressive AI
def postRiverBodiAI(app, hand, board, numPlayersLeft, callSize = 0):

    if numPlayersLeft == 7:
        handOdds = postRiverOdds(hand, board, 7, 1000)
        handOdds += pokerMLOddsAdjustment(app)
        return postRiver7OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 6:
        handOdds = postRiverOdds(hand, board, 6, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.75
        return postRiver6OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 5:
        handOdds = postRiverOdds(hand, board, 5, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.5
        return postRiver5OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 4:
        handOdds = postRiverOdds(hand, board, 4, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3.25
        return postRiver4OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 3:
        handOdds = postRiverOdds(hand, board, 3, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4
        return postRiver3OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 2:
        handOdds = postRiverOdds(hand, board, 2, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4.75
        return postRiver2OthersBodiAIAction(handOdds, callSize)

    elif numPlayersLeft == 1:
        handOdds = postRiverOdds(hand, board, 1, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 5.5
        return postRiver1OtherBodiAIAction(handOdds, callSize)

# post river with 7 others
def postRiver7OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .275:
            action = ("Call")
        elif .275 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .375 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        elif handOdds > .525:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .225:
            action = ("Fold")
        elif .225 < handOdds <= .3:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
        elif .3 < handOdds <= .375:
            action = ("Call")
        elif .375 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum >= 66:
                action = ("Call")
            else:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum >= 25:
                action = ("Call")
            elif 25 < randNum <= 50:
                randBet = random.randint(1, 2)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)

    elif .04 < callSize <= .075:
        if handOdds <= .275:
            action = ("Fold")
        elif .275 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .35 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .4:
            action = ("Fold")
        elif .4 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .725:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 6 others
def postRiver6OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .3:
            action = ("Call")
        elif .3 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .4 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        elif handOdds > .55:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .3:
            action = ("Fold")
        elif .3 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 40:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .575:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .5 < handOdds <= .675:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .75:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 5 others
def postRiver5OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .325:
            action = ("Call")
        elif .325 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .4 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .3:
            action = ("Fold")
        elif .3 < handOdds <= .35:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .35 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .4 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .75:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 4 others
def postRiver4OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .35:
            action = ("Call")
        elif .35 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .425 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .325:
            action = ("Fold")
        elif .325 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .425 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .75:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 3 others
def postRiver3OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .375:
            action = ("Call")
        elif .375 < handOdds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .45 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .45 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .4:
            action = ("Fold")
        elif .4 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .5 < handOdds <= .7:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .475:
            action = ("Fold")
        elif .475 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .75:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 2 others
def postRiver2OthersBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .425:
            action = ("Call")
        elif .425 < handOdds <= .5:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .5 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .425:
            action = ("Fold")
        elif .425 < handOdds <= .475:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .475 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .475:
            action = ("Fold")
        elif .475 < handOdds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .55 < handOdds <= .7:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .5:
            action = ("Fold")
        elif .525 < handOdds <= .7:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .85:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 1 other
def postRiver1OtherBodiAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .55:
            action = ("Call")
        elif .55 < handOdds <= .65:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .65 < handOdds <= .8:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
        else:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .5:
            action = ("Fold")
        elif .5 < handOdds <= .6:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .6 < handOdds <= .7:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .65:
            action = ("Fold")
        elif .65 < handOdds <= .75:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .75 < handOdds <= .925:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .75:
            action = ("Fold")
        elif .75 < handOdds <= .925:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")

    elif callSize > .2:
        if handOdds <= .95:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# print(postRiverBodiAI(["AD","AS"], ["7H","3D","7D","7S"], 4, 0.1))