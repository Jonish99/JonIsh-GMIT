#A student managememnt program.
#The add student name and add modules funcitons for the student management program are developed in a separate file.
#
#This version we have added the readModules function

"""
Version 1: Get student details
This version adds readModule function
 """
#Author: Jon Ishaque



#create empty  list called students
students= []

#define readModules function to add stuent modules  No arguments or return data yet
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

#define doAdd function to add student names to list 
def doAdd(students):
    #create a dictionary for the current student
    currentStudent = {}
    #get student name from user input and add to dictionary key 'name'
    currentStudent["name"]=input("enter student name :")
    #call function to for user to enter studne modules
    currentStudent["modules"]= readModules()
    #append current student to students list
    students.append(currentStudent)

#testdoAdd(students)

doAdd(students)
#test, output content of students
print(students)