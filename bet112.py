# by Nicholas Wernink

import math, random, time
from cmu_112_graphics import *
import decimal

from pokerclass import *
from loadimages import *
from pokerfunctions import *
from pokerkeypressed import *

from bodiAI import * # agressive AI
from gangerAI import * # conservative AI
from werninkAI import * # balanced AI
from imranAI import * # super agressive AI
from sepAI import * # super conservative AI

from pokerml import *

from database import *


########################
# Welcome Mode
########################

def welcomeMode_appStarted(app):
    
    # initiate variables for login
    app.enterUsername = False
    app.username = ""
    app.enterPassword = False
    app.password = ""
    app.loginError = False
    app.noAccount = False
    app.wrongPassword = False
    app.alreadyUser = False
    app.accountBalance = 0
    app.pokerML = 0
    app.pokerMLWeight = 0

def welcomeMode_mousePressed(app, event):
    # print(event.x, event.y)

    # checks if you click create an account
    if (app.width/2 - 80 <= event.x <= app.width/2 + 80) and (app.height/2 + 60 <= event.y <= app.height/2 + 90):
        # checks to see if username and password are valid
        if (len(app.username) >= 3) and (len(app.password) >= 3):

            conn = sqlite3.connect("user.db")
            cursor = conn.cursor()
            
            hasAccount = False
            accountBalance = 0
            for row in cursor.execute('SELECT * FROM users ORDER BY account_balance'):
                if row[0] == app.username:
                    hasAccount = True

            if hasAccount:
                app.alreadyUser = True
                app.loginError = False
                app.noAccount = False
                app.wrongPassword = False
            else:
                cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (app.username, app.password, 5000, 0, 0))
                app.accountBalance = 5000
                app.mode = "casinoMode"
                app.enterUsername = False
                app.enterPassword = False

            # commit actions to database, save, and close the connection
            conn.commit()
            conn.close()

    # checks if you click login
    if (app.width/2 - 30 <= event.x <= app.width/2 + 30) and (app.height/2 + 110 <= event.y <= app.height/2 + 140):
        # checks to see if username and password are valid
        if (len(app.username) >= 3) and (len(app.password) >= 3):

            # connect to user database
            conn = sqlite3.connect("user.db")
            cursor = conn.cursor()
            
            hasAccount = False
            correctPassword = False
            accountBalance = 0
            pokerML = 0
            pokerMLWeight = 0

            # loop through each user
            for row in cursor.execute('SELECT * FROM users ORDER BY account_balance'):
                if row[0] == app.username:
                    hasAccount = True
                    if row[1] == app.password:
                        correctPassword = True
                        accountBalance = row[2]
                        pokerML = row[3]
                        pokerMLWeight = row[4]
            
            # check if login credentials are correct
            if hasAccount and correctPassword:
                app.accountBalance = accountBalance
                app.pokerML = pokerML
                app.pokerMLWeight = pokerMLWeight
                app.mode = "casinoMode"
                app.enterUsername = False
                app.enterPassword = False

            # check if password is incorrect given username
            elif hasAccount and not correctPassword:
                app.wrongPassword = True
                app.enterUsername = False
                app.enterPassword = False
                app.loginError = False
                app.noAccount = False
                app.alreadyUser = False
            
            # if both username and password are incorrect
            else:
                app.noAccount = True
                app.enterUsername = False
                app.enterPassword = False
                app.loginError = False
                app.wrongPassword = False
                app.alreadyUser = False
            
            # commit actions to database, save, and close the connection
            conn.commit()
            conn.close()
 
        else:
            app.loginError = True
            app.enterUsername = False
            app.enterPassword = False

    # checks if you click username
    elif (app.width/2 - 100 <= event.x <= app.width/2 + 100) and (app.height/2 - 10 <= event.y <= app.height/2 + 10):
        app.enterUsername = True
        app.enterPassword = False

    # checks if you click password
    elif (app.width/2 - 100 <= event.x <= app.width/2 + 100) and (app.height/2 + 25 <= event.y <= app.height/2 + 45):
        app.enterPassword = True
        app.enterUsername = False

    # checks if you click out of username or password or login
    else:
        app.enterUsername = False
        app.enterPassword = False

        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * FROM users ORDER BY account_balance'):
            print(row)

        conn.commit()
        conn.close()

def welcomeMode_keyPressed(app, event):

    # checks if user has clicked to enter their username
    if app.enterUsername:
        # checks if key presses are legal characters
        if (event.key.isalnum()) and (len(event.key) == 1):
            app.username += event.key
        elif event.key == "Delete":
            app.username = app.username[:-1]

    # checks if user has clicked to enter their password
    elif app.enterPassword:
        # checks if key presses are legal characters
        if (event.key.isalnum()) and (len(event.key) == 1):
            app.password += event.key
        elif event.key == "Delete":
            app.password = app.password[:-1]

def welcomeMode_redrawAll(app, canvas):
    # creates the welcome page

    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan2")

    # welcome text
    canvas.create_text(app.width/2, app.height/4, text = "Welcome To",
                font = "Times 60 bold", fill = "black")
    canvas.create_text(app.width/2, app.height/4 + 75, text = "bet112!",
                font = "Times 60 bold", fill = "black")

    # username text
    if len(app.username) > 0 or app.enterUsername:
        if app.enterUsername:
            font = "Times 17 bold"
        else:
            font = "Times 17"
        canvas.create_text(app.width/2, app.height/2,
                text = f'Username: {app.username}', font = font)
    else:
        canvas.create_text(app.width/2, app.height/2,
                text = "Username:  ______________", font = "Times 17")

    # password text
    if app.enterPassword:
        canvas.create_text(app.width/2, app.height/2 + 35,
                text = f'Password: {app.password}', font = "Times 17 bold")
    elif len(app.password) > 0:
        password = len(app.password) * "*"
        canvas.create_text(app.width/2, app.height/2 + 35,
                text = f'Password: {password}', font = "Times 17")
    else:
        canvas.create_text(app.width/2, app.height/2 + 35,
                text = "Password:  ______________", font = "Times 17")


    canvas.create_text(app.width/2, app.height/2 + 75, text = "Create an Account",
                font = "Times 20 italic")
    canvas.create_text(app.width/2, app.height/2 + 100, text = "or",
                font = "Times 17")
    canvas.create_text(app.width/2, app.height/2 + 125, text = "Login",
                font = "Times 20 italic")

    # login error text
    if app.loginError:
        canvas.create_text(app.width/2, app.height/2 + 200,
                text = "Invalid username/password", fill = "red")
        canvas.create_text(app.width/2, app.height/2 + 225,
                text = "Please enter a username/password that is longer than 2 characters!",
                fill = "red")
    elif app.noAccount:
        canvas.create_text(app.width/2, app.height/2 + 200,
                text = "No account associated with that username", fill = "red")
    elif app.wrongPassword:
        canvas.create_text(app.width/2, app.height/2 + 200,
                text = "Password is incorrect, please try again", fill = "red")
    elif app.alreadyUser:
        canvas.create_text(app.width/2, app.height/2 + 200,
                text = "Username is already in use, please try a new one", fill = "red")


