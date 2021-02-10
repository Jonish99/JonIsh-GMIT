#Programme to subtract two numbers
#Author: Jon Ishaque

#input reads a string and convets to int so it can be worked on arithetically.

x=int(input("Enter a number:"))
y=int(input("Enter another number:"))

answer = x - y

#format output
print ("{} minus {} equals {}." .format(x,y,answer))