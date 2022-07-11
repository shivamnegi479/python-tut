class Employee:
    leavs=9
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __add__(self,other):
        return self.salary / other.salary

    def __truediv__(self,other):
        return self.salary%other.salary
    def __repr__(self):
        return f"Employee('{self.name}' {self.salary})"
        
    def __str__(self):
        return f"Hello My name is {self.name}"
emp1=Employee("Shivam",500)
emp2=Employee("atul",500)
# emp3=Employee("sanju",500)
# print(emp1+emp2)

print(emp1 + emp2)
print(emp1)       