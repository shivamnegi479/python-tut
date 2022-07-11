class a():
    def met(self):
        return f"hi i am a method of class a"
class b(a):
    def met(self):
        return f"hi i am a method of class b"
class c(a):
    def met(self):
        return f"hi i am a method of class c"
class d(c,b):
    # def met(self):
    #     return f"hi i am a method of class d"
    pass

D=d()
print(D.met())
