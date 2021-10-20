# this file holds the poker player class
from loadimages import *

# initiate a poker player class
class Pokerplayer(object):
    def __init__(self, number, type):
        self.playerNum = number
        self.playerType = type
        self.playerHand = []
        self.playerMoney = 1000
        self.playerBet = 0
        self.playerIn = True

# creates poker players in the poker player class
def createPokerPlayers(app, numOpponents = 1, level = "Hard", buyIn = 1000):

    # create eight poker players
    if level == "Hard":
        app.myPokerPlayer = Pokerplayer(0, "User")
        app.opp1PokerPlayer = Pokerplayer(1, "Wernink")
        app.opp2PokerPlayer = Pokerplayer(2, "Ganger")
        app.opp3PokerPlayer = Pokerplayer(3, "Sep")
        app.opp4PokerPlayer = Pokerplayer(4, "Wernink")
        app.opp5PokerPlayer = Pokerplayer(5, "Ganger")
        app.opp6PokerPlayer = Pokerplayer(6, "Sep")
        app.opp7PokerPlayer = Pokerplayer(7, "Wernink")
    elif level == "Medium":
        app.myPokerPlayer = Pokerplayer(0, "User")
        app.opp1PokerPlayer = Pokerplayer(1, "Ganger")
        app.opp2PokerPlayer = Pokerplayer(2, "Bodi")
        app.opp3PokerPlayer = Pokerplayer(3, "Wernink")
        app.opp4PokerPlayer = Pokerplayer(4, "Sep")
        app.opp5PokerPlayer = Pokerplayer(5, "Ganger")
        app.opp6PokerPlayer = Pokerplayer(6, "Bodi")
        app.opp7PokerPlayer = Pokerplayer(7, "Ganger")
    elif level == "Easy":
        app.myPokerPlayer = Pokerplayer(0, "User")
        app.opp1PokerPlayer = Pokerplayer(1, "Imran")
        app.opp2PokerPlayer = Pokerplayer(2, "Bodi")
        app.opp3PokerPlayer = Pokerplayer(3, "Ganger")
        app.opp4PokerPlayer = Pokerplayer(4, "Imran")
        app.opp5PokerPlayer = Pokerplayer(5, "Wernink")
        app.opp6PokerPlayer = Pokerplayer(6, "Bodi")
        app.opp7PokerPlayer = Pokerplayer(7, "Imran")

    aiPlayers = [app.opp1PokerPlayer,
                app.opp2PokerPlayer, app.opp3PokerPlayer, app.opp4PokerPlayer,
                app.opp5PokerPlayer, app.opp6PokerPlayer, app.opp7PokerPlayer]

    aiPlayerImages = [(app.cpu1Scaled, 1),
            (app.cpu2Scaled, 2), (app.cpu3Scaled, 3), (app.cpu4Scaled, 4),
            (app.cpu5Scaled, 5), (app.cpu6Scaled, 6), (app.cpu7Scaled, 7)]

    app.pokerPlayers = [app.myPokerPlayer]
    app.pokerPlayerImages = [(app.youScaled, 0)]

    # create a list of poker players and associate images with different player numbers
    for i in range(numOpponents):
        app.pokerPlayers.append(aiPlayers[i])
        app.pokerPlayerImages.append(aiPlayerImages[i])
        app.pokerPlayers[i].playerMoney = app.pokerBuyIn
    app.pokerPlayers[i+1].playerMoney = app.pokerBuyIn