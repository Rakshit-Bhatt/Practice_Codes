import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy


filedata=pd.read_csv('F:\demo_codes\SNIPPETS\PYTHON PANDAS\dirtydata.csv')
print(filedata.head(0))
print(filedata.tail(0))

print(filedata.info())

"""data clenaing methods"""

#print(filedata.to_string())
#newfile=filedata.dropna()
#newfile=filedata.fillna(1010101010101)
#newfile=filedata["Calories"].fillna(101010101)
#print(newfile.to_string())
print("Success")
filedata.loc[7,'Duration']=45           #to locate a index and change a value of a particular value
#print(filedata.head(10))

#print("value of index 10th at Duration is: ",(filedata.loc[10,'Duration']))

#locating a place and removing that row completly, use loc() method and dropna() as a looper

df=pd.read_csv('F:\demo_codes\SNIPPETS\PYTHON PANDAS\dirtydata.csv')
 #creating a list of multiple condtions, smarter way:

for i in df.index:
    conditions=[
            df.loc[i, 'Duration']>60,
            df.loc[i, 'Date']==np.NAN,
            df.loc[i, 'Pulse']==np.NAN,
            df.loc[i, 'Maxpulse']==np.NaN,
            df.loc[i, 'Calories']==np.NaN
            ]
    if any(conditions):
        df.drop(i)

#print(df.to_string())
#print(df.drop_duplicates())

"""printing correlation between labels and their datas"""

print(df.corr())

#plotting pandas files modules through 'plt':
df.plot()
df.plot(kind='scatter', x='Duration', y='Pulse') #scatter plot
df['Maxpulse'].plot(kind='hist' )       #histogram, uses only one column

plt.show()