########################
# Casino Mode
########################

def casinoMode_mousePressed(app, event):
    # print(event.x, event.y)

    # checks if you click help
    if (25 <= event.x <= 75) and (35 <= event.y <= 65):
        app.mode = "casinoHelpMode"

    # checks if you click log out
    elif (app.width - 90 <= event.x <= app.width - 30) and (35 <= event.y <= 65):
        app.mode = "welcomeMode"
        welcomeMode_appStarted(app)

    # checks if you click blackjack
    # elif (app.width/2 - 390 <= event.x <= app.width/2 - 210) and (app.height/2 - 200 <= event.y <= app.height/2):
    #     app.mode = "blackjackMode"

    # checks if you click texas hold'em
    elif (app.width/2 - 200 <= event.x <= app.width/2 + 200) and (app.height/2 - 200 <= event.y <= app.height/2 + 200):
        app.mode = "pokerOptionMode"
        pokerOptionMode_appStarted(app)

    # checks if you click roulette
    # elif (app.width/2 - 140 <= event.x <= app.width/2 + 140) and (app.height/2 - 50 <= event.y <= app.height/2 + 150):
    #     app.mode = "rouletteMode"

def casinoMode_redrawAll(app, canvas):
    # creates the welcome casino page

    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan2")

    # welcome to the casino text
    canvas.create_text(app.width/2, 60, text = f'Hi {app.username}!',
                font = "Times 30")
    canvas.create_text(app.width/2, 165, text = "Texas Hold'em",
                font = "Times 30 italic")

    # blackjack image and text
    # canvas.create_image(app.width/2 - 300, app.height/2 - 100,
    #             image=ImageTk.PhotoImage(app.blackjackScaledImage))
    # canvas.create_text(app.width/2 - 300, app.height/2 - 225,
    #             text = "Blackjack", font = "Times 25 italic")

    # poker image and text
    # canvas.create_image(app.width/2 + 300, app.height/2 - 100,
    #             image=ImageTk.PhotoImage(app.pokerScaledImage))
    # canvas.create_text(app.width/2 + 302.5, app.height/2 - 225,
    #             text = "Texas Hold'em", font = "Times 25 italic")

    # roulette image and text
    # canvas.create_image(app.width/2, app.height/2 + 50,
    #             image=ImageTk.PhotoImage(app.rouletteScaledImage))
    # canvas.create_text(app.width/2, app.height/2 - 75,
    #             text = "Roulette", font = "Times 25 italic")

    # poker image and text
    canvas.create_image(app.width/2, app.height/2,
                image=ImageTk.PhotoImage(app.pokerScaledImage))

    # canvas.create_text(app.width/2, app.height/2 - 100,
    #             text = "Texas Hold'em", font = "Times 25 italic")

    # generates account balance text with percent gain/loss
    if app.accountBalance > 5000:
        balanceText = f'${round(app.accountBalance, 2)} (+{round((app.accountBalance - 5000)/5000 * 100, 3)}%)'
        fill = "green"
    elif app.accountBalance < 5000:
        balanceText = f'${round(app.accountBalance, 2)} ({round((app.accountBalance - 5000)/5000 * 100, 3)}%)'
        fill = "red"
    else:
        balanceText = f'${round(app.accountBalance, 2)} (0.00%)'
        fill = "black"

    # account balance text
    canvas.create_text(app.width/2, app.height - 150,
                text = "Account Balance", font = "Times 25 bold") 
    canvas.create_text(app.width/2, app.height - 100, text = balanceText,
                font = "Times 20", fill = fill)

    # help and log out text
    canvas.create_text(50, 50, text = "Help", font = "Times 15")
    canvas.create_text(app.width - 60, 50, text = "Log Out", font = "Times 15")


########################
# Casino Help Mode
########################

def casinoHelpMode_mousePressed(app, event):
    # checks if you click back
    if (25 <= event.x <= 75) and (35 <= event.y <= 65):
        app.mode = "casinoMode"

    # checks if you click log out
    elif (app.width - 90 <= event.x <= app.width - 30) and (35 <= event.y <= 65):
        app.mode = "welcomeMode"
        welcomeMode_appStarted(app)

def casinoHelpMode_redrawAll(app, canvas):
    # creates the casino help page

    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan2")

    canvas.create_text(app.width/2, 60, text = "Casino Instructions",
                font = "Times 30")

    # casino instructions
    instructions = ["Play no limit Texas Hold'em poker by clicking on the image of the playing cards",
        "Adjust the number of opponents you would like to play against, the level of difficulty and the buy in",
        "Check your account balance at the bottom of the page to see how you are doing",
        "Don't worry about saving anything as all of your information is automatically updated",
        "Have fun trying to beat the AIs!"]
    for i in range(len(instructions)):
        canvas.create_text(app.width/2, 125 + i*40, text = instructions[i],
                font = f"Times 20")

    # back and log out text
    canvas.create_text(50, 50, text = "Back", font = "Times 15")
    canvas.create_text(app.width - 60, 50, text = "Log Out", font = "Times 15")


########################
# Poker User Option Mode
########################

def pokerOptionMode_appStarted(app):
    app.numOpponentsClicked = 0
    app.pokerLevelClicked = ""
    app.buyInClicked = False
    app.buyInError = False

def pokerOptionMode_keyPressed(app, event):

    if app.buyInClicked:
        if event.key.isdigit():
            if app.pokerBuyIn*10 + int(event.key) <= app.accountBalance:
                app.pokerBuyIn = app.pokerBuyIn*10 + int(event.key)
        elif event.key == "Delete":
            app.pokerBuyIn //= 10
        if app.pokerBuyIn >= 2:
            app.buyInError = False

