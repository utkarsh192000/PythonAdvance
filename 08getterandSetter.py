# getter method 



class Mobile:
    def __init__(self):
        self.model="Realme X"   # instace variable


    def get_model(self):   # gettermethod
        return self.model

realme=Mobile()
m=realme.get_model() 
print(m) 




# setter method 



class Mobile:
    def __init__(self):
        self.model="Realme X"   # instace variable


    def set_model(self):   # gettermethod
        self.model="Redmi 7pro"
        return self.model

realme=Mobile()
m=realme.set_model() 
print(m) 