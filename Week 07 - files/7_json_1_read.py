# a program to read the contents of a JSON file
# the program uses a function
#Author: Jon Ishaque


#imports
import json 

#set file name as actual path and file
#had to use the whole path, possiblly because working off one drive.
#Also note, python code error, forced to use forward slash in path

filename = 'C:/Users/jonishaque/OneDrive/GMIT/Programming and Scripting/JonIsh-GMIT/Week 07 - files/testdict.json'

def readDict(): 
# this will throw an error if the file does not exist
# # it should readly just return an empty dict 
# # we can do this later
    with open(filename) as f:
        return json.load(f)

# test the function 
somedict = readDict()

print(somedict)  