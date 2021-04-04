#  if more than one mehod of same name is defined inside the same class . then it is method overloading
# There is no such method overloading in python , but we can achhieve it somehow
#  if same method perform different task , then in python it is called as method overloading
# 

# class MyClass:
#     def sum(self,a):
#         print("Ist sum method",a)

#     def sum(self):
#         print("2nd sum method")
    
# obj=MyClass()
# obj.sum()
# obj.sum(10)   # this also goes to the 2nd method , since it is written later


# METHOD OVERLOADING

class MyClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            s="Provide atleast 2 no."
        return s

    # def sum(self):
    #     print("2nd sum method")
    
obj=MyClass()
print(obj.sum(10))   # we want make it such that we can send as much as argument we want, it will perform differnt operation in same method using
