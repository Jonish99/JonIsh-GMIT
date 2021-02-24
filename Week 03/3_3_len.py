#A program to read a string and output length of string
#Author:Jon Ishaque

#Use the input function to assign a string to var, inputStr

inputStr=input("Enter a string:")
#assign length of inputStr to var, inputStrlen using len function
inputStrLen = len(inputStr)

#print and output using format method.
print("The lenght of the string {}, is {}".format(inputStr,inputStrLen))