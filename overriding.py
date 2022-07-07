class a():
    classVar1="Hi i am class variable of A"
    def __init__(self):
        self.classVar1="Hi i am a instance variable of class A"
        self.var1="instance A"
        self.special="sepcial"

class b(a):
    classVar1="Hi i am class variable of B"
    def __init__(self):
        super().__init__()
        self.classVar1="Hi i am a instance variable of class B"
        # self.var1="instance B"

A=a()
B=b()
print(B.classVar1)