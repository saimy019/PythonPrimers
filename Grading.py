mark=int(input("Enter marks 0 and 100: "))
if(mark>=85):
    print("The mark "+ str(mark)+ " gives the grade HD")
elif(mark>=75 and mark<85):
    print("The mark "+ str(mark)+ " gives the grade D")
elif(mark>=65 and mark<75):
    print("The mark "+ str(mark)+ " gives the grade C")
elif(mark>=55 and mark<65):
    print("The mark "+ str(mark)+ " gives the grade P1")
elif(mark>=50 and mark<55):
    print("The mark "+ str(mark)+ " gives the grade P2")
elif(mark>=45 and mark<50):
    print("The mark "+ str(mark)+ " gives the grade F1")
else:
    print("The mark "+ str(mark)+ " gives the grade F2")