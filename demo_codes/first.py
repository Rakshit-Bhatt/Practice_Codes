print(__name__)

global my_dict
my_dict={
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e'
}


print(my_dict)
#dictionary functions:

my_dict[6]='f'
print(my_dict)

for key,value in my_dict.items():
    print(key,' ',value)

#trying to copy a new dictionary:
global new_dict

# new_dict=my_dict
# new_dict[10]='new element'          #dictionary are immutable hence we cant simply create a copy and update it. it wil update the original one too

def new_update():
    new_dict=my_dict.copy()
    new_dict[100]='ANOTHER NEW ELEMENT'

    print(my_dict)
    print(new_dict)

def myfun():
    
    dict_stu={
     "name":"rakshit",
     "marks":[10,20,30,40]
    }
    
    temp=(dict_stu['marks'])
    print(temp)
    x_sum=0
    for i in temp:
        x_sum+=i
        
    print("sum of the values of fetched value_pair is: ",x_sum)

new_update()
myfun()

