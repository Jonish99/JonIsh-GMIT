
'''program to ask as user to input a number
and tell if the number is even or not'''
#Author: Jon Ishaque

#Get user input,covert to integer and assign to variable
#initiate num
num = 0
#continue until user enters -1

num =int(input("Enter a number, enter -1 to quit:"))
while num !=-1:
    if (num % 2) == 0:
        print("{} is a an even number".format(num))
    else:
        print("{} is an odd number".format(num))
    num =int(input("Enter a number, enter -1 to quit:"))
