# dictionary are user to store data in key value pare  
# it dont allows duplicate 

# emp={
#     "name":"shivam",
#     "surname":"negi",
#     "dept":"IT"
# }
# print(emp.items())
# for i in emp:
#     print(i)


dict={
    "shivam":"mango",
    "atul":"guava",
    "sanju":"apple",
    "raji":{
        "b":"bhat",
        "lunch":"Roti",
        "dinner":"chawal"
    }
}
del dict["atul"]
print(dict["raji"]["lunch"])

# add item in dictionary 
dict["anki"]="food awesome"

print(dict["anki"])

# delet item from dictoray 

del dict["anki"]
print(dict)

# copy function 

dict2=dict.copy();
print(dict)