from itertools import product

#timeit() module to test the time lapse
import timeit

def cart_product(list1, list2):
    return (product(list1 , list2))

if __name__=="__main__":

    a=[int(item) for item in input("Enter values for first list: ").split()]
    b=[int(item) for item in input("Enter values for second list: ").split()]
    
    START_TIME= timeit.default_timer()
    
    if len(a)<30 and len(b)<30:
        ans=cart_product(a,b)
        
    for i in ans:
        print(i, end=" ")

    print("\nTime of execution is ", (timeit.default_timer() - START_TIME))