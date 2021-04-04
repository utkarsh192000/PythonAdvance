#  Constructor in Inheritance

class Father():
    def __init__(self,m):
        self.money=m
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def disp(self):
        print("Son Class Instance Method")

s=Son(2000)
s.show()
s.disp()
print(s.money)   # child class automatically inherit constructor from  parent
