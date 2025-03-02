#written by Garrett McCarthy

import numpy

def mult(*args): #Function that produces the factor of all the user numbers multiplied
    total = 1
    
    for x in args:
        total *= x
        
    return total #Returns product

def sub(*args): #Function that subtracts all numbers after the first number from the first number
    
    return args[0] - (sum(args[1:]))
        
def add(*args): #Function to find the sum of the users numbers
    
    return sum(args)

#Written by Khalid Soliman

while (0 == 0): #infinite loop that runs until the user stops it
    choice = input('''Enter operation
"+", "-", "*", or "q" to quit: ''') #asking for user's choice of operation

    if(choice != "+" and choice != "*" and choice != "-" and choice.lower() != "q"): #if input is invalid tell user and reset loop
        print("Invalid option \n")
        continue

    if(choice.lower() == "q"): #if user chooses to quit, break loop and end program
        print("Thanks for using this program!")
        break
    listSize = int(input("How many numbers do you want to enter: ")) #asking user for the amount of numbers to input

    numList = (numpy.zeros(listSize, dtype = int)) #creating array specified by user full of zeros
    for x in range(listSize): #asking user to enter the numbers they choose and saving to list
        entry = int(input("Enter number: "))
        numList[x] = entry
    if (choice == "+"): #if user selected addition, find sum
        print(f"{add(*numList)}\n")
    if (choice == "-"): #if user selected subtraction, find sum
        print(f"{sub(*numList)}\n")
    if (choice == "*"):
        print(f"{mult(*numList)}\n")
