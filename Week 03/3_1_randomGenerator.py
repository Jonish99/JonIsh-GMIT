#A program to print out random no between 1 & 10
#Author:Jon Ishaque

#import random library 
import random

#assign a random number to var using the randit function from the random library
number =random.randint(1,10)

#output a message using and format using the format method of the string object
print("Here is a random number, {}".format(number))

