
''' if only father has the constructor then it can be accessed by the child but if the Child class also 
has the constructor then it can only access its own construcor , not his fathers'''


class Father():
    def __init__(self):
        self.money=1000
        print("Father Class Constructor",self.money)

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        self.money=5000
        print("Son Class Constructor",self.money)

    def disp(self):
        print("Son Class Instance Method")

s=Son()
print(s.money)
s.show()   # Child class can acesss the instance method of Parent

# Child Class constructor overrides the parent Class constructor