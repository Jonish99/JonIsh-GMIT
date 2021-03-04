#A student managememnt program.
#Developed over lab with increasing funcionality added.
#
"""
Version 6.2: function to display a menue and get user choice
Version 6.3: added container functions for adding a student and view a student. And added a while loop to the main program to continue looping 
Version 6.6: added read modules and add student from testing scripts 
Version 6.7:  added view display modules, doView, displayStudents
version 7.1: added save function 
whilst saving and opening an existing file the system path must be determined using os path.

"""
#Author: Jon Ishaque

#imports
import json 
import sys
import os.path

#initiate student list
students =[]

#Functions
def displayMenu():
    #output initial menu with command and instructions for the user.
    print("What would you like to do ?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    #instruct user to input and get user input
    choice = input("Type one letter (a/v/s/q):  ").strip()
    print(choice)
    
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

#argument is modules dicionary for current student
def displayModules(modules):
    #function to print name and grade of all modules for current student
    print("\tName   \tGrade")
    #loop through modules for current student
    for module in modules:
        #output name and grade for current module
        print("\t{}\t{}".format(module["name"], module["grade"])) 

#argument is list of students if any
def doView(students):
    #function for any students in students list print student name and then call display module fuction for that student name
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

def doSave(students):
    #code to write to json file
    #sub function call. 
    with open( filename, 'wt') as f:
        #pass students from function call to be written to file name.
        json.dump(students,f)

#use open file  functions to read the json file and return the formatted data as a list.
def doLoad(filename):
    with open(filename) as f:
        return json.load(f)

#Main program

#assign file name & prefix double slash to join file name string
#\\ is how python deals with paths.

filen = '\\students.json'
#this system requires an absolute path from to find file
mypath =str(os.path.dirname(os.path.abspath(sys.argv[0])))
#join the path with the file

filename = mypath+filen
#check file exists
if not os.path.isfile(filename):
    bfile = False
    
    #we will create the file at the first option to save.


students = doLoad(filename)
#call display menu function
choice = displayMenu()
#use choice input to control flow of main while loop.

while(choice != 'q'):
# we could do this with lamda functions# I am keeping this basic for the moment
    #if user select 'a' then call doAdd funcion - add a student
    if choice == 'a':
        doAdd(students)
    #if user select 'a' then call doView funcion - view a student
    elif choice == 'v':
        doView(students)
    
    #if user select 's' the call doSave function - save the file
    elif choice == 's':
        doSave(students)
    #else the user has made a non-valid data entry for the program
    
    elif choice !='q':
        #output reminder to user of available options.
        print("\n\nplease select either a,v,s or q")
    
    #call dsiplay menu to get user choice
    choice=displayMenu()
    
