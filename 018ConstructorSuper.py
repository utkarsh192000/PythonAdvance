# Super Method helps Child class to call the constructor of its parent even after declaring its own constructor


# class Father():
#     def __init__(self):
#         self.money=1000
#         print("Father Class Constructor",self.money)

#     def show(self):
#         print("Father Class Instance Method")

# class Son(Father):
#     def __init__(self):
#         super().__init__()   # this would call the parent class constructor
#         self.money=5000
#         print("Son Class Constructor",self.money)

#     def disp(self):
#         print("Son Class Instance Method")

# s=Son()
# s.disp()  # calling child instance method





class Father():
    def __init__(self,m):
        self.money=m
        print("Father Class Constructor",self.money)

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)   # this would call the parent class constructor
        # self.money=5000
        self.job=j
        print("Son Class Constructor",self.money, self.job)

    def disp(self):
        print("Son Class Instance Method")

s=Son(1000,"Python")
s.disp()  # calling child instance method



