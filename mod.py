import module1

print(module1.adds(4,8))

a = 4

print(id(a))
print(id(2))



# python Class
class Person:
    "THis is a Person Class"
    def __init__(self , name, age):
        self.name = name
        self.age = age

    def whoIS(self):
        print(f"{self.name} was born in {str(2024 -self.age)}")    
        


student1 = Person("Dele" , 22)

print(student1.whoIS())


# This is a class that does nothing and is empty

# creating an instance of an Object
print(sum([2,3,4,5,6,7,8]))

def aggg(*args):
    return sum(args)

print(aggg(2,3,4,5,67,7,8))