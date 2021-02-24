
'''This programme reads in a
percentage and prints out corresponding grade, modified to convert a decimal to an integer/round'''
#Author: Jon Ishaque

#get input, convert str to int and assign to variable, 'percentage'
percentage = int(input("Enter the percentage: "))

#use  if and elif to test possiblities
#1 if out of range, output msg to user to enter another number
if percentage < 0 or percentage > 100:
    # throw error (not)
    print("Please enter a number between 0 and 100")
# test if 0 to 39
elif percentage < 40: 
     #if test is true print output
    print("Fail")
#test if 40 to 49
elif percentage < 50: 
    #if test is true print output
    print("Pass")
# test if 50 to 59
elif percentage < 60: 
    #if test is true print output
    print("Merit1")
#test if 60 to 69
elif percentage < 70:
    #if test is true print output
    print("Merit2")
# must be 70 and 100
else: 
    #print only other possible output
    print("Distinction")