def calculator():
    x=int(input('Enter the First Number'))
    y=int(input('Enter the Second Number'))
    print("Enter 1 for Add\nEnter 2 for Substraction\nEnter 3 For Division\nEnter 4 For multification")
    option=int(input('Enter the Number'))
    def add():
        res=x+y
        print(res)
    def substraction():
        res=x-y
        print(res)
    def devide():
        res=x/y
        print(res)
    def multiply():
        res=x*y
        print(res)
    if option==1:
        add()
    
    elif option==2:
        substraction()
    
    elif option==3:
        devide()
    
    if option==4:
        multiply()
    
calculator()

