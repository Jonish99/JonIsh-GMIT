#A program that makes a pie plot of the unique occurences value sin an array
#Author: Jon Ishaque

import numpy as np 
import matplotlib.pyplot as plt

#create an array
possibleCounties =['Cork','Kerry','Waterford','Limerick','Tipperary']

#pick 100 randomly from possible countries with the frequency set in p

counties = np.random.choice(possibleCounties, p=[0.1, 0.3, 0.2, 0.12, 0.28], size=(100))

#get the number of occurences of each county, returns a tuple of the uniqque values and how many times they appear
#research this
unique, counts = np.unique(counties,return_counts=True)

#add to a bar plot

plt.bar(unique,counts)
plt.show()