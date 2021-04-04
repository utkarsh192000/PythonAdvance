# If an operator performs more than function than it is called as operator overloading

# print(10+20)

# int.__add__(self,other)
# print(int.__add__(10,20))
# print(int.__sub__(20,10))
# print(str.__add__('Hello',' brother'))

# This methods are already written in the python , and they have been given certain symbol

class A:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x + other.x
    
class B:
    def __init__(self,x):
        self.x=x

a=A(100)
b=B(200)

print(a+b)   # this is same as A.__add__(a,b)

#  we have made a code to add two object
10+20
"Hello "+"World"
a+b