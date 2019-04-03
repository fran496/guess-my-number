gameOn = False
userName = str(raw_input("Hello! Whats your name? "))
print("Welcome " + userName + "!, write start when you're ready to play!")

while gameOn == False:
    startGame = str(raw_input("Ready? "))
    if startGame == "start":
        print("Let's play!")
        gameOn = True

# game()