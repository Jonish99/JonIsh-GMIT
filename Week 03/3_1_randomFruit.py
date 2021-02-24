#A program that prints out a random fruit  from a list, demontrating lists, the len function
#Author:Jon Ishaque

#imports
import random

#create list and assign 10 items in the list
fruits =('Apple','Banana','Blackberry','Cherry','Mango','Pear','Orange','Kiwi','Pineapple','Strawberry')
#get a random number between 1 and lenght of list -1, and assgign to a variable, 'index'.
index =random.randint(1,len(fruits)-1)

#output random fruit using the format method of string objects

print("A random fruit, {}".format(fruits[index]))