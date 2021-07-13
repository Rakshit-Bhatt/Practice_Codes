import matplotlib
import numpy



# understanding collections
# there are five type of collections available here to provide additional functionality:
# counter, namedtuple, OrderedDict, defaultdict, deque:

# 1. COUNTER:

import timeit 
from collections import Counter

# it can count the frequencies of the characters used here:
my_str='aaabbbcccccdhjeejkedjffff'
a=Counter(my_str)


#methods available for accessing the key/value pairs:

print((a), type(a))
print(a.items())
print(a.keys())
print(a.values())

def count_fun():
            
    count=a.values()
    temp=0
    for i in count:
        temp+=i

    print('total characters used by my defined function:', temp)

print('total length of the string used by defined function:',len(my_str))

