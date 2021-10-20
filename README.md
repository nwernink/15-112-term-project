# 15-122-term-project

bet112 by Nicholas Wernink

bet112 is a poker app where you can login/create an account to play and choose how many opponents you want to play against, the difficulty of the AI, and the buy in amount. All user information is saved globally even when exiting the app including usernames, passwords, account balances, and the machine learning aspect for the AIs to use which determines how aggressive or conservative you are as a player.

To run the project, make sure you have cmu_112_graphics and sqlite3 imported and run bet112.py. Upon opening the app, you will be able to login or create an account. To do so click on the username and type in your username and do the same for the password. Then click login or create an account. Upon opening the app a print statement in the terminal will show you all of the users information for reference in case you forget your username or password or otherwise cannot enter the game. Once you are in the main "casino" page, you can click help to see instructions about how the app works, logout, or click the image of the poker cards to start playing poker. You will then enter the poker option page where you can select the number of opponents you want to play against, the AIs difficulty, and the buy in amount. The default is playing against 7 players with a difficulty of hard and a buy in of $1000. When you click play, you are taken to the poker page where you can read the instructions by clicking help or press back to go back to the options page. Press the "right" arrow key for the cards to be dealt and you can see your cards in the bottom left hand corner. The current message will be displayed in the information section next to your cards that says the last action taken and who is next up. Also, the player whose turn it is will turn to red text and then switch back to black text once they make their action. When it is your turn, the betting interface will pop up where you can bet, check/call, or fold. To fold, click fold and then press the "right" arrow key. To check/call, click check/call and then press the "right" arrow key. To bet, click bet and then type in the desired amount you would like to bet which must be greater than the big blind plus the highest bet on the table. Once you are satisfied, press the "right" arrow key to submit the bet. After the round of betting is complete, the flop will be dealt, and another round of betting will occur. Once that ends, the turn will be dealt, and once again there is another round of betting. Finally, the river will be dealt followed by one final round of betting. Once that is over, the winner of the hand will receive the money in the pot and the winning message will be displayed. To go to the next hand press the "right" arrow key which resets the table and moves onto the next hand, and repeat. You can also see the opponent's hands and everyone's odds by pressing the space bar (but that's cheating!). The odds are updated in real-time and represent a Monte-Carlo simulation that takes into account all of the information available including all players' hands as well as the board. If you return to the main "casino" page by clicking back twice, you can see that your account balance has changed based on how you did.