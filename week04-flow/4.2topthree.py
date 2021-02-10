
'''program to generate 10 random number and print the top 3 '''
#Author: Jon Ishaque
#imports
import random

#how many number to generate
howMany =10
#how top numbers
topHowMany =3

#range for random generator
rangeFrom=0
rangeTo=100

#initate list
nums=[]
#loop to get 10 numbers and append to list
for i in range(1,10):
    nums.append(random.randint(rangeFrom,rangeTo))
#output howman and nums lis
print("{} random numbers\t {}".format(howMany,nums) ) 

#copy the list
topOnes = nums.copy()
#sort the list in reverse order
topOnes.sort(reverse= True)
print("The top {} are \t\t{}".format(topHowMany,topOnes[0:topHowMany]))