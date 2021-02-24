#Program to subtract one number from another and output the result
#Author: Jon Ishaque

#input reads a string and convrets to int so it can be worked on arithmetically and assign to var x
x=int(input("Enter a number:"))
#input reads a string and convrets to int so it can be worked on arithmetically and assign to var y
y=int(input("Enter another number:"))

#Subtract y from x and assign to 'answer'
answer = x - y

#Format output using format method of string objct converting nubers back to strings
print ("{} minus {} equals {}." .format(x,y,answer))