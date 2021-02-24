#Uses a variable to store user name, add the variable(name) to a greeting
#and outputs the greeting and name
#assigns an integer to the variable age, outputs a string and converts the integer to a string to ensue
#the output works
#uses format to add variables to an output string.


#Author: Jon Ishaque
name="Jon"
print("Hello," + name)
#integer passed to variable, so python recognises age an integer.
age=45
#Output a message with the age. Age must converted to a string or python will throw an error as it will thing an addition is taking plce
#with line 'your age
print('Your age is: '+str(age))
#use the print format method, to add and formate name and age to output message.
print('Hello {}\tYour age is {}'.format(name,age))