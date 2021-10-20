# Balanced/Wernink poker AI
from montecarloodds import *
from pokerml import *

# runs pre flop balanced AI
def preFlopWerninkAI(app, hand, numPlayersLeft, betSize = 1/100):

    handString = ""
    for card in hand:
        handString += card

    if numPlayersLeft == 7:
        try:
            handOdds = call8PlayerDict1326()[handString]
        except:
            handOdds = call8PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app)

        return preFlop7OthersWerninkAIAction(handOdds, betSize), handOdds

    elif numPlayersLeft == 6:
        try:
            handOdds = call7PlayerDict1326()[handString]
        except:
            handOdds = call7PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 1.25

        return preFlop6OthersWerninkAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 5:
        try:
            handOdds = call6PlayerDict1326()[handString]
        except:
            handOdds = call6PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 1.5

        return preFlop5OthersWerninkAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 4:
        try:
            handOdds = call5PlayerDict1326()[handString]
        except:
            handOdds = call5PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 1.75
        
        return preFlop4OthersWerninkAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 3:
        try:
            handOdds = call4PlayerDict1326()[handString]
        except:
            handOdds = call4PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 2
        
        return preFlop3OthersWerninkAIAction(handOdds, betSize), handOdds
        
    elif numPlayersLeft == 2:
        try:
            handOdds = call3PlayerDict1326()[handString]
        except:
            handOdds = call3PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 2.25
        
        return preFlop2OthersWerninkAIAction(handOdds, betSize), handOdds
    
    elif numPlayersLeft == 1:
        try:
            handOdds = call2PlayerDict1326()[handString]
        except:
            handOdds = call2PlayerDict1326()[handString[2:] + handString[0:2]]

        handOdds += pokerMLOddsAdjustment(app) * 2.5
        
        return preFlop1OtherWerninkAIAction(handOdds, betSize), handOdds

# pre flop with 7 others
def preFlop7OthersWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds < .1:
            action = ("Fold")
        elif .1 <= odds < .11:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif .11 <= odds <= .16:
            action = ("Call")
        elif .16 < odds <= .19:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        elif .19 < odds <= .27:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            elif 25 < randNum <= 50:
                randBet = random.randint(3, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
        elif odds > .27:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            elif 50 < randNum <= 75:
                randBet = random.randint(3, 5)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .14:
            action = ("Fold")
        elif .14 < odds <= .16:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds > .16:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .16:
            action = ("Fold")
        elif .16 < odds <= .215:
            randNum = random.randint(1, 100)
            if randNum <= 20:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds > .215:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds < .22:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
    
    elif betSize > .2:
        if odds < .225:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 6 others
def preFlop6OthersWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .115:
            action = ("Fold")
        elif .115 < odds <= .22:
            action = ("Call")
        elif .22 < odds <= .275:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .13:
            action = ("Fold")
        elif .13 < odds <= .165:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .19:
            action = ("Fold")
        elif .19 < odds <= .25:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .215:
            action = ("Fold")
        elif .215 < odds <= .275:
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
        if odds <= .25:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 5 others
def preFlop5OthersWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .185:
            action = ("Fold")
        elif .185 < odds <= .25:
            action = ("Call")
        elif .25 < odds <= .3:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .215:
            action = ("Fold")
        elif .215 < odds <= .275:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .25:
            action = ("Fold")
        elif .25 < odds <= .3:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .275:
            action = ("Fold")
        elif .275 < odds <= .35:
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
        if odds <= .375:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 4 others
def preFlop4OthersWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .21:
            action = ("Fold")
        elif .21 < odds <= .3:
            action = ("Call")
        elif .3 < odds <= .375:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .25:
            action = ("Fold")
        elif .25 < odds <= .3:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .3:
            action = ("Fold")
        elif .3 < odds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .325:
            action = ("Fold")
        elif .325 < odds <= .425:
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
        if odds <= .45:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 3 others
def preFlop3OthersWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .25:
            action = ("Fold")
        elif .25 < odds <= .35:
            action = ("Call")
        elif .35 < odds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 50:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .325:
            action = ("Fold")
        elif .325 < odds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .375:
            action = ("Fold")
        elif .375 < odds <= .43:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .4:
            action = ("Fold")
        elif .4 < odds <= .485:
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

# pre flop with 2 others
def preFlop2OthersWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .325:
            action = ("Fold")
        elif .325 < odds <= .425:
            action = ("Call")
        elif .425 < odds <= .5:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call") 
    
    elif .01 < betSize <= .04:
        if odds <= .375:
            action = ("Fold")
        elif .375 < odds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds >= .675:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                randBet = random.randint(3, 5)
                action = ("Bet", randBet/100)
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .425:
            action = ("Fold")
        elif .425 < odds <= .55:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .5:
            action = ("Fold")
        elif .5 < odds <= .575:
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
        if odds <= .575:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")

    return action

# pre flop with 1 other
def preFlop1OtherWerninkAIAction(odds, betSize):
    action = ""

    if betSize <= .01:
        if odds <= .53:
            action = ("Fold")
        elif .53 < odds <= .63:
            action = ("Call")
        elif .63 < odds <= .73:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)
            else:
                action = ("Call")
    
    elif .01 < betSize <= .04:
        if odds <= .575:
            action = ("Fold")
        elif .575 < odds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        elif odds >= .78:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                randBet = random.randint(3, 5)
                action = ("Bet", randBet/100)
        else:
            action = ("Call")
    
    elif .04 < betSize <= .075:
        if odds <= .63:
            action = ("Fold")
        elif .63 < odds <= .68:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")
    
    elif .075 < betSize <= .2:
        if odds <= .68:
            action = ("Fold")
        elif .68 < odds <= .78:
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
        if odds <= .78:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 25:
                action = ("Call")
            else:
                action = ("Fold")


    return action

