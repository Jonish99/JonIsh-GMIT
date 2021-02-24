# programme to demonstrate tuples & accessing a range from the tuple
# Author: Jon Ishaque

#create tuple of 12 months
months=("January","February","March","April","May","June","July","August","September","October","November","December")
#Assign elements(months) to a new list, 'summer', i.e 4-7 means elements 0-4 = 5th month ie May, upto but including the 8th element(August),i.e July
summer=months[4:7]

#loop through the list
for month in summer:
    #print element in list at each loop interation.
    print (month)