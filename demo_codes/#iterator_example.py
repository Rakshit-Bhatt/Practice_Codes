#trying to create a generator and later implementing the generator functions:

def squareList(num):
    sqaured=[i*i for i in range(num)]
    return sqaured

print("the output of squared table is {} ".format(squareList(10)))    


def sqauredGenerated(num1):
    for i in range(num1):
        yield (i*i)

def printGenerator(num2):
    for j in range(num2):
        print(next(output_hash))


usr_prompt1=int(input("enter how many digits you really want from the generator to make the list ???: "))
print(sqauredGenerated(usr_prompt1))

output_hash=sqauredGenerated(usr_prompt1)

usr_prompt2=int(input("enter how many digits you really want from the generator to fetch???: "))
#running the made function printGenerator() to fech valaues from gennerated list:
printGenerator(usr_prompt2)