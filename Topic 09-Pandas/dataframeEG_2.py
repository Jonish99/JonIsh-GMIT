'''program to explore pandas data frames, reading from a log file and cleaning data'''
#Author: Jon Ishaque

import pandas as pd
import re
import matplotlib.pyplot as plt

############
#funcitons
def getNewValue(x):
    newvalue = re.search('[\w:/]+', x).group()
    # do your stuff
    return newvalue



############
path = '../pands2021/labs/'
logFilename = path + 'access.log'
colNames= ('ip',
'dash1',
'userId',
'time',
'url',
'status code',
'size of response',
'referer',
'user agent',
'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

#drop columns with just dashes
df.drop(columns=['dash1', 'userId'], inplace=True)
#remove[] from time
#use apply function to hit every elemnet in the column and returen a series
#and make the original column equal to that
#df['time'] = df['time'].apply(getNewValue)

#convert to string before reg ex function

df['time'] = df['time'].apply(str)
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

#reformat time

df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

print(df.dtypes)
print (df['time'].head(600))

#get event between two dates (2 methods)
# way one use the loc function
#newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
# way 2 use the series function between
#newdf = df[df.time.between(start_date, end_date)]
# way three set the index to the date column
# this give a whole pile of handy features
df = df.set_index(['time'])
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
#newdf = df.between_time('23:00', '23:59') # this is times every day
print (newdf)

#sample download sites
# sample the download sizes say every 30 Minutes
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)
downloadSamples.plot()
plt.show()
