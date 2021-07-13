from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
import random


mydata=[random.randrange(10,99) for i in range(10)]
data= np.linspace(0,10,100)
x=np.sin(data)
y=np.cos(data)

ary1=np.array([10,20,30,40,50])
ary2=np.array([20,30,40,50,60])

ary3=np.array([x*10 for x in range(5,10)])
ary4=np.array([x*10 for x in range(10,15)])


plt.plot(ary1, ary2, 'o--b')
#plt.show()
#plt.close()

#CREATING SUBPLOTS:CREATING LABELS:CREATING TITLES

plt.subplot(1,3,1)
plt.plot(ary3,ary4, 'o--b')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("first plot")

plt.subplot(1,3,2)
plt.plot(ary2,ary1, 'o--c')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Second plot")

plt.subplot(1,3,3)
plt.plot(ary4,ary1, 'o--y')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Third plot")

"""Super title added"""
plt.suptitle("Super title for first plotting")
plt.show()
plt.close()






"""creating histogram"""

myhistogram=plt.hist(mydata)
#plt.show()
plt.close()

"""creating a scatter plot"""
x=[random.randrange(10,99) for i in range(10)]
y=[random.randrange(10,99) for i in range(10)]

scatterplot=plt.scatter(mydata, x, marker=".", s=25, c="r" )                #dont know how to add labels in x and y - axes
scatterplot=plt.scatter(mydata, y, marker="*", s=15, c="b" )

#plt.show()
plt.close()

"""creating a pie chart """
#creating a list of values to be used as labels:
labelData=['A', 'B', 'C', 'D', 'E']

plt.pie(mydata[:5], labels=labelData)
#plt.show()
plt.close()
