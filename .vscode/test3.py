import datetime
# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age



# obj1=Employee("Ankit",26)

# class dancer(Employee):
#     def __init__(self, name, age,dance):
#         super().__init__(name, age)
#         self.dance=dance

# obj2=dancer("shivam",26,"Hiphop")
# print(obj2.dance)

# print(obj1.name)
        

# today_day = datetime.datetime.today().strftime("%d")
# today_month = datetime.datetime.today().strftime("%m")
# today_year = datetime.datetime.today().strftime("%Y")
# print(today_day)
# print(today_month)
# print(today_year)

# import logging
# import threading
# import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     # x.join()
#     logging.info("Main    : all done")

from threading import Thread

def dis():
    print("Starting Threads")
    for i in range(50):
        print(i)
t=Thread(target=dis)
t.start()


def dis2():
    print("\nSecond thread Start")

t1=Thread(target=dis2)
t1.start()

def dis3():
    print("\n Third thread Start ")
    for x in range(40):
        print("\n*\n")
t2=Thread(target=dis3)
t2.start()