#A program that assigns user input to a variable using the input fuction
#prints a message greeting with the variable
#an integer is assigned to a variable(age_ from the input function
#a message is printed out using the format method of a string, which converts the integer to a string

#Author: Jon Ishaque

#input msg, assign input to name using input function
name = input('Enter your name: ')
#output greeting and using + operator to join two strings
print('Hello '+ name)
#input msg, assign input to var age using input function
age = input('What is your age: ')
#output message and age using the format method of the string function, which converts the age to a string. 
print('Your age is {}'.format(age))