from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        return 0
        
        
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
class square(shape):
  
    def __init__(self,side):
        self.side=side
        super().__init__()
    def area(self):
        return self.side*self.side




rect1=rectangle(10,20)
print(rect1.area())
rect2=square(8)
print(rect2.area())