from threading import Thread

def dis():
    print("Starting Threads")
    for i in range(50):
        print(i)
t=Thread(target=dis)
t.start()


def dis2():
    print("\nSecond thread Start")
    for i in range(40):
        print("======")

t1=Thread(target=dis2)
t1.start()

def dis3():
    print("\n Third thread Start ")
    for x in range(40):
        print("\n*\n")
t2=Thread(target=dis3)
t2.start()