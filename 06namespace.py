#  NAMESPACE

class Mobile:
    fp='yes' # class variable
    
    @classmethod    # class method
    def is_fp(cls):
        print("Finger Print: ",cls.fp)   # accessing class variable

realme=Mobile()  # creating object
redmi=Mobile()
geeky=Mobile()

print("class FP: ",Mobile.fp)  # acessing class variable ouside require classname.variavlemname
print("Realme: ",realme.fp)   # also acessed through object
print("redmi: ",redmi.fp)
print("geeky: ",geeky.fp)

print()
Mobile.fp="No"

print("class FP: ",Mobile.fp)  # acessing class variable ouside require classname.variavlemname
print("Realme: ",realme.fp)   # also acessed through object
print("redmi: ",redmi.fp)
print("geeky: ",geeky.fp)
print()
#  since it is class variable so the single copy is made for all the objects
#  also remember we have changed using Classname , then only the change is for everyone otherwise if accssed using object then only that value changes


realme.fp="Not working"
print("class FP: ",Mobile.fp)  # acessing class variable ouside require classname.variavlemname
print("Realme: ",realme.fp)   # also acessed through object
print("redmi: ",redmi.fp)
print("geeky: ",geeky.fp)