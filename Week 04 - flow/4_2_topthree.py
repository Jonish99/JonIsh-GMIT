
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

#initate a list
nums=[]
#loop 10 times to get 10 numbers and append to list
for i in range(1,10):
    #use random int function to get a random number between specified range and append through nums list
    nums.append(random.randint(rangeFrom,rangeTo))
#Output how many numbers and the nums list
print("{} random numbers\t {}".format(howMany,nums) ) 

#copy the list to a new list
topOnes = nums.copy()
#sort the list in reverse order
topOnes.sort(reverse = True)
#output the lists using the format method of strings and just get the 
# #ange from 0 (first element) upto, 3,but not including the 3rd element. topOnes[0:3] ie (1st, 2nd & 3rd elements)
print("The top {} are \t\t{}".format(topHowMany,topOnes[0:topHowMany]))