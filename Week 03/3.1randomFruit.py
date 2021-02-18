#print out a randome fruit using from a list
#Author:Jon Ishaque

#imports
import random

#create list of fruits
fruits =('Apple','Banana','Blackberry','Cherry','Mango','Pear','Orange','Kiwi','Pineapple')
#get a random number between 1 and lenght of list -1
index =random.randint(1,len(fruits)-1)

#output random fruit
print("A random fruit, {}".format(fruits[index]))