
'''program to use a for loop to keep reading a number and add it to a list until
the user enters 0 then print back the list with the average of the list '''
#Author: Jon Ishaque

#create empty list
nums = []


# get first num then we check if it is 0 

num = int(input("enter number (0 to quit): "))
while num != 0:
    nums.append(num)
    # read the another number and check for 0
    num = int(input("enter another (0 to quit): "))
#output list
for value in nums:
    print(value)
# get average as float
average = float(sum(nums)) / len(nums)
print("The average is {}".format(average))