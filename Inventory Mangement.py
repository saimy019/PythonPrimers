######################
# Date: 01-05-2020
# Author: Mohammad Nawaid Saify
# Stage5
# IT Concept Assignment
# Environment: IDLE 3.8, Python 3.8
##########################

#Aarry taken for storing records
hardwarestore = []
#Method prompting user to enter another record
def doContinue():
    isContinue = input("Do you wish to enter another record? (Y/N) ")
    if isContinue.lower() == "y":
        return True
    elif isContinue.lower() == "n":
        return False
    else:
        doContinue()


def start(choice):
    #Imported date and time pre-defined package
    import datetime
    from datetime import datetime

    hid = 0

    if choice.upper() == "A":

        keepAsking = True
        # Defining list for storing data

        print ("Hardware Manager")

        # Starting while loop for user to enter data
        while keepAsking:

            nameOfHardwareProduct = input('Hardware: ')
            if nameOfHardwareProduct == "":
                print('No record has been recorded.')
                keepAsking = doContinue()
                if keepAsking:
                    continue
                else:
                    menu()

            yearOfProductPurchased = int(input('Purchase Year: '))
            if yearOfProductPurchased == "":
                print('No record has been recorded.')
                keepAsking = doContinue()
                if keepAsking:
                    continue
                else:
                    menu()

            productUser = input('User: ')
            if productUser == "":
                print('No record has been recorded.')
                keepAsking = doContinue()
                if keepAsking:
                    continue
                else:
                    menu()

            locationOfUser = input('Location: ')
            if locationOfUser == "":
                print ('No record has been recorded. ')
            elif locationOfUser.lower() not in ('home', 'office'):
                print ("No record has been recorded. ")
                keepAsking = doContinue()
                if keepAsking:
                    continue
                else:
                    menu()

            print (nameOfHardwareProduct + " " + "(" + str(
                yearOfProductPurchased) + ")" + " has been recorded as assigned to " + productUser + " and retained at " + locationOfUser + ".")
            ctime = datetime.now().strftime("%A,%d.%B %Y %I:%M %p")
            mtime = datetime.now().strftime("%A,%d.%B %Y %I:%M %p")
            hardwarestore.append(
                [nameOfHardwareProduct, yearOfProductPurchased, productUser, locationOfUser, ctime, mtime])
            #print (hardwarestore)
            with open("data.txt", 'w') as output:
                for i in range(len(hardwarestore)):
                    hstore = hardwarestore[i]
                    #print(str(i + 1) + " . " + hstore[0] + " (" + str(hstore[1]) + ") - " + hstore[2] + ", " + hstore[
                        #3] + "\n" + "Created: " + str(hstore[4]) + "\n" + "Modified: " + str(hstore[5]))
                    output.write(str(i+1) + " . " + hstore[0] + " (" + str(hstore[1]) + ") - " + hstore[2] + ", " + hstore[3] + "\n"+"Created: " + str(hstore[4]) + "\n"+"Modified: " + str(hstore[5])+ "\n")
            menu()

    elif choice.upper() == "L":
        #print (hardwarestore)
        if not hardwarestore:
            print("No Records to display")
        else:
            f = open("data.txt")
            for line in f:
                print(line)
            f.close()
            menu()

        menu()
    elif choice.upper() == "C":
        if not hardwarestore:
            print("No Records to display")
        else:
            ChangeItem = input("Enter Record ID ")
            cID=int(ChangeItem)
            filename = "data.txt"
            contents = []
            with open(filename, "r+") as f:
                frec = f.readlines()
                if cID > len(frec):
                    print("There are no records with the ID  "+str(ChangeItem))
                else:
                    for word in frec:
                        field = word.split(" ")
                        if field[0] == ChangeItem:
                            oldUser = field[5]
                            oldLocation = field[6]
                            newUser = str(input("Enter a new user:"))
                            newLocation = str(input("Enter a new location"))
                            field[5] = field[5].replace(oldUser, newUser)
                            field[6] = field[6].replace(oldLocation, newLocation + '\n')
                            contents.append(" ".join(field))
                            #print(contents)
                        else:

                            contents.append(" ".join(field))
                    frec = f.readlines()

            with open(filename, "w+") as f:
                for line in contents:
                    f.write(line)
            f.close()
        menu()

    elif choice.upper() == "D":
        DeleteItem = input("Enter Record ID ")
        DID= int(DeleteItem)
        filename = "data.txt"
        with open(filename, "r+") as f:
            lines=f.readlines()
            if DID > len(lines):
                print("No records found")
            else:    
                for w in lines:
                    words = w.split(" ")
                    if words[0] == DeleteItem:
                        print("You are about to delete " + str(words[2]) + " " + str(words[3]))
                        print ("Do you wish to delete this record " + DeleteItem + "(Y/N)")
                        DeleteItem = int(DeleteItem)-1
                        verifyDelete = str.lower(input(">"))
                        if verifyDelete == "y":
                            filename = "data.txt"
                            with open(filename, "r") as f:
                                lines = ' '.join([a for i, a in enumerate(f) if i != DeleteItem])
                                

                            with open(filename, "w") as f:
                                f.write(lines)
        menu()                       
                
    elif choice.upper() == "E":
        import csv
        import pandas as pd
        df = pd.read_csv("data.txt", delimiter=',')
        df.to_csv('data.csv')

        menu()

    elif choice.upper() == "Q":
        print ("Thank you")

        exit(0)
    else:
        print("Wrong choice !!. START AGAIN")


def menu():
    print("Hardware Manager")
    print ("(A)dd a new record")
    print ("(L)ist existing records")
    print ("(C)hange records")
    print ("(D)elete records")
    print ("(E)xport to CVS")
    print("(Q)uit")
    c = input("Your choice: ")
    start(c)


menu()
