# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def example():
	mylist = []
	for x in range(100):
		mylist.append(sqrt(x))
'''

# timeit statement
print (timeit.timeit(setup = mysetup,
					stmt = mycode,
					number = 10000))

import timeit

def myfun():				#USING DEFAULT_TIMER() METHOD TO GET TIME LAPSES
    
    ST=timeit.default_timer()
    
    value=10
    print("ANY NUMBER  here to be represented is {}".format(value))
    
    print("time of execution :", (timeit.default_timer()-ST ))

print(myfun())
