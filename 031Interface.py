#  if there is no concrte method in abstractclass then it is interface in python



from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

 

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Definig Absctract method")

c=Child()
c.disp()
