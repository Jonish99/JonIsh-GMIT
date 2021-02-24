#A program to take a float and output an integer
#Author:Jon Ishaque

#use the input function to assign user input to numToRound, first coverting the input string to a float
numToRound=float(input("Enter a float number:"))
#use the round function to round numToRound and assign to RoundNum
roundNum=round(numToRound)

#output and format numbers to strings using the format method of strings
print("{} rounded is, {}".format(numToRound,roundNum))