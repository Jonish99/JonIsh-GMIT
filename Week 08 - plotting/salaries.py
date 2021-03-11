'''
A program that:
1. creates a list of (random) salaries
2. forces the same random list each time the program is run
3. creates a second list with 5000 added to each of the original salaires
4. creates a third list with each salary of the 1st increased by 5%

'''
#Author: Jon Ishaque

import numpy as np 
# set absolute range
minSalary = 20000
maxSalary = 110000
#fixed number of salaries
NumberOfEntries = 10

#ensure same random salaries happen each time program is run
np.random.seed(1)
#use randint of np to generate NumberOfEntries between minSalary and maxSalary
salaries = np.random.randint(minSalary,maxSalary,NumberOfEntries)
#output salaries
print(salaries)

salariesPlus = salaries +50000 #add 5000 to each salary in the array
#output salaries plus
print(salariesPlus)

salariesMult = salaries * 1.05 # increases the original salaries by 5% in a new list

#output salaries 5%
print(salariesMult)
#convert salairesMult from float array to int array
salariesNew = salariesMult.astype(int)

#output salariesNew
print(salariesNew)

