import re

# tp=['a','b','c','d']
# print(tp[0:3])
txt = "The rain in Spain"
x = re.search("^the.*Spain$", txt)
if x:
    print("Yes We have Matched")

else:

    print("Sorry We dont Have that kind of word")
