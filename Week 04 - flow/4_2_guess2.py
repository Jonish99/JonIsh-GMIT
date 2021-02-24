
'''program to loop until a user guess the number'''
#Author: Jon Ishaque

#import random library
import random

#use randint function from random library to generate random number in range 1-100
numToGuess = random.randint(1,100)
#for tessting
#print (numToGuess)


#get user input and convert to integer
Guess = int(input("Please enter a number to guess the correct answer:"))
##loop until user inputs Guess = numToguess
while numToGuess  != Guess:
    #test numToGuess to give hint
    if Guess < numToGuess:
        #print hint
        print("Hint, too low")
    else:
        #print hint
        print("Hint, too high!")
    #Get new Guess and conver to integer, go back to start of while loop.
    Guess = int(input("Please try again:"))

#output congratulations correct msg, using format method to convert integer to string

print("Well done, {} is the correct answer".format(numToGuess))
