 import itertools
from itertools import count, product, permutations, combinations, accumulate
import operator

#using iter() method to create an iterable object from default ggiven data types:
mylist=([i for i in range(10)])  #no iter() funnction used and whole of the memory is being used

newlist=(i for i in range(10)) # menmory confined and stored
ans=[]
for i in newlist:

    ans.append(i)

print("answer of the generated array list from iterated method is ",ans)

#using different  methods:

a=[1,2,3,4,5]
b=[6,7,8,9,10]

tot=list(product(a,b))
print(tot)

#using permutations and combinations:
print(list(permutations(a)))
print(list(combinations(a,5)))

comb=(combinations(a,5))
#print("count of the values obtained is: ",(count(comb)))            #COUNT() METHOD UNABLE TO USE

# using accumulate() method:

list1=[a for a in range(10,100,10)]
list2=[a for a in range(15,150,10)]

new_tot=list(accumulate(list1))                 #need to TYPECAST the outputs into list() becoz it is readily the iter() object outputs:
old_tot=list(accumulate(list2))

fresh_tot=list(accumulate(list1, func=operator.mul))

print(new_tot)
print(old_tot)
print(fresh_tot)

