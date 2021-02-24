#A program that floors a number
#Author: Jon Ishaque

#import math library
import math

numToFloor = float(input("Enter a float number:"))
#use the floor function of the math library to get the floored value of numToFloor and assign outcome to Floored Num
flooredNum =math.floor(numToFloor)

#Output and format numbers to string using format method of strings.
print("{} floored is {}".format(numToFloor,flooredNum))