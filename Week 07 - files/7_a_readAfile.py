
#A program tha will read a file an count how many times
#it has been run. I tiwll do this by saving incrementing the count in separate file. 
#The program will open the file, read the file and write to the file
#Author: Jon Ishaque

#set file name as actual path and file
#had to use the whole path, possiblly because working off one drive.
#Also note, python code error, forced to use forward slash in path
filename = 'C:/Users/jonishaque/OneDrive/GMIT/Programming and Scripting/JonIsh-GMIT/Week 07 - files/count1.txt'


#define function to read the the file
def readNumber():
    #use with to carry out file operations on file
    #open file and assign local name, f
    with open(filename,'r') as f:
        #read file contents, convert the string to an int and assign to variable
        number = int(f.read())
        #return the value of number to the function call
        return number




def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number)) 


#main#call the function read number and assign its returned 
#value to the variable num
num = readNumber()

# increment the value of num, to include the current running of the program
num += 1
#output and the number, fomatted using format method.
print("we have run this program {} times".format(num))

#call write function, to increment the value in the file
writeNumber(num)
