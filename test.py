# import re

# # tp=['a','b','c','d']
# # print(tp[0:3])
# txt = "The rain in Spain"
# x = re.search("^the.*Spain$", txt)
# if x:
#     print("Yes We have Matched")

# else:

#     print("Sorry We dont Have that kind of word")

import threading 

def des0():
    print("0 threading")
    for i in range (10):
        print(i)
text=threading.Thread(target=des0)
text.start()
def dis():
    print("This is Threding 1")
tex1=threading.Thread(target=dis)
tex1.start()

