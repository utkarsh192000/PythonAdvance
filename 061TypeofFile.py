#  text mode , r, it is treated as string whereas in binary mode , rb , it is simply read


f=open('student.txt',mode='w')
f.write("Hello\n")
f.write("Geeky\n")
f.write("How are you\n")
f.close()
print("Writing successful")

f=open('student.txt',mode='r')
data=f.read()
print(data)
f.close()

f=open('student.txt',mode='rb')
data=f.read()
print(data)
f.close()