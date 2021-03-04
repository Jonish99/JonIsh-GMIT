# a program to demonstrate the use of JSON to store a dictionary
# the program uses a funcitno
#Author: Jon Ishaque


#imports
import json 

#set file name as actual path and file
#had to use the whole path, possiblly because working off one drive.
#Also note, python code error, forced to use forward slash in path

filename = 'C:/Users/jonishaque/OneDrive/GMIT/Programming and Scripting/JonIsh-GMIT/Week 07 - files/testdict.json'

sample= dict(name='fred', age=31, grades=[1,34,55])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)
    
#test the function

writeDict(sample)   