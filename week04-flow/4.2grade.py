
'''This programme reads in a
percentage and prints out corresponding grade'''
#Author: Jon Ishaque

#get input, convert str to float and assign to variable
percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    # throw error (not)
    print("Please enter a number between 0 and 100")
elif percentage < 40: 
    # 0 to 39
    print("Fail")
elif percentage < 50: 
    #  40 to 49
    print("Pass")
elif percentage < 60: 
    #  50 to 59
    print("Merit1")
elif percentage < 70:
    #  60 to 69
    print("Merit2")
else: 
    # must be 70 and 100
    print("Distinction")