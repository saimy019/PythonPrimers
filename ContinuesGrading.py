askIfTheyWantToContinue = True
while (askIfTheyWantToContinue == True):
    studentName = str(input("Student: "))
    mark = int(input("Mark: "))
    if (mark >= 85):
        print(studentName + " was awarded the grade HD")
    elif (mark >= 75 and mark < 85):
        print(studentName + " was awarded the grade D")
    elif (mark >= 65 and mark < 75):
        print(studentName + " was awarded the grade C")
    elif (mark >= 55 and mark < 65):
        print(studentName + " was awarded the grade P1")
    elif (mark >= 50 and mark < 55):
        print(studentName + " was awarded the grade P2")
    elif (mark >= 45 and mark < 50):
        print(studentName + " was awarded the grade F1")
    else:
        print(studentName + " was awarded the grade F2")
    continueAnswer = input("Continue? ")
    continueAnswer = continueAnswer.lower()
    if (continueAnswer == "no"):
        print("Best of luck for next semester !!!")
        break;
