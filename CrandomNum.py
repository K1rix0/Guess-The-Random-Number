#Program about generating number

from random import randrange as ran
#To generate the number

print("~~~~~~~~~~~~~ Guess The Number ~~~~~~~~~~~~~")

while True:
    print("You have 8 tries...\n")

    def highLowOr(x):
        if x == randomNum:
            print("Congratulations!!")
            return True    
        elif x < randomNum:
            print("Higher")
            return False
        else:
            print("Lower")
            return False

    randomNum = ran(0, 101)
    for x in range(8):
        while True:
            try:
                guessNum = int(input("Try and guess the number: "))
            except:
                print("An error occured, try again. ")
            else:
                break

        WinOrTry = highLowOr(guessNum)

        if WinOrTry == True:
            break

    print("The game is finished, the number was " + str(randomNum))

    while True:
        global anotherGame
        anotherGame = input("\nDo you want another game (y/n): ")
        if anotherGame == "n" or anotherGame == "N" or anotherGame == "y" or anotherGame == "Y":
            break
        else:
            print("An error occured, try again.")
    
    if anotherGame == "n" or anotherGame == "N":
        print("Thanks for playing...")
        break
    else:
        print("Game reloading...\n")

print("\nDone")
