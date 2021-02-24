#A student managememnt program.
#Developed over lab with increasing funcionality added.
#
"""
Version 6.2: function to display a menue and get user choice
Version 6.3: added container functions for adding a student and view a student. And added a while loop to the main program to continue looping 
This version added read modules and add student from testing scripts 6.4 & 6.5 """
#Author: Jon Ishaque


students =[]

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

def doAdd(students):
    #create a dictionary for the current student
    currentStudent = {}
    #get student name from user input and add to dictionary key 'name'
    currentStudent["name"]=input("enter student name :")
    #call function to for user to enter studne modules
    currentStudent["modules"]= readModules()
    #append current student to students list
    students.append(currentStudent)
def readModules():
    #Create a list for the modules of student name definined
    #in current iteration of doAdd
    modules = []
    #assign user input to module name#instruct user to enter blank to quit
    #strip method to remove training and leading space if they exist
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    #loop, collecting module names and grades until the user enters "" blank to quit
    while moduleName != "":
        #define a dictionary for current module
        module = {}
        #assign module name to module key "name" of current module from ModuleName Variable
        module["name"]= moduleName
        # no error handling
        #assgign grade to key "grade" of current module from user input
        module["grade"]=int(input("\t\tEnter grade:"))
        #module dictionary for current module to module list
        modules.append(module)
        # now read the next module name
        #before exiting the loop check if user want to add another another module
        #if return not blank go to start of this while loop.
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules


#Main program
#call display menu function
choice = displayMenu()
#use choice input to control flow of main while loop.
#
while(choice != 'q'):
# we could do this with lamda functions# I am keeping this basic for the moment
    #if user select 'a' then call doAdd funcion - add a student
    if choice == 'a':
        doAdd(students)
    #if user select 'a' then call doView funcion - view a student
    elif choice == 'v':
        doView(students)
    #else the user has made a non-valid data entry for the program
    
    elif choice !='q':
        #output reminder to user of available options.
        print("\n\nplease select either a,v or q")
    
    #call dsiplay menu to get user choice
    choice=displayMenu()
    
