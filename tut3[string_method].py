from ast import Str


str="shivam"
# print(str[0:6])
# o/p hello 

# skip the 1 character
# print(str[0:5:2])
# op hlo 

# skip 2 charcter 
# print(str[0:8:3])
# op hlm

# print(str[0:])
# op hello my name is shivam

# print(str[:5])
# op hello

# print(str[0:12:1])
# op without escaping the caharacter 

# print(str[3::2])
# to uppercase 
# print(str.upper())

# to lower 
# str2="HELLO THIS IS SHIVAM"
# print(str2.lower())

# length of string 
# print(len(str))

# reverse the string 
# print(str[::-1])

# print(str[-4:-2])

# a="9".join(str)
# print(a)
# x=str.split(',')
# print(str[9])

# for i in range(0,len(str),2):
#     print(str[i])
# for i in range(0,len(str),3):
#     print(str[i])


print(str.endswith('shivam'))
print(str.count('j'))
print(str.find('m'))
print(str.replace('m','j'))
print(str)