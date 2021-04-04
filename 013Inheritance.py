# SINGLE Inheritance

class Father:
    money=1000

    def show(self):
        print("Parent Class Instance Method")
    
    @classmethod
    def showmoney(cls):
        print("Parent class Method:",cls.money)

    @staticmethod
    def stat():
        a=10
        print("Parent class static class",a)

class Son(Father):
    def disp(self):
        print("Child class Instance Method")

s=Son()
s.disp() # calling method of child class Son
s.show() # we can also call the paret Father class members (method or variable) since Son is child class of Father
s.showmoney()
s.stat()

print()


f=Father()
f.show()
f.showmoney()
f.stat()
# f.disp()  # this would give error , because child can inherit the the prperty of father but father cannot have property of child