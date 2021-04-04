
# EXAMPLE 1
# class Myclass():
#     def show(self):
#         print("I am Method ")

# x=Myclass()
# x.show()

# EX 2
# class Mobile:
#     def __init__(self):
#         self.model="Realme X"

#     def show_model(self):
#         print("Model:" ,self.model)

# realme=Mobile()

# # realme.show_model()
# # print(realme.model)
# realme.model="Realme Pro2"
# print(realme.model)
# realme.show_model()



# EX 3

class Mobile:
    def __init__(self,m):
        self.model=m

    def show_model(self,p):
        self.price=p
        print("Model:" ,self.model, "Price:" ,self.price)

realme=Mobile('Realme X')

# realme.show_model()
# print(realme.model)
# realme.model="Realme Pro2"
# print(realme.model)
realme.show_model(1000)

print(id(realme))
print()

realme=Mobile('Redmi 7s')
realme.show_model(1000)
print(id(realme))
print()


geeky=Mobile('Python')
# realme.show_model(1000)
print(id(realme))
print()

