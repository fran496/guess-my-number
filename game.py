from random import *

gameOn = False
randomNumber = 0


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

def game ():
    print("I'm going to choose a natural number between 1 and 100, if you guess it right you win! ")
    randomNumber = randint(1, 100)
    
    while gameOn == True:
        playerInput = input()
        testPlayerInput(playerInput)

def intro ():
    playerName = str(raw_input("Hello! What's your name? "))
    print("Welcome " + playerName + "!, write start when you're ready to play!")
    while gameOn == False:
        startGame = str(raw_input("Ready? "))
        if startGame == "start":
            print("Let's play!")
            gameOn = True
            game()

intro()