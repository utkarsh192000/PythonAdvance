#  CLASS Method without argument

class Mobile:
    
    @classmethod    # decorator   # class method
    def show_model(cls):
        print("Realme X")   # accessing class variable

realme=Mobile()  # creating object
Mobile.show_model()  # calling class method




#  Class method using Formal parameter
class Mobile:
    fp='yes' # class variable
    
    @classmethod    # class method
    def show_model(cls,r):
        cls.ram=r # accessing class variable
        print(cls.fp,cls.ram)

realme=Mobile()  # creating object
Mobile.show_model("4gb")