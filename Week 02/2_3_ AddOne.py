#A program to get an input from a user, a number, convet it to an int and add one to it
#using the format method of a string object to convert the numbers to strings for the output message.
#Author: Jon Ishaque


#enter a number, convert input to an int
#use input function to to output msg to user to enter a number. 
# #Use int() function to convert possible real/float to int. (a string will error when performted on arithmetically)
Num=int(input('Please enter a number:'))
#add one to num and assign outcome to NewNum variable
NewNum = Num + 1 
#use the format method to output the message as text version of the expression. x + 1 =y
print('{} + 1 is {}'.format(Num,NewNum))