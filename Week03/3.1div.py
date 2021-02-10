"""A prog that reads in two numbers,divides the first one by the second and give the integer result and the remainder"""
#Author: Jon Ishaque
x=int(input("Enter a number:"))
y=int(input("Enter another number:"))

#answer as integer
#remainder use mod operator
answer = int(x//y)
remainder = x%y 

#format output
print ("{} divided {} is  {}, remainder {}" .format(x,y,answer,remainder))