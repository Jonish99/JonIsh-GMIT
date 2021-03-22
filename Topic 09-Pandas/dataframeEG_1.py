'''program to explore pandas data frames, write to and read from'''
#Author: Jon Ishaque

import pandas as pd
import openpyxl
listDAta= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
print(df.head(3))
print(df)
print(df.describe())
print(type(df.describe()))
path = "../pands2021/labs/"

#write to csv
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)

#write to wb with ws for summary
excelFilename = path +'grades.xlsx'
with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")

#calculate and print the mean
#get the mean from describe'
mean = df.describe().loc['mean','grade']
print(mean)
# or calculate the mean
mean = df['grade'].mean()
print (mean)