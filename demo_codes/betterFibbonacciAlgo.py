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
    value+=1
    for i in range(2, value):
        fibbo.append(fibbo[-1] + fibbo[-2])

    return fibbo
#NOT THAT EFFICIENT,, CANT PROCESS VALUES UPTO 1 Cr

#method 3. here the last two values are remembered only, while all the previous ones are popped. this will 
#save extra memory as well as computational time.

def ultra_new_fibbo(value):
    value+=1
    a,b = 0,1
    for i in range(2, value):

        c = a + b
        #one way swapping, we only need last two values as [-1] and [-2]
        a=b
        b=c

    return b   # c not gtaking as because of th previous value iteration, it got swapped and came to the placevalue of c



while True:
  
    val=input("enter the value for fibbo sum: ")
    
    #starting first timer instance
    START_TIMER=timeit.default_timer()

    choice_for_function=int(input("Enter 1 for older function\nEnter 2 for new function\nEnter 3 for ultra new function\n>>>"))
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
        print("Answer is: ",answer[val])
        
        print("time consumed is: ", (timeit.default_timer()-START_TIMER))

        print("\nwanna try again?? type 'y' for yes. otherwise press Enter")
        choice=input()

        if (choice=="Y" or choice=="y"):
            True
        else:
            break

    
    if choice_for_function==3:
         
        val=int(val)
        answer=ultra_new_fibbo(val)
        print("Answer is: ",end=" ")
        print(int(answer))
        
        print("time consumed is: ", (timeit.default_timer()-START_TIMER))

        print("\nwanna try again?? type 'y' for yes. otherwise press Enter")
        choice=input()

        if (choice=="Y" or choice=="y"):
            True
        else:
            break