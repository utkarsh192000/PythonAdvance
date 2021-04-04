#  In method overriding the child class would not inherit the method of same name as it has .
#  method is overridden in the child class

# class Add:
#     def results(self,a,b):
#         print("Addition: ",a+b)
    
# class Multi(Add):
#     def results(self,a,b):
#         print("Multiplication : ",a*b)

# m=Multi()
# m.results(20,10) # resluts of Child class is called , priority is given to the child class method , if it is not present , then parent method is used



class Add:
    def results(self,x,y):
        print("Addition: ",x+y)
    
class Multi(Add):
    def results(self,a,b):
        super().results(10,20)  # this helps us to call the parent method results
        print("Multiplication : ",a*b)

m=Multi()
m.results(20,10) 