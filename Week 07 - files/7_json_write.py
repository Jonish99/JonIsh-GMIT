'''A file with opens a json file to demontrate how a json file can be used to store a 
dictionary file structure'''
#Author:Jon Ishaque

#imports
import json 
#assign file to filename

filename="testdict.json"
#create datastructure
sample= dict(name='fred', age=31, grades=[1,34,55])

#define write function
def writeDict(obj): 
    #open file as a write object
    with open(filename, 'wt') as f:
        #pass the conetents from the function call to be written to the file
        json.dump(obj,f)


#test the function - (need to read, to be sure it has worked.)

writeDict(sample)