# print(preFlopWerninkAI(["AC","TH"], 5, .35))

# runs pre turn balanced AI
def preTurnWerninkAI(app, hand, board, numPlayersLeft, callSize = 0):

    if numPlayersLeft == 7:
        handOdds = postFlopOdds(hand, board, 7, 1000)
        handOdds += pokerMLOddsAdjustment(app)
        return preTurn7OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 6:
        handOdds = postFlopOdds(hand, board, 6, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.4
        return preTurn6OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 5:
        handOdds = postFlopOdds(hand, board, 5, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.8
        return preTurn5OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 4:
        handOdds = postFlopOdds(hand, board, 4, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.2
        return preTurn4OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 3:
        handOdds = postFlopOdds(hand, board, 3, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.6
        return preTurn3OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 2:
        handOdds = postFlopOdds(hand, board, 2, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3
        return preTurn2OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 1:
        handOdds = postFlopOdds(hand, board, 1, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3.5
        return preTurn1OtherWerninkAIAction(handOdds, callSize)
    
# pre turn with 7 others
def preTurn7OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .235:
            action = ("Call")
        elif .235 < handOdds <= .375:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .185:
            action = ("Fold")
        elif .185 < handOdds <= .275:
            randNum = random.randint(1, 100)
            if randNum <= 85:
                action = ("Call")
            else:
                action = ("Fold")
        elif .275 < handOdds <= .375:
            action = ("Call")
        elif .375 < handOdds <= .525:
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
        if handOdds <= .235:
            action = ("Fold")
        elif .235 < handOdds <= .325:
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
        elif handOdds > .525:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .53:
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
        if handOdds <= .675:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 6 others
def preTurn6OthersWerninkAIAction(handOdds, callSize):
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
        elif handOdds > .525:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .285:
            action = ("Fold")
        elif .285 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .575:
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
        if handOdds <= .73:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 5 others
def preTurn5OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .285:
            action = ("Call")
        elif .285 < handOdds <= .375:
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
        if handOdds <= .265:
            action = ("Fold")
        elif .265 < handOdds <= .325:
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
        if handOdds <= .3:
            action = ("Fold")
        elif .3 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .575:
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

# pre turn with 4 others
def preTurn4OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .32:
            action = ("Call")
        elif .32 < handOdds <= .395:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .395 < handOdds <= .575:
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
        if handOdds <= .32:
            action = ("Fold")
        elif .32 < handOdds <= .4:
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
        elif .425 < handOdds <= .63:
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
        if handOdds <= .73:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 3 others
def preTurn3OthersWerninkAIAction(handOdds, callSize):
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
        elif .45 < handOdds <= .63:
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
        if handOdds <= .73:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 2 others
def preTurn2OthersWerninkAIAction(handOdds, callSize):
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
        if handOdds <= .775:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre turn with 1 other
def preTurn1OtherWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .53:
            action = ("Call")
        elif .53 < handOdds <= .63:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .63 < handOdds <= .78:
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
        if handOdds <= .53:
            action = ("Fold")
        elif .53 < handOdds <= .68:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .68 < handOdds <= .875:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .61:
            action = ("Fold")
        elif .61 < handOdds <= .79:
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
        if handOdds <= .88:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# print(preTurnWerninkAI(["AD","AS"], ["7H","3D","7D"], 4, 0.1))

# runs pre river balanced AI
def preRiverWerninkAI(app, hand, board, numPlayersLeft, callSize = 0):

    if numPlayersLeft == 7:
        handOdds = postTurnOdds(hand, board, 7, 1000)
        handOdds += pokerMLOddsAdjustment(app)
        return preRiver7OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 6:
        handOdds = postTurnOdds(hand, board, 6, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.6
        return preRiver6OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 5:
        handOdds = postTurnOdds(hand, board, 5, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.2
        return preRiver5OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 4:
        handOdds = postTurnOdds(hand, board, 4, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.8
        return preRiver4OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 3:
        handOdds = postTurnOdds(hand, board, 3, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3.4
        return preRiver3OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 2:
        handOdds = postTurnOdds(hand, board, 2, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4
        return preRiver2OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 1:
        handOdds = postTurnOdds(hand, board, 1, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4.5
        return preRiver1OtherWerninkAIAction(handOdds, callSize)

# pre river with 7 others
def preRiver7OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .265:
            action = ("Call")
        elif .265 < handOdds <= .375:
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
        if handOdds <= .22:
            action = ("Fold")
        elif .22 < handOdds <= .3:
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
        if handOdds <= .265:
            action = ("Fold")
        elif .265 < handOdds <= .35:
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

# pre river with 6 others
def preRiver6OthersWerninkAIAction(handOdds, callSize):
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
                randBet = random.randint(2, 4)
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
        elif handOdds > .6:
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
        elif .5 < handOdds <= .67:
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

# pre river with 5 others
def preRiver5OthersWerninkAIAction(handOdds, callSize):
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

# pre river with 4 others
def preRiver4OthersWerninkAIAction(handOdds, callSize):
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
                randBet = random.randint(2, 4)
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

# pre river with 3 others
def preRiver3OthersWerninkAIAction(handOdds, callSize):
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

# pre river with 2 others
def preRiver2OthersWerninkAIAction(handOdds, callSize):
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
                randBet = random.randint(2, 4)
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
        if handOdds <= .53:
            action = ("Fold")
        elif .53 < handOdds <= .7:
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
        if handOdds <= .825:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# pre river with 1 other
def preRiver1OtherWerninkAIAction(handOdds, callSize):
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
                randBet = random.randint(2, 4)
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
        if handOdds <= .63:
            action = ("Fold")
        elif .63 < handOdds <= .73:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .73 < handOdds <= .9:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .675:
            action = ("Fold")
        elif .675 < handOdds <= .83:
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

# print(preRiverWerninkAI(["AD","AS"], ["7H","3D","7D","7S"], 4, 0.1))

# runs post river balanced AI
def postRiverWerninkAI(app, hand, board, numPlayersLeft, callSize = 0):

    if numPlayersLeft == 7:
        handOdds = postRiverOdds(hand, board, 7, 1000)
        handOdds += pokerMLOddsAdjustment(app)
        return postRiver7OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 6:
        handOdds = postRiverOdds(hand, board, 6, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 1.75
        return postRiver6OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 5:
        handOdds = postRiverOdds(hand, board, 5, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 2.5
        return postRiver5OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 4:
        handOdds = postRiverOdds(hand, board, 4, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 3.25
        return postRiver4OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 3:
        handOdds = postRiverOdds(hand, board, 3, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4
        return postRiver3OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 2:
        handOdds = postRiverOdds(hand, board, 2, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 4.75
        return postRiver2OthersWerninkAIAction(handOdds, callSize)

    elif numPlayersLeft == 1:
        handOdds = postRiverOdds(hand, board, 1, 1000)
        handOdds += pokerMLOddsAdjustment(app) * 5.5
        return postRiver1OtherWerninkAIAction(handOdds, callSize)

# post river with 7 others
def postRiver7OthersWerninkAIAction(handOdds, callSize):
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
        elif handOdds > .555:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .25:
            action = ("Fold")
        elif .25 < handOdds <= .325:
            randNum = random.randint(1, 100)
            if randNum <= 66:
                action = ("Call")
            else:
                action = ("Fold")
        elif .325 < handOdds <= .4:
            action = ("Call")
        elif .4 < handOdds <= .55:
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
        if handOdds <= .3:
            action = ("Fold")
        elif .3 < handOdds <= .375:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .375 < handOdds <= .575:
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

# post river with 6 others
def postRiver6OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .32:
            action = ("Call")
        elif .32 < handOdds <= .425:
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
        elif handOdds > .575:
            randNum = random.randint(1, 100)
            if randNum <= 10:
                action = ("Call")
            elif 10 < randNum <= 50:
                randBet = random.randint(2, 3)
                action = ("Bet", randBet/100)
            else:
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .325:
            action = ("Fold")
        elif .325 < handOdds <= .4:
            randNum = random.randint(1, 100)
            if randNum <= 40:
                action = ("Call")
            else:
                action = ("Fold")
        elif .4 < handOdds <= .625:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        elif handOdds > .625:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .4:
            action = ("Fold")
        elif .4 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .525 < handOdds <= .7:
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
        elif .475 < handOdds <= .675:
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
        if handOdds <= .775:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 5 others
def postRiver5OthersWerninkAIAction(handOdds, callSize):
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
                randBet = random.randint(2, 4)
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
        elif .375 < handOdds <= .575:
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
        elif .375 < handOdds <= .425:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .425 < handOdds <= .65:
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
        elif .475 < handOdds <= .675:
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
        if handOdds <= .775:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 4 others
def postRiver4OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .375:
            action = ("Call")
        elif .375 < handOdds <= .43:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .43 < handOdds <= .65:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .35:
            action = ("Fold")
        elif .35 < handOdds <= .4:
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

    elif .04 < callSize <= .075:
        if handOdds <= .375:
            action = ("Fold")
        elif .375 < handOdds <= .45:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .45 < handOdds <= .63:
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
        elif .475 < handOdds <= .675:
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
        if handOdds <= .775:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 3 others
def postRiver3OthersWerninkAIAction(handOdds, callSize):
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
        elif .475 < handOdds <= .625:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .4:
            action = ("Fold")
        elif .4 < handOdds <= .475:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .475 < handOdds <= .625:
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
        elif .425 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .525 < handOdds <= .725:
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
        if handOdds <= .775:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 2 others
def postRiver2OthersWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .45:
            action = ("Call")
        elif .45 < handOdds <= .525:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .525 < handOdds <= .65:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .45:
            action = ("Fold")
        elif .45 < handOdds <= .5:
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

    elif .04 < callSize <= .075:
        if handOdds <= .5:
            action = ("Fold")
        elif .5 < handOdds <= .575:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .575 < handOdds <= .725:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .53:
            action = ("Fold")
        elif .53 < handOdds <= .73:
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
        if handOdds <= .88:
            action = ("Fold")
        else:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")

    return action, handOdds

# post river with 1 other
def postRiver1OtherWerninkAIAction(handOdds, callSize):
    action = ""

    if callSize == 0:
        if handOdds <= .575:
            action = ("Call")
        elif .575 < handOdds <= .675:
            randNum = random.randint(1, 100)
            if randNum <= 50:
                action = ("Call")
            else:
                action = ("Bet", 1/100)
        elif .675 < handOdds <= .83:
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
                randBet = random.randint(2, 4)
                action = ("Bet", randBet/100)

    elif 0 < callSize <= .04:
        if handOdds <= .53:
            action = ("Fold")
        elif .53 < handOdds <= .63:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .63 < handOdds <= .73:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .04 < callSize <= .075:
        if handOdds <= .675:
            action = ("Fold")
        elif .675 < handOdds <= .775:
            randNum = random.randint(1, 100)
            if randNum <= 33:
                action = ("Call")
            else:
                action = ("Fold")
        elif .775 < handOdds <= .95:
            randNum = random.randint(1, 100)
            if randNum <= 80:
                action = ("Call")
            else:
                action = ("Fold")
        else:
            action = ("Call")

    elif .075 < callSize <= .2:
        if handOdds <= .775:
            action = ("Fold")
        elif .775 < handOdds <= .95:
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

# print(postRiverWerninkAI(["AD","AS"], ["7H","3D","7D","7S"], 4, 0.1))