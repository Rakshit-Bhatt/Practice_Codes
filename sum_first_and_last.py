n=int(input("enter a value: "))
sum_first_and_last=0

if n<=10:
    sum_first_and_last=n
    print("Sum is {}".format(n))

elif n>10:
    first_digit=n//10
    last_digit=n%10
    sum_first_and_last= first_digit + last_digit
    print("value > 10 and sum of digits is ", end='')
    print(sum_first_and_last)
    
else:
    pass