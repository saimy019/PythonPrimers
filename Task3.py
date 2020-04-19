enterTime = float(input('Enter the time in second to determine the stage of the flight '))
#enterTime = float(enterTime)
if (enterTime >= 0 and enterTime < 100):
    print ('The flight is in Stage 1!')
elif (enterTime >= 100 and enterTime < 170):
    print ('The flight is in Stage 2!')
elif (enterTime >= 170 and enterTime >= 260):
    print ('The flight is in Stage 3!')
else:
    print ("The flight is un-powered, please start the flight!")
