#A student managememnt program.
#Developed over lab with increasing funcionality added.
#
"""
Version 6.3: function to display a menue and get user choice
added container functions for adding a student and view a student. And added a while loop to the main program to continue looping 
until user enters quits"""
#Author: Jon Ishaque




#Functions
def displayMenu():
    #output initial menu with command and instructions for the user.
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    #instruct user to input and get user input
    choice = input("Type one letter (a/v/q):").strip()
    
    #return choice
    return choice

def doAdd():
    #we fill this in laterprint("in adding")
    print("add")

def doView():
    # we fill this in laterprint("in viewing")
    print("view")

#Main program
#call display menu function
choice = displayMenu()
#use choice input to control flow of main while loop.
#
while(choice != 'q'):
# we could do this with lamda functions# I am keeping this basic for the moment
    #if user select 'a' then call doAdd funcion - add a student
    if choice == 'a':
        doAdd()
    #if user select 'a' then call doView funcion - view a student
    elif choice == 'v':
        doView()
    #else the user has made a non-valid data entry for the program
    
    elif choice !='q':
        #output reminder to user of available options.
        print("\n\nplease select either a,v or q")
    
    #call dsiplay menu to get user choice
    choice=displayMenu()
    
