# multiple inheritance


class Student:
    dstt="rudraprayag"
    def __init__(self,Sname,Sage,Sdept):
        self.name=Sname
        self.age=Sage
        self.dept=Sdept

class Player:
    no_of_game=4
    def __init__(self,game):
        self.game=game
        

       

class CoolProgrammer(Player,Student):
    languages=["c","python"]
    def __init__(self, Sname, Sage, Sdept,game):
        Student.__init__(self,Sname, Sage, Sdept)
        Player.__init__(self,game)



shivam=Student("Shivam",26,"IT")
atul=Student("atul",26,"ME")

sanju=CoolProgrammer("sanju",26,"it","Foosball")
print(sanju.__dict__)



