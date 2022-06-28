from attr import NOTHING


class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    @staticmethod
    def myfun(string):
        print(f"Hello {string}")
    
shiv=Student("shivam",25)
print(shiv.myfun("atul"))
