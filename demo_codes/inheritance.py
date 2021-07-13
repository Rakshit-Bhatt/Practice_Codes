#TRYING TO USE THE CONCEPTS OF INHERITANCE AND RELATED PROPERTIES


class vehicle():
    def __init__(self,id,age,cond,usage):
        
        self.id=id
        self.age=age
        self.cond=cond
        self.usage=usage
        
    def represent(self):
        print("details of your vehicle is as follows: ")
        print("REG_ID= {} TIME= {} CONDITION= {} USABILITY= {}".format(self.id,self.age,self.cond,self.usage))
        
class Astonmartin(vehicle):
    def __init__(self,name):
        self.name=name
        
    def printname(self):
        print("Name is {}", format(self.name))

#main()
vec1=vehicle("20C152CH85","1990-2045","WORKING","OKAY")
vec2=Astonmartin("20C152CH85","1990-2045","NOT WORKING","NOT OKAY")

vec1.represent()
vec2.represent()
