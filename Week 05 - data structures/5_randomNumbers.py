#A program print random numbers from a list, then loop through the list removing one number 
#and then outputting the number removed and the list

#Author:Jon Ishaque
#import library
import random

#initate list
queue=[]
#set length of list - not forceing but the max numbers the code below will append to the list
sizeOfList =10
#set random number max range, i.e random numers will be between 0 and 100
rangeTo =100
#loop to add 10(size of list) random numbers to queue
for n in range (0,sizeOfList):
    #append random number from randint function(from, to)
    queue.append(random.randint(0,rangeTo))

#output the whole of list, ';queue'
print ("queue is: {}".format(queue))

#loop until the number of elements in the queue = 0
#for each interation of the loop pop of the first number.
while len(queue) != 0:
    #pop 1st remaining number in (at front of) queue and assign to varible
    currentNum= queue.pop(0)
    #output currentnumber and remaining numbers, using format method of strings to convert list and number to string.
    print ("currentNum is, {} and the remaining numbers are:{}".format(currentNum,queue))

print ("Queue is now empty")