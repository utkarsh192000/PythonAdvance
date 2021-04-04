class Army:   # Outer Class 
    def __init__(self):
        self.name="Rahul"
        self.gn=self.Gun()   # inner class object

    def show(self):
        print("Name: ",self.name)

    class Gun:   # inner class object
        def __init__(self):
            self.name="AK47"
            self.capacity="75 rounds"
            self.length=34.5

        def disp(self):
            print("Gun Name: ",self.name)
            print("Gun Capacity: ",self.capacity)
            print("Gun length: ",self.length)


a=Army()
a.show()

print(a.gn)
g=a.gn
print(g.name)
print(g.capacity)
print(g.length)
g.disp()

# g=Army().Gun()   # another way of setting g
