# from threading import Thread

# def fun1():
#     print("This is first Thread")
#     for i in range (0,22,2):
#         print(i)

# t=Thread(target=fun1)
# t.start()

# def fun2():
#     print("This is Second Thread")

# t1=Thread(target=fun2)
# t1.start()


# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")

from hmac import digest


num = int(input("ENter the Number"))
temp=num
rev=0
while(num>0):
    deg=num%10
    rev=rev*10+deg
    num=num//10
if(temp==rev):
    print("palimdrom")
else:
    print("Not Palimdrom")