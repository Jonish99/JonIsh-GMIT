
'''program to loop until a user guess the number'''
#Author: Jon Ishaque

#assign number to guess
numToGuess = 50


##loop until user inputs 50
numToGuess = int(input("Please enter a number to guess the correct answer:"))
while numToGuess !=50:
    print("Wrong!")
    numToGuess = int(input("Please try again:"))

#output congratulations correct msg

print("Well done, {} is the correct answer".format(numToGuess))
