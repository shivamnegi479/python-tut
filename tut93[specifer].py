class Employee():
    no_of_leaves=8
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    a=8
    __b=89
    def isPlayer(self,indoor):
        return f"{self.name} is a {indoor} player"



class Dancer():
    def __init__(self,danceStyle):
        self.dance=danceStyle
        

class player(Employee,Dancer):
    def __init__(self, name,age,dance):
        Employee.__init__(self,name,age)
        Dancer.__init__(self,dance)


    def gamePlay(self,game):
        return f"{self.name} is a {game} player "
                
class Accounts(player):
    def __init__(self, name, age, dance,salary):
        self.salary=salary
        super().__init__(name, age, dance)
 

# emp4=Accounts("Shivam",26,"classic",20000)
# print(emp4.isPlayer("foosball"))
# shivam=Employee("Shivam",25)
# atul=player("atul",26,"Hiphop")
# print(atul.dance)
# print(atul.isPlayer("atul Rubgy"))
# print(shivam.isPlayer("basketball"))

shivam=Employee("name",26)

print(shivam.Employee.__b)