def pokerOptionMode_mousePressed(app, event):

    # checks if you click the number of opponents
    if (app.width/2 - 350 <= event.x <= app.width/2 - 275) and (250 <= event.y <= 325):
        app.pokerNumOpponents = 1
        app.numOpponentsClicked = 1
    elif (app.width/2 - 275 <= event.x <= app.width/2 - 200) and (250 <= event.y <= 325):
        app.pokerNumOpponents = 2
        app.numOpponentsClicked = 2
    elif (app.width/2 - 200 <= event.x <= app.width/2 - 125) and (250 <= event.y <= 325):
        app.pokerNumOpponents = 3
        app.numOpponentsClicked = 3
    elif (app.width/2 - 350 <= event.x <= app.width/2 - 275) and (325 <= event.y <= 400):
        app.pokerNumOpponents = 4
        app.numOpponentsClicked = 4
    elif (app.width/2 - 275 <= event.x <= app.width/2 - 200) and (325 <= event.y <= 400):
        app.pokerNumOpponents = 5
        app.numOpponentsClicked = 5
    elif (app.width/2 - 200 <= event.x <= app.width/2 - 125) and (325 <= event.y <= 400):
        app.pokerNumOpponents = 6
        app.numOpponentsClicked = 6
    elif (app.width/2 - 350 <= event.x <= app.width/2 - 125) and (400 <= event.y <= 475):
        app.pokerNumOpponents = 7
        app.numOpponentsClicked = 7

    # checks if you click the level of the AI
    if (app.width/2 + 125 <= event.x <= app.width/2 + 350) and (250 <= event.y <= 325):
        app.pokerLevel = "Easy"
        app.pokerLevelClicked = "Easy"
    elif (app.width/2 + 125 <= event.x <= app.width/2 + 350) and (325 <= event.y <= 400):
        app.pokerLevel = "Medium"
        app.pokerLevelClicked = "Medium"
    elif (app.width/2 + 125 <= event.x <= app.width/2 + 350) and (400 <= event.y <= 475):
        app.pokerLevel = "Hard"
        app.pokerLevelClicked = "Hard"

    # checks if you click the buy in amount
    if (app.width/2 - 50 <= event.x <= app.width/2 + 50) and (app.height - 225 <= event.y <= app.height - 175):
        app.buyInClicked = not app.buyInClicked
    else:
        app.buyInClicked = False

    # checks if you click play
    if (app.width/2 - 50 <= event.x <= app.width/2 + 50) and (app.height - 125 <= event.y <= app.height - 75) and (app.pokerBuyIn >= 2):
        app.mode = "pokerMode"
        pokerMode_appStarted(app)
        random.shuffle(app.pokerPlayerImages)
    elif (app.width/2 - 50 <= event.x <= app.width/2 + 50) and (app.height - 125 <= event.y <= app.height - 75) and (app.pokerBuyIn < 2):
        app.buyInError = True


    # checks if you click back
    if (25 <= event.x <= 75) and (35 <= event.y <= 65):
        app.mode = "casinoMode"

    # checks if you click log out
    elif (app.width - 90 <= event.x <= app.width - 30) and (35 <= event.y <= 65):
        app.mode = "welcomeMode"
        welcomeMode_appStarted(app)

def pokerOptionMode_redrawAll(app, canvas):

    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan2")

    canvas.create_text(app.width/2, 60, text = "Poker Mode Options",
                font = "Times 30")

    canvas.create_text((app.width/2 - 350 + app.width/2 - 125)/2, 215,
                text = "Select the Number of Opponents", font = "Times 20 bold")

    # creates the boxes for the number of players
    for i in range(3):
        for j in range(2):
            x1 = app.width/2 - 350 + i*75
            y1 = 250 + j*75
            x2 = app.width/2 - 350 + (i+1)*75
            y2 = 250 + (j+1)*75
            if j*3 + i + 1 == app.numOpponentsClicked:
                fill = "green2"
            else:
                fill = "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill = fill)
            canvas.create_text((x1 + x2)/2, (y1 + y2)/2, text = j*3 + i + 1,
                font = "Times 20")

    if app.numOpponentsClicked == 7:
        fill = "green2"
    else:
        fill = "white"

    canvas.create_rectangle(app.width/2 - 350, y1 + 75, app.width/2 - 125,
            y2 + 75, fill = fill)
    canvas.create_text((app.width/2 - 350 + app.width/2 - 125)/2,
            (y1 + 75 + y2 + 75)/2, text = 7, font = "Times 20")
    

    canvas.create_text((app.width/2 + 125 + app.width/2 + 350)/2, 215,
            text = "Select the Level of Difficulty", font = "Times 20 bold")

    # creates the boxes for the level of play
    levels = ["Easy", "Medium", "Hard"]
    for i in range(3):
        x1 = app.width/2 + 125
        y1 = 250 + i*75
        x2 = app.width/2 + 350
        y2 = 250 + (i+1)*75
        if app.pokerLevelClicked == levels[i]:
            fill = "green2"
        else:
            fill = "white"
        canvas.create_rectangle(x1, y1, x2, y2, fill = fill)
        canvas.create_text((x1 + x2)/2, (y1 + y2)/2, text = levels[i],
                font = "Times 20")

    # creates the buy in option
    canvas.create_text(app.width/2, (app.height*2 - 500)/2,
            text = "Type in Your Desired Buy In", font = "Times 20 bold")
    canvas.create_rectangle(app.width/2 - 50, app.height - 225, app.width/2 + 50,
            app.height - 175, fill = "white")
    if app.buyInClicked:
        bold = " bold"
    else:
        bold = ""
    canvas.create_text((app.width/2 - 50 + app.width/2 + 50)/2,
            (app.height - 225 + app.height - 175)/2, text = f"${app.pokerBuyIn}",
            fill = "black", font = f"Times 20{bold}")

    # creates the play button
    canvas.create_rectangle(app.width/2 - 50, app.height - 125,
            app.width/2 + 50, app.height - 75, fill = "white")
    canvas.create_text((app.width/2 - 50 + app.width/2 + 50)/2,
            (app.height - 125 + app.height - 75)/2, text = "Play!",
            font = "Times 20 bold")
    
    if app.buyInError:
        canvas.create_text(app.width/2, app.height - 35,
            text = "Buy in amount must be greater than $2", fill = "red")

    # back and log out text
    canvas.create_text(50, 50, text = "Back", font = "Times 15")
    canvas.create_text(app.width - 60, 50, text = "Log Out", font = "Times 15")


########################
# Poker Mode
########################

# creates the poker page with table and icons
def generatePokerTable(app, canvas):

    canvas.create_text(app.width/2, 60, text = "Texas Hold'em!",
                font = "Times 30")
    
    # back and help text
    canvas.create_text(50, 50, text = "Back", font = "Times 15")
    canvas.create_text(app.width - 60, 50, text = "Help", font = "Times 15")

    # creates poker table
    canvas.create_oval(app.width/2 - 400, 220, app.width/2 + 400, 520, fill = "green", width = 20,
                outline = "goldenrod")

    # dealer image
    canvas.create_image(app.width/2, 160,
                image=ImageTk.PhotoImage(app.dealerScaledImage))
    # dealer icon
    canvas.create_oval(app.width/2 - 15, 240, app.width/2 + 15, 270,
                fill = "white")
    canvas.create_text(app.width/2 + 1, 255, text = "D", font = "Times 20 bold")

