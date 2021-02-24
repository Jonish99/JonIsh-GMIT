"""A program that reads in two numbers,divides the first one by the second and give the integer 
result and the remainder"""
#Author: Jon Ishaque
#use input function to enter a number,convert to an integer as the input is a string  and assign to variable x
x=int(input("Enter a number:"))
#use input function to enter a number,convert integer as the input is a string  and assign to variable y
y=int(input("Enter another number:"))

#answer as integer
#divide with an integer as result, discarding remainder and assign to answer variable
answer = int(x//y)
# get remainder from result of modulus expression and assign to variable
remainder = x%y 

#out message formatted using format method for strings, converting numbers to strings.
print ("{} divided {} is  {}, remainder {}" .format(x,y,answer,remainder))