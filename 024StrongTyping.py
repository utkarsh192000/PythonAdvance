

# Strong  Typing 
# hasattr(object,attribute)
# Returns true or false

class Duck:
    def walk(self):
        print("Tapak Tapak")

class Horse:
    def walk(self):
        print("Tabdak")

class Cat:
    def talk(self):
        print("Mew mew")

def myfunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()

d=Duck()
myfunction(d)



h=Horse()
myfunction(h)

c=Cat()
myfunction(c)
#  This would give an error as there is no such attribute as obj.talk(), but it this case we have used has hasattr , we will not get error