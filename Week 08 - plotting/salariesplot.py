'''
A program that:
1. creates a list of (random) salaries
2. forces the same random list each time the program is run
3. creates a second random list of ages
4. creates random scatter plot for the data
5. with an added line of y=x*x

'''
#Author: Jon Ishaque

#imports
import matplotlib.pyplot as plt
import numpy as np 
# set absolute range
minSalary = 20000
maxSalary = 110000
minage = 21
maxage = 65

#fixed number of salaries
NumberOfEntries = 100

#ensure same random salaries happen each time program is run
np.random.seed(1)
#use randint of np to generate NumberOfEntries between minSalary and maxSalary
salaries = np.random.randint(minSalary,maxSalary,NumberOfEntries)
ages = np.random.randint(minage,maxage,NumberOfEntries)

#create line arrays
xpoints =np.array(range(1,101))
ypoints = xpoints * xpoints #i.e x squared
#create a plot with lists as coordinates
plt.plot(xpoints,ypoints,color='r')
#add a label
#plt.plot.__annotations__("y=x*x")



#plot the scatter
plt.scatter(ages,salaries)
#add a title to the plot
plt.title("Random Plot")
#add axes labels
plt.ylabel("Salaries")
plt.xlabel("Ages")
#display the scatter
plt.show()
plt.savefig("Prettier-plot.png")
