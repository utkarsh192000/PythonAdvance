


from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print('Concrete Method')

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Definig Absctract method")

c=Child()
c.disp()
c.show()


# PVM cannot create its object   obj=Father() would give error
#  abstract method function does not have statement
# concrete method is same as normal method
#  Child class is must for abstract class 
#  child class should have description of abstract method

#  Examle 2

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print("AK 47")

class Army(DefenceForce):
     def area(self):
        print("Land")
class Airforce(DefenceForce):
     def area(self):
        print("Sky")
class Navy(DefenceForce):
     def area(self):
        print("Water")

a=Army()
af=Airforce()
nv=Navy()

a.area()
af.area()
nv.area()
nv.gun()
nv.gun()
