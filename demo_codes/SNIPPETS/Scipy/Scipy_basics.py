from operator import imod
from numpy.lib.npyio import _genfromtxt_dispatcher
from scipy.optimize import minimize
from scipy.sparse.construct import random
# problem is to minimize the function f(x)=((x-3)**2)

def resolver(x):
    return ((x-3)*2)                #function definition

#problem set-2
#2-D prblem having two variables and constraints are included as well;

f=lambda x:(x[0]-1)**2 + (x[1]-2.5)**2

#ubjected to the constraints:
"""designing constraints"""
cons=({
    'type':'ineq', 'fun':lambda x:x[0] -2*x[1] +2,
    'type':'ineq', 'fun':lambda x:-x[0] -2*x[1] +6,
    'type':'ineq', 'fun':lambda x:x[0] +2*x[1] +2
})
bnds=((0, None), (0, None))         #boundary lines for x and y-axes

result=minimize(f, (20,0), bounds=bnds, constraints=cons)
###print(result)



"""INTERPOLATION """
#used to estimate the unknown vvalue from a function through the set of given values that are known,and by drawing a statistical graph between them
#basic importing

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import random

myarr=np.array([random.randrange(10,99) for i in range(10)])
newarr=np.array([random.randrange(10,99) for i in range(10)])
plt.scatter(myarr, newarr)
plt.xlabel("X_Axis")
plt.ylabel("Y_Axis")
plt.title("here is my pyplot diagram")
plt.show()


from scipy.interpolate import interp1d

"""need to create an interpolation function so that we can obtain th values from that interpolated ffuncton"""

f==interp1d(myarr, newarr, kind='cubic')
newdata=np.arange(10,50,4)



plt.plot(f)
