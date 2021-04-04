# class Mobile:
#     def __init__(self):
#         print("Constructor is called")

# realme=Mobile()


# Ex2

class Mobile:
    def __init__(self,m,v=80): # here v is default parament
        self.model=m
        self.volume=v

    def show_model(self,p):
        self.price=p
        print("Model:" ,self.model, "Price:" ,self.price)
        print("Volume :",self.volume)

# passing argument to the constructor
realme=Mobile('Realme X',50)   # 50 is formal argument

#  accessing method from outside the class
realme.show_model(1000)

realme=Mobile('Redmi 7 s')
realme.show_model(2000)
