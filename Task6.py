import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print (die1, die2)

if die1 == die2:
    print("You rolled a pair of " + str(die1) + "s")
else:
    print("You have rolled a " + str(die1) + " and a " + str(die2))
