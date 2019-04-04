from random import *

playerName = 0
randomNumber = 0
status = 0

def intro ():
    status = False
    playerName = str(raw_input("Hello! What's your name? "))
    print("Welcome " + playerName + "!, write start when you're ready to play!")
    while status == False:
		    startGame = str(raw_input("Ready? "))
		    if startGame == "start":
		        print("Let's play!")
		        status = True
		        game(status, playerName)

def game(status, playerName):
    print("I'm going to choose an integer between 1 and 100, try to guess it!")
    randomNumber = randint(1, 100) 
    while status == True:
        print("NEW GAME")
        playerInput = input()
        testPlayerInput(playerInput, playerName, randomNumber)


def testPlayerInput(playerInput, playerName, randomNumber):
    if playerInput == randomNumber:
        print("YOU WIN " + playerName + "!")
        return
    elif playerInput < randomNumber:
        print("THAT'S NOT IT! Guess higher!")
        return
    elif playerInput > randomNumber:
        print("THAT'S NOT IT! Guess lower!")
        return

intro()