#  Instance method without argument
class Mobile:

    def show_model(self):
        print("Realme X")


realme=Mobile()
realme.show_model()





#  Instance method with argument

class Mobile:
    def __init__(self):
        self.model="Realme X"   # instace variable


    def show_model(self,p):   # instance variable
        self.price=p
        print("Model:" ,self.model, "Price:" ,self.price)

realme=Mobile()
realme.show_model(1000)  # accessing using object.variablename with formal argument