# create images and text around the board for all players randomly
def drawPlayersAroundBoard(app, canvas):
    
    # resets the action index
    actionIndex = app.pokerActionIndex
    if app.newPokerRound:
        actionIndex = -1

    # changes color of player text based on whose turn it its
    actionListColors = []
    for i in range(len(app.pokerPlayers)):
        if i == actionIndex:
            actionListColors.append("red")
        else:
            actionListColors.append("black")

    # player in spot 0
    canvas.create_image(app.width/2 + 200, app.height/2 - 205,
        image=ImageTk.PhotoImage(app.pokerPlayerImages[0][0]))
    if app.pokerPlayerImages[0][1] == 0:
        canvas.create_text(app.width/2 + 300, app.height/2 - 205,
            text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[0][1]].playerMoney, 2)}',
            font = "Times 20 bold", fill = actionListColors[0])
    else:
        canvas.create_text(app.width/2 + 300, app.height/2 - 205,
            text = f'CPU {app.pokerPlayerImages[0][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[0][1]].playerMoney, 2)}',
            font = "Times 20 bold", fill = actionListColors[0])

    # player in spot 1
    canvas.create_image(app.width/2 + 395, app.height/2 - 130,
        image=ImageTk.PhotoImage(app.pokerPlayerImages[1][0]))
    if app.pokerPlayerImages[1][1] == 0:
        canvas.create_text(app.width/2 + 495, app.height/2 - 130,
            text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[1][1]].playerMoney, 2)}',
            font = "Times 20 bold", fill = actionListColors[1])
    else:
        canvas.create_text(app.width/2 + 495, app.height/2 - 130,
            text = f'CPU {app.pokerPlayerImages[1][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[1][1]].playerMoney, 2)}',
            font = "Times 20 bold", fill = actionListColors[1])

    if len(app.pokerPlayers) > 2:
        # player in spot 2
        canvas.create_image(app.width/2 + 395, app.height/2 + 75,
            image=ImageTk.PhotoImage(app.pokerPlayerImages[2][0]))
        if app.pokerPlayerImages[2][1] == 0:
            canvas.create_text(app.width/2 + 495, app.height/2 + 75,
                text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[2][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[2])
        else:
            canvas.create_text(app.width/2 + 495, app.height/2 + 75,
                text = f'CPU {app.pokerPlayerImages[2][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[2][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[2])

    if len(app.pokerPlayers) > 3:
        # player in spot 3
        canvas.create_image(app.width/2 + 200, app.height/2 + 150,
            image=ImageTk.PhotoImage(app.pokerPlayerImages[3][0]))
        if app.pokerPlayerImages[3][1] == 0:
            canvas.create_text(app.width/2 + 300, app.height/2 + 150,
                text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[3][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[3])
        else:
            canvas.create_text(app.width/2 + 300, app.height/2 + 150,
                text = f'CPU {app.pokerPlayerImages[3][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[3][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[3])

    if len(app.pokerPlayers) > 4:
        # player in spot 4
        canvas.create_image(app.width/2 - 200, app.height/2 + 148,
            image=ImageTk.PhotoImage(app.pokerPlayerImages[4][0]))
        if app.pokerPlayerImages[4][1] == 0:
            canvas.create_text(app.width/2 - 300, app.height/2 + 148,
                text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[4][1]].playerMoney, 2)}', font = "Times 20 bold",
                fill = actionListColors[4])
        else:
            canvas.create_text(app.width/2 - 300, app.height/2 + 148,
                text = f'CPU {app.pokerPlayerImages[4][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[4][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[4])

    if len(app.pokerPlayers) > 5:
        # player in spot 5
        canvas.create_image(app.width/2 - 395, app.height/2 + 75,
            image=ImageTk.PhotoImage(app.pokerPlayerImages[5][0]))
        if app.pokerPlayerImages[5][1] == 0:
            canvas.create_text(app.width/2 - 495, app.height/2 + 75,
                text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[5][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[5])
        else:
            canvas.create_text(app.width/2 - 495, app.height/2 + 75,
                text = f'CPU {app.pokerPlayerImages[5][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[5][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[5])

    if len(app.pokerPlayers) > 6:
        # player in spot 6
        canvas.create_image(app.width/2 - 395, app.height/2 - 130,
            image=ImageTk.PhotoImage(app.pokerPlayerImages[6][0]))
        if app.pokerPlayerImages[6][1] == 0:
            canvas.create_text(app.width/2 - 495, app.height/2 - 130,
                text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[5][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[6])
        else:
            canvas.create_text(app.width/2 - 495, app.height/2 - 130,
                text = f'CPU {app.pokerPlayerImages[6][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[6][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[6])

    if len(app.pokerPlayers) > 7:
        # player in spot 7
        canvas.create_image(app.width/2 - 200, app.height/2 - 205,
            image=ImageTk.PhotoImage(app.pokerPlayerImages[7][0]))
        if app.pokerPlayerImages[7][1] == 0:
            canvas.create_text(app.width/2 - 300, app.height/2 - 205,
                text = f'{app.username} - ${round(app.pokerPlayers[app.pokerPlayerImages[7][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[7])
        else:
            canvas.create_text(app.width/2 - 300, app.height/2 - 205,
                text = f'CPU {app.pokerPlayerImages[7][1]} - ${round(app.pokerPlayers[app.pokerPlayerImages[7][1]].playerMoney, 2)}',
                font = "Times 20 bold", fill = actionListColors[7])

# key pressed for dealing the cards at the start of poker
def pokerDealKeyPressed(app):

    # initializes the small and big blinds as bets
    app.pokerPlayers[app.pokerPlayerImages[app.smallBlindIndex][1]].playerMoney -= app.smallBlind
    app.pokerPlayers[app.pokerPlayerImages[app.smallBlindIndex][1]].playerBet += app.smallBlind
    if app.pokerPlayers[app.pokerPlayerImages[app.smallBlindIndex][1]].playerNum == 0:
        app.accountBalance -= app.smallBlind

    app.pokerPlayers[app.pokerPlayerImages[app.bigBlindIndex][1]].playerMoney -= app.bigBlind
    app.pokerPlayers[app.pokerPlayerImages[app.bigBlindIndex][1]].playerBet += app.bigBlind
    if app.pokerPlayers[app.pokerPlayerImages[app.bigBlindIndex][1]].playerNum == 0:
        app.accountBalance -= app.bigBlind

    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (app.accountBalance, app.username))
    conn.commit()
    conn.close()

    # deals cards
    dealCards(app, app.remainingDeck)
    app.pokerDeal = False
    app.pokerFlop = True
    
    # changes the index of the blinds
    if app.bigBlindIndex == len(app.pokerPlayers) - 1:
        app.pokerActionIndex = 0
    else:
        app.pokerActionIndex = app.bigBlindIndex + 1
    
    # displays current informational message for the start of poker
    if app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
        app.pokerCurrentMessage = f"Cards have been dealt, {app.username}'s turn"
    else:
        app.pokerCurrentMessage = f"Cards have been dealt, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"

    app.pokerPlayerOdds = omniscientPlayerOddsPreFlop(app)

# checks if the pre flop betting round is over
def pokerPreFlopCheckKeyPressed(app):

    # checks if the number of players left is equal to the number of checks
    if app.pokerNumOfChecks == app.pokerPlayersLeft:

        # changes the action index
        app.pokerActionIndex = app.smallBlindIndex
        while app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerIn == False:
            if app.pokerActionIndex == len(app.pokerPlayers) - 1:
                app.pokerActionIndex = 0
            else:
                app.pokerActionIndex += 1

        # resets poker buttons
        app.pokerBetClicked = False
        app.pokerFoldClicked = False
        app.pokerCallClicked = False
        app.donePreFlopBetting = True

        # resets betting variables and deals the flop
        app.pokerBetAmount = app.bigBlind
        app.pokerCallAmount = 0
        app.pokerNumOfChecks = 0
        dealFlop(app, app.remainingDeck)
        app.pokerPlayerOdds = omniscientPlayerOddsPreTurn(app)

        # allows for the flop to be shown
        app.pokerTurn = True
        app.dealtFlop = True
        app.pokerFlop = False

        # displays current informational message for the flop being dealt
        if app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
            app.pokerCurrentMessage = f"The flop has been dealt, {app.username}'s turn"
        else:
            app.pokerCurrentMessage = f"The flop has been dealt, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"

# checks if the pre turn betting round is over
def pokerPreTurnCheckKeyPressed(app):

    # checks if the number of players left is equal to the number of checks
    if app.pokerNumOfChecks == app.pokerPlayersLeft:

        # changes the action index
        app.pokerActionIndex = app.smallBlindIndex
        while app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerIn == False:
            if app.pokerActionIndex == len(app.pokerPlayers) - 1:
                app.pokerActionIndex = 0
            else:
                app.pokerActionIndex += 1

        # displays current informational message for the turn being dealt
        if app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum == 0:
            app.pokerCurrentMessage = f"The turn has been dealt, {app.username}'s turn"
        else:
            app.pokerCurrentMessage = f"The turn has been dealt, CPU {app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum}'s turn"
        
        # resets poker buttons
        app.pokerBetClicked = False
        app.pokerFoldClicked = False
        app.pokerCallClicked = False
        app.donePreTurnBetting = True

        # resets betting variables and deals the turn
        app.pokerBetAmount = app.bigBlind
        app.pokerCallAmount = 0
        app.pokerNumOfChecks = 0
        dealTurn(app, app.remainingDeck)
        app.pokerPlayerOdds = omniscientPlayerOddsPreRiver(app)

        # allows for the turn to be shown
        app.pokerTurn = False
        app.dealtTurn = True
        app.pokerRiver = True

# checks if the pre river betting round is over
def pokerPreRiverCheckKeyPressed(app):

    # checks if the number of players left is equal to the number of checks
    if app.pokerNumOfChecks == app.pokerPlayersLeft:

        # changes the action index
        app.pokerActionIndex = app.smallBlindIndex
        while app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerIn == False:
            if app.pokerActionIndex == len(app.pokerPlayers) - 1:
                app.pokerActionIndex = 0
            else:
                app.pokerActionIndex += 1

        # resets poker buttons
        app.pokerBetClicked = False
        app.pokerFoldClicked = False
        app.pokerCallClicked = False
        app.donePostTurnBetting = True

        # resets betting variables and deals the river
        app.pokerBetAmount = app.bigBlind
        app.pokerCallAmount = 0
        app.pokerNumOfChecks = 0
        dealRiver(app, app.remainingDeck)
        app.pokerPlayerOdds = omniscientPlayerOddsPostRiver(app)

        # allows for the river to be shown
        app.pokerRiver = False
        app.dealtRiver = True
        app.endPokerBetting = True

        # displays current informational message for the river being dealt
        if app.pokerPlayerImages[app.pokerActionIndex][1] == 0:
            app.pokerCurrentMessage = f"The river has been dealt, {app.username}'s turn"
        else:
            app.pokerCurrentMessage = f"The river has been dealt, CPU {app.pokerPlayerImages[app.pokerActionIndex][1]}'s turn"

# checks if the post river betting round is over
def pokerEndBettingCheckKeyPressed(app):

    # checks if the number of players left is equal to the number of checks
    if app.pokerNumOfChecks == app.pokerPlayersLeft:
        
        # calculate ML
        calculateUserBetDifference(app)

        # allows for a new hand of poker to be played
        app.endPokerBetting = False
        app.newPokerRound = True
        app.endOfHand = True

        # initializes winning hand/score varialbes
        bestHandScore = 0
        winnerList = []
        winnerHandList = []

        # loops thorugh all of the players
        for i in range(len(app.pokerPlayers)):
            # makes sure that the player has not folded
            if app.pokerPlayers[app.pokerPlayerImages[i][1]].playerIn == True:
                # checks to see if the player's hand is the best hand yet
                if chooseBestHand(app.pokerPlayers[app.pokerPlayerImages[i][1]].playerHand, app.pokerBoard)[1] > bestHandScore:
                    bestHandScore = chooseBestHand(app.pokerPlayers[app.pokerPlayerImages[i][1]].playerHand, app.pokerBoard)[1]
                    winnerHandList = [chooseBestHand(app.pokerPlayers[app.pokerPlayerImages[i][1]].playerHand, app.pokerBoard)[0]]
                    winnerList = [app.pokerPlayers[app.pokerPlayerImages[i][1]].playerNum]
                
                # checks to see if the player's hand is the same as the best hand yet
                elif chooseBestHand(app.pokerPlayers[app.pokerPlayerImages[i][1]].playerHand, app.pokerBoard)[1] == bestHandScore:
                    winnerList.append(app.pokerPlayers[app.pokerPlayerImages[i][1]].playerNum)
                    winnerHandList.append(chooseBestHand(app.pokerPlayers[app.pokerPlayerImages[i][1]].playerHand, app.pokerBoard)[0])

        # gives the money in the pot to the winning player(s)
        for i in winnerList:
            app.pokerPlayers[i].playerMoney += round(app.pokerPotSize/(len(winnerList)), 2)
            if i == 0:
                app.accountBalance += round(app.pokerPotSize/(len(winnerList)), 2)

        # displays message if there is one winner
        if len(winnerList) == 1:
            if winnerList[0] == 0:
                app.pokerCurrentMessage = f"{app.username} wins the hand with a {calculateHandScore(winnerHandList[0])[1]}"
            else:
                app.pokerCurrentMessage = f"CPU {app.pokerPlayers[i].playerNum} wins the hand with a {calculateHandScore(winnerHandList[0])[1]}"
        
        # displays message if there are multiple winners
        else:
            if 0 not in winnerList:
                winningMessage = "CPUs "
                for i in winnerList:
                    winningMessage += f"{app.pokerPlayers[i].playerNum}, "
                winningMessage = winningMessage[0:-2]
                app.pokerCurrentMessage = f"{winningMessage} win the hand"
            else:
                winningMessage = f"{app.username} and CPUs "
                for i in winnerList:
                    if i != 0:
                        winningMessage += f"{app.pokerPlayers[i].playerNum}, "
                winningMessage = winningMessage[0:-2]
                app.pokerCurrentMessage = f"{winningMessage} win the hand"

        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (app.accountBalance, app.username))
        conn.commit()
        conn.close()

    # checks if everyone folds
    elif (app.pokerPlayersLeft == 1) and (app.newPokerRound == False):

            # changes the action index
            previousActionIndex = app.pokerActionIndex
            app.pokerActionIndex = app.smallBlindIndex

            # allows for a new hand to be played
            app.newPokerRound = True
            app.endOfHand = True
            app.endPokerBetting = False

            # finds the winner of the hand
            winner = -1
            for i in range(len(app.pokerPlayers)):
                if app.pokerPlayers[app.pokerPlayerImages[i][1]].playerIn == True:
                    winner = i
            
            # gives the money in the pot to the winner
            app.pokerPlayers[app.pokerPlayerImages[winner][1]].playerMoney += app.pokerPotSize
            if app.pokerPlayers[app.pokerPlayerImages[winner][1]].playerNum == 0:
                app.accountBalance += round(app.pokerPotSize, 2)

            # displays the winning message
            if app.pokerPlayerImages[previousActionIndex][1] == 0:
                app.pokerCurrentMessage = f"{app.username} folds, CPU {app.pokerPlayerImages[winner][1]} wins the hand"
            elif app.pokerPlayerImages[winner][1] == 0:
                app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} folds, {app.username} wins the hand"
            else:
                app.pokerCurrentMessage = f"CPU {app.pokerPlayerImages[previousActionIndex][1]} folds, CPU {app.pokerPlayerImages[winner][1]} wins the hand"
            
            conn = sqlite3.connect("user.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET account_balance = (?) WHERE username = (?)", (app.accountBalance, app.username))
            conn.commit()
            conn.close()

# resets poker variables for a new round
def pokerNewRoundKeyPressed(app):

    # poker state variable
    app.pokerDeal = True
    app.pokerFlop = False
    app.dealtFlop = False
    app.pokerTurn = False
    app.dealtTurn = False
    app.pokerRiver = False
    app.dealtRiver = False
    app.newPokerRound = False
    app.endOfHand = False
    app.endHandEarly = False

    # resets betting variables
    app.pokerBetAmount = app.bigBlind
    app.pokerCallAmount = app.bigBlind
    app.pokerHighestBet = app.bigBlind

    app.pokerActionIndex = -1

    # resets round betting variables
    app.donePreFlopBetting = False
    app.donePreTurnBetting = False
    app.donePreRiverBetting = False
    app.donePostRiverBetting = False
    app.endPokerBetting = False

    # resets button variables
    app.pokerCallClicked = False
    app.pokerBetClicked = False
    app.pokerFoldClicked = False
    app.pokerPlayersLeft = len(app.pokerPlayers)
    app.pokerPotSize = app.smallBlind + app.bigBlind
    app.pokerNumOfChecks = 0

    # resets board and current message
    app.pokerBoard = []
    app.pokerCurrentMessage = "Press 'right' for cards to be dealt"

    # changes the blind indexes
    changeBlinds(app)

    # resets the card deck and player class variables
    app.remainingDeck = cardDeck()
    for i in range(len(app.pokerPlayers)):
        app.pokerPlayers[i].playerHand = []
        app.pokerPlayers[i].playerBet = 0
        app.pokerPlayers[i].playerIn = True

# carries out the poker AI actions
def pokerAIAction(app):

    # initializes bet, call, hand variables for the AI to take in
    betSize = round(app.pokerHighestBet / app.pokerBuyIn, 2)
    callSize = round((app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet)/app.pokerBuyIn, 2)
    hand = app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerHand

    # if the AI is aggressive/Bodi
    if app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerType == "Bodi":
        if (app.pokerFlop):
            action = preFlopBodiAI(app, hand, app.pokerPlayersLeft - 1, betSize)[0]
        elif (app.pokerTurn):
            action = preTurnBodiAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.pokerRiver):
            action = preRiverBodiAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.endPokerBetting):
            action = postRiverBodiAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]

    # if the AI is conservative/Ganger
    elif app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerType == "Ganger":
        if (app.pokerFlop):
            action = preFlopGangerAI(app, hand, app.pokerPlayersLeft - 1, betSize)[0]
        elif (app.pokerTurn):
            action = preTurnGangerAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.pokerRiver):
            action = preRiverGangerAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.endPokerBetting):
            action = postRiverGangerAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]

    # if the AI is balanced/Wernink
    elif app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerType == "Wernink":
        if (app.pokerFlop):
            action = preFlopWerninkAI(app, hand, app.pokerPlayersLeft - 1, betSize)[0]
        elif (app.pokerTurn):
            action = preTurnWerninkAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.pokerRiver):
            action = preRiverWerninkAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.endPokerBetting):
            action = postRiverWerninkAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]

    # if the AI is super aggressive/Imran
    elif app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerType == "Imran":
        if (app.pokerFlop):
            action = preFlopImranAI(app, hand, app.pokerPlayersLeft - 1, betSize)[0]
        elif (app.pokerTurn):
            action = preTurnImranAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.pokerRiver):
            action = preRiverImranAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.endPokerBetting):
            action = postRiverImranAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]

    # if the AI is super conservative/Sep
    elif app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerType == "Sep":
        if (app.pokerFlop):
            action = preFlopSepAI(app, hand, app.pokerPlayersLeft - 1, betSize)[0]
        elif (app.pokerTurn):
            action = preTurnSepAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.pokerRiver):
            action = preRiverSepAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]
        elif (app.endPokerBetting):
            action = postRiverSepAI(app, hand, app.pokerBoard, app.pokerPlayersLeft - 1, callSize)[0]


    # if the action is a bet
    if len(action) == 2:
        previousActionIndex = app.pokerActionIndex
        app.pokerBetAmount = round(float(app.pokerBuyIn * float(action[1])), 2)
        betKeyPressed(app)
        changeActionIndex(app)
        betMessage(app, previousActionIndex)

    # if the action is a call
    elif action == "Call":
        previousActionIndex = app.pokerActionIndex
        callKeyPressed(app)
        changeActionIndex(app)
        callMessage(app, previousActionIndex)

    # if the action is a fold
    elif action == "Fold":

        # check to see if the player can check
        if app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet == 0:
            previousActionIndex = app.pokerActionIndex
            callKeyPressed(app)
            changeActionIndex(app)
            callMessage(app, previousActionIndex)
        else:
            previousActionIndex = app.pokerActionIndex
            foldKeyPressed(app)
            changeActionIndex(app)
            foldMessage(app, previousActionIndex)


