class Employee():
    def __init__(self,fname,lname):
        self.name=fname
        self.surname=lname
        # self.email=f"{fname}.{lname}@abacasys.com"

    @property
    def email(self):
        if self.name==None or self.surname==None:
            return "Email is Not set Please Set the email"
        return f"{self.name}.{self.surname}@abacasys.com"


    @email.setter
    def email(self,string):
       
        names=string.split("@")[0]
        self.name=names.split(".")[0]
        self.surname=names.split(".")[1]
    
    @email.deleter
    def email(self):
        self.name=None
        self.surname=None
emp1=Employee("shivam","negi")
print(emp1.email)

emp1.email="suresh.kumar@and.com"
print(emp1.email)
del emp1.email
print(emp1.email)
# emp1.