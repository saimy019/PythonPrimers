examineForEvenOrOddNumber = int(input('Enter the number to check if it is even or odd positive integer '))
if examineForEvenOrOddNumber <= 0:
    print ('Enter a positive integer which is greater than zero ')
elif examineForEvenOrOddNumber % 2 == 0:
    print ('The entered number is an even number!')
else:
    print('The entered number is odd!')