def pokerMode_appStarted(app):

    # initiates the poker players
    createPokerPlayers(app, app.pokerNumOpponents, app.pokerLevel, app.pokerBuyIn)

    # initiate variable to track if the dealer should deal the players cards
    app.pokerDeal = True
    app.pokerFlop = False
    app.dealtFlop = False
    app.pokerTurn = False
    app.dealtTurn = False
    app.pokerRiver = False
    app.dealtRiver = False
    app.newPokerRound = False

    # initiates the blinds and bet amounts
    app.smallBlindIndex = 0
    app.smallBlind = app.pokerBuyIn/200
    app.bigBlindIndex = 1
    app.bigBlind = app.pokerBuyIn/100
    app.pokerBetAmount = app.bigBlind
    app.pokerCallAmount = app.bigBlind
    app.pokerHighestBet = app.bigBlind
    app.betDecimal = False
    app.numBetDecimals = 0

    app.pokerActionIndex = -1

    # initalize betting variables
    app.pokerCheat = False
    app.donePreFlopBetting = False
    app.donePreTurnBetting = False
    app.donePreRiverBetting = False
    app.donePostRiverBetting = False
    app.endPokerBetting = False
    app.endOfHand = False
    app.endHandEarly = False

    # initiate poker buttons
    app.pokerCallClicked = False
    app.pokerBetClicked = False
    app.pokerFoldClicked = False
    app.pokerPlayersLeft = len(app.pokerPlayers)
    app.pokerPotSize = app.smallBlind + app.bigBlind
    app.pokerNumOfChecks = 0
    app.pokerCurrentMessage = "Press 'right' for cards to be dealt"

    # list of the cards on the poker table
    app.pokerBoard = []

    app.pokerPlayerOdds = {}

    # create a deck of cards
    app.remainingDeck = cardDeck()

    app.timerDelay = 2000

