'''A file with opens a json file with an existing dictionary to demontrate how json can 
read from a dictionary file structure from a json file'''
#Author: Jon Ishaque

#imports
import json 

#assigne file name to variable

filename="testdict.json"
#define read function
def readDict(): 

# this will throw an error if the file does not exist
# it should readly just return an empty dict
# we can do this later 

    #open the file
    with open(filename) as f:
        #load the contents from fand return
        return json.load(f)
        
# test the function
# 
#assging contents of from function to variable
somedict = readDict()
#print output
print(somedict)