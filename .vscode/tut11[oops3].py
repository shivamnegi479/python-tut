class Employee:
    no_of_leaves=8
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def ChnageLeaves(cls,newLeaves):
        cls.no_of_leaves=newLeaves

    @classmethod
    def from_str(cls,string):
        params=string.split("-")
        return cls(params[0],params[1])
emp1=Employee("Shivam",23)
emp2=Employee("Atul",27)
# emp2.ChnageLeaves(23)
# emp1.ChnageLeaves(28)
# print(emp1.__dict__)
# print(emp2.no_of_leaves)
emp3=Employee("karan-29")