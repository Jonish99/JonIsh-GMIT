#A program to read a string
#remove trailing and leading space
#convert to lower case
#and output formatted string and string length

#Author:Jon Ishaque

#use input function to get user inut and assign to var rawStr
rawStr=input("Enter any amount of text:")

#normalise, using strip method to removed training space and lower method to convert to lower case.
normalsisedStr= rawStr.strip().lower()

#get length of rawSr and assign to variable lenRawStr
lenRawStr=len(rawStr)

#Getlenth of normalsedStr using len function and assign to var lenNormalisedStr
lenNormalisedStr=len(normalsisedStr)

#output using the normalised string used format method of strings
print ("The string normalised is, {}".format(normalsisedStr))

#out put message ussing format method to convert string length values from integers to strings
print("The length of the raw string is {} characters, and the lenght of the normalised string is {} characters".format(lenRawStr,lenNormalisedStr))