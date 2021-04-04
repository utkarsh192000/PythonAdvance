#  INSTANCE VARIABLE

class Mobile:
    def __init__(self): # here v is default parament
        self.model="Realme X"

    def show_model(self):
        print(self.model)

realme=Mobile() 
redmi=Mobile()
geek=Mobile()

print(realme.model)
print(redmi.model)
print(geek.model)
print()

redmi.model="Remdi 7s"

print(realme.model)
print(redmi.model)
print(geek.model)
print()


# STATIC VARIABLE
#  SINGLE COPY IS made for all instance , any modifiaction would refelct in other too

class Mobile:
    fp="Yes"  # static variable ,class variable
    def __init__(self): # here v is default parament
        self.model="Realme X"

    def show_model(self):
        print(self.model)

    @classmethod
    def is_fp(cls):   # to access class variable @ and cls id used
        print(cls.fp)  # to acess we need cls.variablename

realme=Mobile()
realme.show_model() # calling instance method 
Mobile.is_fp() # calling class method
print()
Mobile.fp="No"
Mobile.is_fp()

# realme=Mobile()
# redmi=Mobile()
# geek=Mobile()

# print(realme.model)
# print(redmi.model)
# print(geek.model)
# print()





#  EX 3
