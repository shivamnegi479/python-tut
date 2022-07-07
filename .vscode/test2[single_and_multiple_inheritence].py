class Employee:
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def Emp_id(id):
        return f"Your Employee id is {id}"


class Hr:
    def __init__(self,leaves):
        self.leaves=leaves

        
# single level inheritence

class Accounts(Employee,Hr):
    def __init__(self, name, age, dept,salary,leaves):
        Employee.__init__(self,name, age, dept)
        Hr.__init__(self,leaves)
        self.salary=salary

Emp1=Employee("Ankit",26,"Angular")
Emp2=Accounts("shivam",36,"Python","20k",5)
print(Emp2.leaves)
print(Emp1.dept,Emp1.age,Emp1.dept) 
