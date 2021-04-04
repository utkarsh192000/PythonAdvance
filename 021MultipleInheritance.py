#  Multiple inheritance when there are multiple Parents of the child class



# class Father():
#     def showF(self):
#         print("Father Class Instance Method")

# class Mother():
#     def showM(self):
#         print("Mother Class Instance Method")
        

# class Son(Father,Mother):   # it has inherited from 2 parents , there is priority from left to right
#     def showS(self):
#         print("Son Class Instance Method")

# s=Son()
# s.showS()
# s.showF()
# s.showM()




# Complex using Constructor

class Father():
    def __init__(self):
        super().__init__() 
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Mother():
    def __init__(self):
        super().__init__() 
        print("Mother Class Constructor")
    def showM(self):
        print("Mother Class Instance Method")
        

class Son(Father,Mother):
    def __init__(self):
        super().__init__()   # it has 2 parents , father constructor would be called beacuse it has high priority
        print("Son Class Constructor")   # it has inherited from 2 parents , there is priority from left to right
    def showS(self):
        print("Son Class Instance Method")

s=Son()
s.showS()
s.showF()
s.showM()
