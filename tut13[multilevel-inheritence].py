class Dad:
    basket=1
class Son(Dad):
    dance=1
    def Mydance(self):
        return f"I can dance {self.dance} no. of times"

class Grandson(Son):
    # dance=6
    # # def Mydance(self):
    # #     return f"grandson can dance {self.dance} no. of times"
    pass
    

ram=Dad()
shyam=Son()
dham=Grandson()
print(dham.basket)