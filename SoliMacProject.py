#Khalid and Garrett Group Project

#Written by Khalid Soliman

import statistics
import random

def avg(): #function to produce 5 random integers and find their average
    nums = []
    print("Random Integers: ", end = '')

    for x in range(5):  #loop to produce, store, and output 5 random integers
        nums.append(random.randint(1, 20))
        print(f"{nums[x]} ", end = '')
    print(f"\nThe average of those random numbers is {statistics.mean(nums):.1f}") #finding and outputting the average of the 5 integers

def summation(): #function to produce 5 random integers and find the sum of all 5
    nums = []
    print("Random Integers: ", end = '')

    for x in range(5): #loop to produce, store, and output 5 random integers
        nums.append(random.randint(1, 20))
        print(f"{nums[x]} ", end = '')
    print(f"\nThe sum of that set of random numbers is {sum(nums)}") #find and output the sum of the lis

while (0 == 0): #written by Garrett McCarthy

    choice = input("Which operation do you prefer (A/S): ").upper() #receiving user input for desired operation

    if (choice == 'A'): #if they choose average, call average
        avg()

    elif (choice == 'S'): #if they choose summation, call summation function
        summation()

    else: #if user inputs unexpected value
        wrongInput = random.randint(1,3) #generating random number between 1 and 3

        if (wrongInput == 1): #if number previously generated is 1, call avg function
           avg()
        else: #If number is 2 or 3, call summation function
            summation()

    rerun = input("Continue? (Y/N): ").upper() #asking user if they want to continue

    print("")

    if (rerun == 'N'): #if user doesn't want to continue break loop
        break
    elif (rerun == 'Y'): #if the user does want to continue, restart loop
        continue
