
    #A program tha will read a file an count how many times
    #it has been run. I tiwll do this by saving incrementing the count in separate file. 
    #The program will open the file, read the file and write to the file
    #The program will also test to see if the file it exists, if it does not it will create it with a '0' writter

#imports
import os.path

#set file name as actual path and file
#had to use the whole path, possiblly because working off one drive.
#Also note, python code error, forced to use forward slash in path
filename = 'C:/Users/jonishaque/OneDrive/GMIT/Programming and Scripting/JonIsh-GMIT/Week 07 - files/count1.txt'


#define function to read the the file
def readNumber():
    #add try - it will work because we have the isfile method already
    try:
        #use with to carry out file operations on file
        #open file and assign local name, f
        with open(filename,'r') as f:
            #read file contents, convert the string to an int and assign to variable
            number = int(f.read())
            #return the value of number to the function call
            return number
    except IOError
        # this file will be created when we write back.
        # # no file assumes first time running 
        # # ie 0 previous runs

        #the funciton call is expecting something.
        return 0



def writeNumber(number):
    
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number)) 


#main#


# check file exists
if not os.path.isfile(filename):
    print("File does not exist")
    #initialise file here
    
    writeNumber(0)
# call the function read number and assign its returned 
#value to the variable num


num = readNumber()

# increment the value of num, to include the current running of the program
num += 1
#output and the number, fomatted using format method.
print("we have run this program {} times".format(num))

#call write function, to increment the value in the file
writeNumber(num)
