#A program that gives the absolute value of a number
#Author:Jon Ishaque

#use the input function to assign a number to a var'number', convert it from a string to a float
number =float(input("Enter a number:"))
#assign the absolute value of 'number' to variable absVal
absVal=abs(number)

#Output and format numbers to string using format method of strings.

print("The absolute value of {} is {}".format(number,absVal))