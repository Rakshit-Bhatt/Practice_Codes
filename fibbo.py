#method 1. worst algorithm for calculation. A mere one value increment makes it too long to compute.

import string, timeit

def fibbo(value):
    a,b=0,1
    if value<=2:
        return 1
    
    return fibbo(value-1) + fibbo(value-2)

#method 2. it uses a list to append values and then we can access nth fibbo value through indexing.

def new_Fibbo(value):
    fibbo=[0,1]
    for i in range(2, value+1):
        fibbo.append(fibbo[-1] + fibbo[-2])   #adding last and 2nd last indexed values
    return fibbo                          #return type is <type'list'>

#method 3. It barely uses previous values from memory, It only uses last two values and fetch the result

def latest_fibbo(value):
    a,b=0,1
    fibbo=a+b
    temp=0
    if value==0:
        return a
    if value==1:
        return b
    if value>1:
        for i in range(1, value+1):
            c=a+b
            a=b
            b=c
    
    return b

while True:
  
    val=input("enter the value for fibbo sum: ")
    
    #starting first timer instance
    START_TIMER=timeit.default_timer()

    choice_for_function=int(input("Enter 1 for older function\nEnter 2 for new function\nEnter 3 for latest function (Dynamic approach based)>>> "))
    if choice_for_function==1:
         
        val=int(val)
        print("Answer is: ",fibbo(val))
        print("time consumed is: ", (timeit.default_timer()-START_TIMER))

        print("\nwanna try again?? type 'y' for yes. otherwise press Enter")
        choice=input()

        if (choice=="Y" or choice=="y"):
            True
        else:
            break

    if choice_for_function==2:
         
        val=int(val)
        answer=new_Fibbo(val)
        print("Answer is: ",end=" ")
        print(answer[val])
        
        print("time consumed is: ", (timeit.default_timer()-START_TIMER))

        print("\nwanna try again?? type 'y' for yes. otherwise press Enter")
        choice=input()

        if (choice=="Y" or choice=="y"):
            True
        else:
            break
    if choice_for_function==3:
         
        val=int(val)
        answer=new_Fibbo(val)
        print("Answer is: ",end=" ")
        print(latest_fibbo(val))
        
        print("time consumed is: ", (timeit.default_timer()-START_TIMER))

        print("\nwanna try again?? type 'y' for yes. otherwise press Enter")
        choice=input()

        if (choice=="Y" or choice=="y"):
            True
        else:
            break
    