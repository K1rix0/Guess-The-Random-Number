#Program about generating number

from random import randrange as ran
#To generate the number

print("~~~~~~~~~~~~~ Guess The Number ~~~~~~~~~~~~~")

while True:
    print("You have 7 tries...\n")

    def highLowOr(x):
        if x == randomNum:
            print("Congratualtions!!")
            return True    
        elif x < randomNum:
            print("Higher")
            return False
        else:
            print("Lower")
            return False

    randomNum = ran(0, 101)
    for x in range(7):
        while True:
            try:
                guessNum = int(input("Try and guess the number: "))
                break
            except:
                print("Print the numebr again, there was an error: ")

        WinOrTry = highLowOr(guessNum)

        if WinOrTry == True:
            break

    print("The game is finished, the number was " + str(randomNum))

    while True:
        global anotherGame
        anotherGame = input("\nDo you want another game (y/n): ")
        if anotherGame == "n" and anotherGame == "N" and anotherGame == "y" and anotherGame == "Y":
            print("Error, try again.")
        else:
            break
    
    if anotherGame == "n" and anotherGame == "N":
        print("Thanks for playing...")
        break
    else:
        pass

print("\nDone")