def pokerMode_timerFired(app):

    # checks to see if it is time for the AI to do its magic
    if (app.pokerDeal == False) and (not app.endOfHand) and (app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum != 0):
        
        # for pre flop betting
        if (app.pokerFlop) and (not app.donePreFlopBetting):

            pokerAIAction(app)
            
            if app.endHandEarly == False:
                pokerPreFlopCheckKeyPressed(app)
            else:
                pokerNewRoundKeyPressed(app)

        # for pre turn betting
        elif (app.pokerTurn) and (not app.donePreTurnBetting):

            pokerAIAction(app)
            
            if app.endHandEarly == False:
                pokerPreTurnCheckKeyPressed(app)
            else:
                pokerNewRoundKeyPressed(app)

        # for pre river betting
        elif (app.pokerRiver) and (not app.donePreRiverBetting):

            pokerAIAction(app)
            
            if app.endHandEarly == False:
                pokerPreRiverCheckKeyPressed(app)
            else:
                pokerNewRoundKeyPressed(app)

        # for post river betting
        elif (app.endPokerBetting):

            pokerAIAction(app)
            
            if app.endHandEarly == False:
                pokerEndBettingCheckKeyPressed(app)
            else:
                pokerNewRoundKeyPressed(app)

    if (app.endOfHand):
        for i in range(len(app.pokerPlayers)):
            if (app.pokerPlayers[i].playerMoney <= 0) and (app.pokerPlayers[i] != app.myPokerPlayer):
                app.pokerPlayers[i].playerMoney = app.pokerBuyIn
            elif (app.pokerPlayers[i].playerMoney <= 0) and (app.pokerPlayers[i] == app.myPokerPlayer):
                app.mode = "pokerOptionMode"

