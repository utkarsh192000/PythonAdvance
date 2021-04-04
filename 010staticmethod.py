#  Static Method without argument

class Mobile:
    fp="Yes"
    @staticmethod    # decorator   # static method
    def show_model():
        print(Mobile.fp)   # accessing class variable

realme=Mobile()  # creating object
Mobile.show_model()  # calling static method




#  Static method using Formal parameter
class Mobile:
    fp="Hello"
    @staticmethod    # static method
    def show_model(r,p):
        ram=r
        price=p
        print(Mobile.fp,ram,price)

realme=Mobile()  # creating object
Mobile.show_model("4gb",1098)