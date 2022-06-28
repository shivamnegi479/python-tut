class Student:
    vill="kothagi"
    age=28
shivam=Student()
shivam.name="shivam"
atul=Student()
atul.city="dubai"
Student.vill="Gholtir"
atul.vill="Kothagi"
atul.age=27
print(atul.vill)
print(shivam.vill)
print(shivam.age)

print(atul.__dict__)