def pokerMode_mousePressed(app, event):

    # checks if you click back
    if (25 <= event.x <= 75) and (35 <= event.y <= 65):
        app.mode = "pokerOptionMode"

    # checks if you click help
    elif (app.width - 90 <= event.x <= app.width - 30) and (35 <= event.y <= 65):
        app.mode = "pokerHelpMode"

    # checks if you are interacting with the betting interface
    if (app.pokerDeal == False) and (not app.endOfHand) and (app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerNum == 0):

            app.pokerBetAmount = round(float(app.bigBlind + app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet), 2)
            
            # betting button clicked
            if (app.width/2 - 160 <= event.x <= app.width/2 - 80) and (app.height/2 - 50 <= event.y <= app.height/2):
                app.pokerBetClicked = not app.pokerBetClicked
                app.pokerCallClicked = False
                app.pokerFoldClicked = False
                # resets the bet amount
                if app.pokerBetClicked == False:
                    app.pokerBetAmount = round(app.bigBlind + app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)

            # call button clicked
            elif (app.width/2 - 70 <= event.x <= app.width/2 + 70) and (app.height/2 - 50 <= event.y <= app.height/2):
                app.pokerCallClicked = not app.pokerCallClicked

                app.pokerCallAmount = round(app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)
                app.pokerFoldClicked = False
                app.pokerBetClicked = False
                app.pokerBetAmount = round(app.bigBlind + app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)

            # fold button clicked
            elif (app.width/2 + 80 <= event.x <= app.width/2 + 160) and (app.height/2 - 50 <= event.y <= app.height/2):
                app.pokerFoldClicked = not app.pokerFoldClicked
                app.pokerCallClicked = False
                app.pokerBetClicked = False
                app.pokerBetAmount = round(app.bigBlind + app.pokerHighestBet - app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerBet, 2)

            # resets variables if anywhere else is clicked
            else:
                app.pokerBetClicked = False
                app.pokerFoldClicked = False
                app.pokerCallClicked = False
                app.pokerBetAmount = round(app.bigBlind + app.pokerCallAmount, 2)

