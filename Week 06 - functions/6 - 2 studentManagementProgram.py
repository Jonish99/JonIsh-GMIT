#A student managememnt program.
#Developed over lab with increasing funcionality added.
#Version 16.2: function to display a menue and get user choice
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



#Main program
#test the fn
choice = displayMenu()
print("you chose {}".format(choice))