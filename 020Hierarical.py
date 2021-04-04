# # Whenever there are multiple childs of parent then , such inheritance is called as hierarical

# #  son and daughter both can use the property of father but not each others

# class Father():

#     def show(self):
#         print("Father Class Instance Method")

# class Son(Father):
#     def disp(self):
#         print("Son Class Instance Method")
        

# class Daughter(Father):
#     def view(self):
#         print("Daughter Class Instance Method")

# s=Son()
# s.disp()
# s.show()
# print()

# d=Daughter()
# d.view()
# d.show()

# # s.view()  This would give error because son cannot access the feature of daughter



#  Complex Example


class Father():
    def __init__(self):
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")

    def disp(self):
        print("Son Class Instance Method")


class Daughter(Father):

    def __init__(self):
        print("Daughter Class Constructor")

    def view(self):
        print("Daughter Class Instance Method")

s=Son()
d=Daughter()

#  both will give prority to their constructor , but they can use super as earlier to call constucor of father