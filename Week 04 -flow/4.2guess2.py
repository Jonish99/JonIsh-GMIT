
'''program to loop until a user guess the number'''
#Author: Jon Ishaque

#assign number to guess

#import random
import random

numToGuess = random.randint(1,100)
#for tessting
print (numToGuess)


##loop until user inputs 50
numToGuess = int(input("Please enter a number to guess the correct answer:"))
while numToGuess !=50:
    #test numToGuess to give hint
    if numToGuess < 50:
        print("Hint, too low")
    else:
        print("Hint, too high!")

    numToGuess = int(input("Please try again:"))

#output congratulations correct msg

print("Well done, {} is the correct answer".format(numToGuess))
