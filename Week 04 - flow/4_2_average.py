
'''Aprogram to use a for loop to keep reading a number and add it to a list until
the user enters 0 then print back the list with the average of the list '''
#Author: Jon Ishaque

#create empty list
nums = []


# get first num and convert string from input function to integer
num = int(input("enter number (0 to quit): "))
#start while loop, loop while num does not equal 0:
while num != 0:
    #append num to nums list
    nums.append(num)
    # read the another, loop will check value of num when it gets back to start
    num = int(input("enter another (0 to quit): "))

#User a for loop to scroll through the elements in nums
for value in nums:
    #print the value
    print(value)
# get average sum of elements in nums list divided the number of elements in the list(length). Convert to float and assign to var, average
average = float(sum(nums)) / len(nums)
#out put the average of the list using the format method of strings to convert the average to a string.
print("The average is {}".format(average))