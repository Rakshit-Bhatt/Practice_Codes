from hashlib import new
import random, timeit

def bubble_sort(dataset):

    ST=timeit.default_timer()

    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j]>dataset[j+1]:
                temp=dataset[j]
                dataset[j]= dataset[j+1]
                dataset[j+1]= temp
    
    print("Execution time is: ", (timeit.default_timer()  - ST))


#generating random 10 values from random() module
dataset=[random.randrange(1000000,9999999) for i in range(20)]  

print(dataset)
bubble_sort(dataset)
print(dataset)