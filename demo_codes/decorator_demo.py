#use of decorator in python

def older(name):
   
    print("HI",end=" ")
#new funnctionality to add the username and print a welcome messaage
    def newer():
        print(name,"\nWelcome tho the world of codes...")

    return newer()

older("rakshit")



#SECOOND METHOD HERE IS TO USE A DECORRATOR FUNCTION THAT CAN BE IMPLEMENTED AS A BASIC FUNCTIONALITY

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        
        #conditions for refinements....
        if a==0 or b==0:
            print("dude error values entered as a 0. going out....")
            return

        if a<b:
            a,b=b,a

        return func(a, b)
    return inner
 
@smart_divide
def divide(a, b):
    print(a/b)          #this is an error prone function so we are creating another function as well

divide(0,100)