from random import *

randomNumber = 0
gameOn = 0

def intro ():
    gameOn = False
    playerName = str(raw_input("Hello! What's your name? "))
    print("Welcome " + playerName + "!, write start when you're ready to play!")
    while gameOn == False:
        startGame = str(raw_input("Ready? "))
        if startGame == "start":
            print("Let's play!")
            gameOn = True
            game(gameOn)

def game(status):
    print("I'm going to choose an integer between 1 and 100, try to guess it!")
    randomNumber = randint(1, 100) 
    while status == True:
        print("Player inputt")
        playerInput = input()
        testPlayerInput(playerInput)

def testPlayerInput(playerInput):
    if playerInput == randomNumber:
        print("YOU WIN " + playerName + "!")
        gameOn = False
        return gameOn
    elif playerInput < randomNumber:
        print("THAT'S NOT IT! Guess higher!")
        return
    elif playerInput > randomNumber:
        print("THAT'S NOT IT! Guess lower!")
        return

intro()
game(gameOn)