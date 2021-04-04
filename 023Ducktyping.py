

# Duck Typing 

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
    obj.walk()

d=Duck()
myfunction(d)
h=Horse()
myfunction(h)

c=Cat()
myfunction(c)
#  This would give an error as there is no such attribute as obj.talk()