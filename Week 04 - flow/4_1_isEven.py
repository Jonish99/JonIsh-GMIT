
'''Aprogram to ask as user to input a number
and tell if the number is even or not'''
#Author: Jon Ishaque

#Get user input,covert to integer and assign to variable
num = int(input("Enter a number"))

#use modulus 2 to determine if even, if outcome(remainder) = zero then is even
if (num % 2) == 0:
    #output msg for even number
    print("{} is a an even number".format(num))
# else it must be odd!
else:
    #output msg for odd number
    print("{} is an odd number".format(num))
