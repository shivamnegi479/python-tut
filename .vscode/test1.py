# # single level inheritance

# from asyncio.windows_events import NULL


# class Student():
#     dstt="rudraprayag"
#     def __init__(self,Sname,Sage,Sdept):
#         self.name=Sname
#         self.age=Sage
#         self.dept=Sdept

#     @classmethod
#     def ChangeDstt(self,Newdstt):
#         self.dstt=Newdstt
#         return Newdstt


# shivam=Student("Shivam",26,"IT")
# atul=Student("atul",26,"ME")
# atul.ChangeDstt("Pauri")
# print(shivam.dstt)
# # print(atul.dstt)

# class Seniours(Student):
#     def __init__(self, Sname, Sage, Sdept,language):
#         super().__init__(Sname, Sage,Sdept)
#         self.language=language
        
#     def Info(self,string):
#         return f"Hi {self.name} You are From {string} your Language {self.language}"
        
        

# Nammi=Seniours("Navmmi",29,"EXC",{
#     1:"C",
#     2:"C++",
#     3:"Javascript",
#     4:"Python"
# })
# Nammi.ChangeDstt("UdhamSingh Nagar")
# print(Nammi.Info("Gholtir"))

# print(shivam.age)
# # print(Seniours.Std)


# class a():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# class b():
#     def __init__(self,dept):
#         self.dept=dept
#     def __init__(self, name, age,dept):
#         a.__init__(self,name, age)
#         b.__init__(self,dept)




# emp1=c("shivam",26,"IT")
# print(emp1.name,emp1.age,emp1.dept)


tt=open('mytext.txt','a')
print(tt.read())
