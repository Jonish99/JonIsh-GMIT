#program to read a string
#remove trailing and leading space
#convert to lower case
#and outputs str length
#this was also in lab 3.1
#Author:Jon Ishaque

#input str
rawStr=input("Enter any amount of text:")
#normalise
normalsisedStr= rawStr.strip().lower()
#get lenght of rawSr
lenRawStr=len(rawStr)

#Getlenth of normalsedStr
lenNormalisedStr=len(normalsisedStr)

#output
print ("The string normalised is, {}".format(normalsisedStr))
print("The length of the raw string is {} characters, and the lenght of the normalised string is {} characters".format(lenRawStr,lenNormalisedStr))