 # -*- coding: utf-8 -*-
from random import *

def intro ():
    gameStatus = False
    playerName = str(raw_input("Hello! What's your name? "))
    print("Welcome " + playerName + "!, write start when you're ready to play!")
    while gameStatus == False:
		    startGame = str(raw_input("Ready? "))
		    if startGame == "start":
		        print("Let's play!")
		        gameStatus = True
		        game(gameStatus, playerName)

def game(gameStatus, playerName):
    randomNumber = randint(1, 100) 
    maxTries = 10
    numberOfTries = 0
    numberOfWins = 0
    print("I'm going to choose an integer between 1 and 100, try to guess it!")
    while gameStatus == True and numberOfTries < maxTries:
        numberOfTries += 1
        playerInput = input()
        if testPlayerInput(playerInput, playerName, randomNumber):
            print("You won in " + str(numberOfTries) + " tries!")
            print("Do you want to keep playing?")
            keepPlaying = str(raw_input("yes or no? "))
            if keepPlaying == "yes":
                numberOfWins += 1
                gameStatus = True
                game(gameStatus, playerName)
            elif keepPlaying == "no":
                return
    print("OUT OF TRIES, YOU LOSE " + playerName + "!")
    print("Do you want to play again?")
    playAgain = str(raw_input("yes or no? "))
    if playAgain == "yes":
        gameStatus = True
        game(gameStatus, playerName)
    elif playAgain == "no":
        return
        


def testPlayerInput(playerInput, playerName, randomNumber):
    if playerInput == randomNumber:
        print("YOU WIN " + playerName + "!")
        return True
    elif playerInput < randomNumber:
        print("THAT'S NOT IT! Guess higher!")
        return False
    elif playerInput > randomNumber:
        print("THAT'S NOT IT! Guess lower!")
        return False

intro()