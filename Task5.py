import random

number = random.randint(1, 10)
userNumber = int(input("Please enter the choice of your number in between 1 to 10 "))
if userNumber == number:
    print("Well done - you guessed it!")
else:
    print("Too bad - better luck next time!")

print ("Do you want to play again? ")
