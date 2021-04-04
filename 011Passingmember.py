#  PASSING MEMBER FROM ONE CLASS TO ANOTHER CLASS


class Student:
    # Constructor
    def __init__(self,n,r):
        self.name=n  # they are the members of the class and we want to pass these memmbers to another class
        self.roll=r

    # Instance Method
    def disp(self):
        print("Student Name: ",self.name) 
        print("Student Roll: ",self.roll) 


class User:
    # Static Method
    @staticmethod
    def show(s):
        print("Username: ",s.name)
        print("roll no.: ",s.roll)

        s.disp()


# creating object of student class
stu=Student("Rahul",101)

User.show(stu)   # we want to pass all attributes of student to user Class using static method
