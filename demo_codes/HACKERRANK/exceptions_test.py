t=int(input("enter value of t: "))

for i in range(t):
    a,b=input("enter a and b here: ").split()

    try:
        print(int(a)//int(b))
    except(ValueError, ZeroDivisionError) as e:
        print("error code: ",e)
