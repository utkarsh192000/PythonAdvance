#  writeline is same as write but it can accept list, tuple


f=open('student.txt',"a")
lst1=["rahul","exam","india"]
f.writelines(lst1)
f.close()
print("Success")

