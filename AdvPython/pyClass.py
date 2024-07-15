class AptechStudent:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def getDOB(self):
        return 2024 - self.age
    
    def getDesc(self):
        return f"My name is {self.name} i am {self.age} years old"
    
    def birthStatus(self):
        if(self.gender == "female"):
            return "You can give birth"
        if(self.gender == "male"):
            return "You can't give birth"


student1 = AptechStudent("great" ,11 , "female" , )

print( student1.getDesc())