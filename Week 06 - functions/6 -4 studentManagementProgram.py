#A student managememnt program.
#The add student name and add modules funcitons for the student management program are developed in a separate file.
#This version create and test the doAdd

"""
Version 1: Get student details
 """
#Author: Jon Ishaque



#create empty  list called students
students= []

#define readModulesfunction to add stuent modules  No arguments or return data yet
def readModules():    
    return []

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