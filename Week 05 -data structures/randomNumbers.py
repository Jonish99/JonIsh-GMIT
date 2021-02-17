#print random numbers from a list, then loop through the list removing one number 
#and then outputting the number removed and the list

#Author:Jon Ishaque
#import lib
import random

#initate array
queue=[]
#set length of array
sizeOfList =10
#set random number max range
rangeTo =100
#loop to add 10 random numbers to queue
for n in range (0,sizeOfList):
    queue.append(random.randint(0,rangeTo))

#output queue
print ("queue is: {}".format(queue))

#loop until all numbers are popped off queue
while len(queue) != 0:
    #pop 1st remaining number in queue and assign to varible
    currentNum= queue.pop(0)
    #output currentnumber and remaining numbers
    print ("currentNum is, {} and the remaining numbers are:{}".format(currentNum,queue))

print ("Queue is now empty")