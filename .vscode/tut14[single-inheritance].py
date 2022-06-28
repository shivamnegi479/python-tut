from operator import le


class Employee():
    State="Uttrakhand"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def Details(self,string):
        return f"hi {self.name} You are From {string} your age is {self.age}"
    
    @classmethod
    def changeState(self,state):
        self.State=state

shivam=Employee("Shivam",26,10000)
atul=Employee("atul",27,15000)

class Programmer(Employee):
    def __init__(self, name, age, salary,language):
        super().__init__(name, age, salary)
        self.language=language
    def printProg(self):
        return f"hi {self.name}  your age is {self.age}, Your Salary {self.salary}"

print(shivam.salary)
print(atul.salary)
sanju=Programmer("Sanju",24,30000,["python","java","C","C++","JavaScript"])
# print(sanju.name,sanju.age,sanju.salary)
print(sanju.Details("thenga"))
sanju.language.append("React")
sanju.language.sort()
print(sanju.language)
print(sanju.State)


