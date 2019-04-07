 # -*- coding: utf-8 -*-
from random import *

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
    numberOfTries = 0
    randomNumber = randint(1, 100) 
    print("I'm going to choose an integer between 1 and 100, try to guess it!")
    while status == True:
        numberOfTries += 1
        playerInput = input()
        if testPlayerInput(playerInput, playerName, randomNumber) == True:
            print("You won in " + str(numberOfTries) + " tries!")
            status = False
            #print("Do you want to keep playing?")
            #keepPlaying = str(raw_input("yes or no? "))
            #if keepPlaying == "yes":
            #    status = True
            #elif keepPlaying == "no":
            #    status = False


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