def pokerMode_keyPressed(app, event):

    # toggle for the information/cheat section
    if event.key == "Space":
        app.pokerCheat = not app.pokerCheat

    # checks if the dealer needs to deal the cards
    if app.pokerDeal:
        # checks if user clicks right to deal the cards
        if event.key == "Right":
            pokerDealKeyPressed(app)
    
    # key pressed for pre-flop when betting round has not finished
    elif (app.pokerFlop) and (not app.donePreFlopBetting):
        # checks if "right" has been clicked and the player is betting greater than or equal to the big blind
        if event.key == "Right" and app.pokerBetClicked and app.pokerBetAmount >= app.bigBlind + app.pokerCallAmount:
            pokerBetKeyPressed(app)

        # checks if "right" was clicked and the player wants to fold
        elif event.key == "Right" and app.pokerFoldClicked:
            pokerFoldKeyPressed(app)

        # checks if "right" is clicked and the player wants to call
        elif event.key == "Right" and app.pokerCallClicked:
            pokerCallKeyPressed(app)

        # checks if the flop needs to be dealt
        if app.endHandEarly == False:
            pokerPreFlopCheckKeyPressed(app)
        else:
            if event.key == "Right":
                pokerNewRoundKeyPressed(app)

    # key pressed for pre-turn when betting round has not finished
    elif (app.pokerTurn) and (not app.donePreTurnBetting):
        # checks if "right" has been clicked and the player is betting greater than or equal to the big blind amount
        if event.key == "Right" and app.pokerBetClicked and app.pokerBetAmount >= app.pokerCallAmount + app.bigBlind:
            pokerBetKeyPressed(app)

        # checks if "right" is clicked and the player wants to call
        elif event.key == "Right" and app.pokerCallClicked:
            pokerCallKeyPressed(app)

        # checks if "right" is clicked and the player wants to fold
        elif event.key == "Right" and app.pokerFoldClicked:
            pokerFoldKeyPressed(app)

        # checks if the turn needs to be dealt
        if app.endHandEarly == False:
            pokerPreTurnCheckKeyPressed(app)
        else:
            if event.key == "Right":
                pokerNewRoundKeyPressed(app)

    # key pressed for pre-river when betting round has not finished
    elif (app.pokerRiver) and (not app.donePreRiverBetting):
        # checks if "right" has been clicked and the player is betting greater than or equal to the big blind amount
        if event.key == "Right" and app.pokerBetClicked and app.pokerBetAmount >= app.pokerCallAmount + app.bigBlind:
            pokerBetKeyPressed(app)

        # checks if "right" is clicked and the player wants to call
        elif event.key == "Right" and app.pokerCallClicked:
            pokerCallKeyPressed(app)

        # checks if "right" is clicked and the player wants to fold
        elif event.key == "Right" and app.pokerFoldClicked:
            pokerFoldKeyPressed(app)

        # checks if the river needs to be dealt
        if app.endHandEarly == False:
            pokerPreRiverCheckKeyPressed(app)
        else:
            if event.key == "Right":
                pokerNewRoundKeyPressed(app)

    # key pressed for post-river when betting round has not finished
    elif app.endPokerBetting:
        # checks if "right" is clicked and the player wants to bet an amount greater than or equal to the big blind
        if event.key == "Right" and app.pokerBetClicked and app.pokerBetAmount >= app.pokerCallAmount + app.bigBlind:
            pokerBetKeyPressed(app)

        # checks if "right" is clicked and the player wants to call
        elif event.key == "Right" and app.pokerCallClicked:
            pokerCallKeyPressed(app)

        # checks if "right" is clicked and the player wants to fold
        elif event.key == "Right" and app.pokerFoldClicked:
            pokerFoldKeyPressed(app)

        # checks if the hand is over
        pokerEndBettingCheckKeyPressed(app)

    # checks if a new poker round is ready
    elif (app.newPokerRound) and (app.endPokerBetting == False):
        if event.key == "Right":
            pokerNewRoundKeyPressed(app)

    # checks if a bet is being placed
    if app.pokerBetClicked:
        
        if event.key.isdigit() and app.betDecimal == False:
            if app.pokerBetAmount*10 + int(event.key) <= app.pokerPlayers[app.pokerPlayerImages[app.pokerActionIndex][1]].playerMoney:
                app.pokerBetAmount = app.pokerBetAmount*10 + int(event.key)

        elif event.key.isdigit() and app.numBetDecimals < 2 and app.betDecimal:
            if app.numBetDecimals == 0:
                app.pokerBetAmount = float(str(app.pokerBetAmount)[:-1] + str(event.key))
            else:
                app.pokerBetAmount = float(str(app.pokerBetAmount) + str(event.key))

            app.numBetDecimals += 1

        elif event.key == "." and app.betDecimal == False:
            app.betDecimal = True
            app.pokerBetAmount = str(app.pokerBetAmount)

        elif event.key == "Delete":
            if app.betDecimal == False:
                app.pokerBetAmount //= 10
            else:
                if app.numBetDecimals > 0:
                    app.pokerBetAmount = float(str(app.pokerBetAmount)[:-1])
                    app.numBetDecimals -= 1
                else:
                    app.pokerBetAmount = int(str(app.pokerBetAmount)[:-2])
                    app.betDecimal = False

def pokerMode_redrawAll(app, canvas):
    # draw the poker page
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan2")

    generatePokerTable(app, canvas)

    drawSmallBlind(app, canvas)
    drawBigBlind(app, canvas)

    if app.pokerCheat:
        drawPokerCheatSection(app, canvas)
    else:
        drawPokerInformationSection(app, canvas)

    drawPokerTableCards(app, canvas)
    
    drawPlayersAroundBoard(app, canvas)

    drawPokerButtons(app, canvas)

    drawPokerBuyInBlinds(app, canvas)

    drawPlayerBets(app, canvas)


########################
# Poker Help Mode
########################

def pokerHelpMode_mousePressed(app, event):
    # checks if you click back
    if (25 <= event.x <= 75) and (35 <= event.y <= 65):
        app.mode = "pokerMode"

    # checks if you click log out
    elif (app.width - 90 <= event.x <= app.width - 30) and (35 <= event.y <= 65):
       app.mode = "welcomeMode"
       welcomeMode_appStarted(app)

def pokerHelpMode_redrawAll(app, canvas):
    # creates the poker help page

    canvas.create_rectangle(0, 0, app.width, app.height, fill = "cyan2")

    canvas.create_text(app.width/2, 60, text = "Texas Hold'em Instructions",
                font = "Times 30")

    # texas hold'em instructions from https://www.instructables.com/Learn-To-Play-Poker---Texas-Hold-Em-aka-Texas-Ho/#:~:text=Step%201%3A%20Let's%20Begin&text=Each%20player%20is%20dealt%20two,by%20a%20third%20betting%20round.
    instructions = ["Game Play", "1) Press 'right' and each player will be dealt two cards (their hand)",
        "2) A round of betting will take place - you can bet, call, or fold by interacting with the betting interface",
        "3) AIs will make their own decisions to bet and will take a couple of seconds to do so",
        "4) After the round of betting is over, if just one person is left, they win, else the flop will be dealt consisting of three community cards",
        "5) A second round of betting will take place in the same fashion as before",
        "6) After this round of betting is over, if just one person is left, they win, else the turn will be dealt consisting of one more community card",
        "7) A third round of betting will take place in the same fashion as before",
        "8) After this round of betting is over, if just one person is left, they win, else the river will be dealt consisting of one last community card",
        "9) A final round of betting will take place in the same fashion as before",
        "10) The winner is determined based on who has the best hand give their hand and the five community cards",
        "11) The winner will receive the money in the pot, and the next round of poker is ready!",
        "Hand Scores",
        "1) Royal Flush - A, K, Q, J, 10 of the same suit",
        "2) Straight Flush - Five cards with a continuous sequence of ranks and the same suit",
        "3) Four of a Kind - Four cards of the same rank",
        "4) Full House - Three cards of the same rank and two other cards of the same rank",
        "5) Flush - Five Cards of the same suit",
        "6) Straight - Five Cards with a continuous sequence of ranks",
        "7) Three of a Kind - Three cards of the same rank",
        "8) Two Pair - Two cards of the same rank and two other cards of the same rank",
        "9) One Pair - Two cards of the same rank",
        "10) High Card - Card of the highest rank"]
    
    for i in range(len(instructions)):
        if instructions[i] == "Hand Scores" or instructions[i] == "Game Play":
            bold = " bold"
        else:
            bold = ""
        canvas.create_text(app.width/2, 100 + i*30, text = instructions[i],
                font = f"Times 15{bold}")

    # back and log out text
    canvas.create_text(50, 50, text = "Back", font = "Times 15")
    canvas.create_text(app.width - 60, 50, text = "Log Out", font = "Times 15")


########################
# Main App
########################

def appStarted(app):

    # initiate welcome mode and its variables
    app.mode = "welcomeMode"
    welcomeMode_appStarted(app)

    # load the images
    loadImages(app)

    app.pokerNumOpponents = 7
    app.pokerLevel = "Hard"
    app.pokerBuyIn = 1000

runApp(width=1200, height=800)