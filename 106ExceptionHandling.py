#  This would not give error
# a=10
# b=5
# d=a/b
# print(d)
# print("Rest Of the code")



# a=10
# b=0 
# try:
# # this would give error 0 division error, but we want our program to work
#     d=a/b
#     print(d)
#     print("Rest Of the code")
# except ZeroDivisionError:
#     print("Zero divison not allowed")
# else:
#     print("I will be only executed if except is not there")
# finally:
#     print("I will always be executed")


# a=10
# b=0 
# try:
# # this would give error 0 division error, but we want our program to work
#     d=a/g
#     print(d)
#     print("Rest Of the code")
# except ZeroDivisionError:
#     print("Zero divison not allowed")
# except NameError as obj:
#     print(obj)
# else:
#     print("I will be only executed if except is not there")
# finally:
#     print("I will always be executed")




# a=10
# b=0 
# try:
# # this would give error 0 division error, but we want our program to work
#     d=a/b
#     print(d)
#     print("Rest Of the code")
# except( NameError, ZeroDivisionError) as obj:   # it will catch whichever error is there
#     print(obj)
# else:
#     print("I will be only executed if except is not there")
# finally:
#     print("I will always be executed")



a=10
b=0 
try:
# this would give error 0 division error, but we want our program to work
    d=a/g
    print(d)
    print("Rest Of the code")
except:   # if we dont know which error has arised
    print("There is some error")
else:
    print("I will be only executed if except is not there")
finally:
    print("I will always be executed")





























#  We should try to minimize the code written in the try , beacuse if the erro arise instantly the control is transferred to the except
#  else part execute only if the exception does not arises
#  There can be more than one exception in the code

