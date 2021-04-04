#  MULTILEVEL INHERITANCE 
#  GRANDCHILD class can access all the feature of its father and grandfather along with its own property


# class Father():
#     def show(self):
#         print("Father Class Instance Method")

# class Son(Father):
#     def disp(self):
#         print("Son Class Instance Method")


# class GrandSon(Son):
#     def view(self):
#         print("GrandSon Class Instance Method")


# g=GrandSon()
# g.show()   # accessing the feature of father
# g.view()   ## accessing the feature of itself
# g.disp()   # accessing the feature of Son



#  EXAMPLE ALONG WITH CONSTRUCTOR

class Father():
    def __init__(self):
        # self.money=m
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        # self.money=m
        print("Son Class Constructor")

    def disp(self):
        print("Son Class Instance Method")


class GrandSon(Son):

    def __init__(self):
        # self.money=m
        super().__init__()
        print("GrandSon Class Constructor")

    def view(self):
        print("GrandSon Class Instance Method")


g=GrandSon()
g.show()   # accessing the feature of father
g.view()   ## accessing the feature of itself
g.disp()   # accessing the feature of Son


#  Grandson gives priority to its own constructor , but we can use super method
#  Granson when uses super then it calls the its own father  constructor
#  so its means that if any child wants to call father contructor , it should have superr in its  constructor