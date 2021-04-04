
# tell() about the beginning of file pointer

f=open('student.txt','r')
print(f.tell())
d=f.read(5)
print(d)
print(f.tell()) # since we have just read 5 character , therefore our pointer is at 5 currently

d2=f.read(5)
print(d2)

print(f.tell())


#  seek() moves the file pointer from 1 point to another pointer

d3=f.seek(3)
print(f.read())
print(f.tell())
print(d3)
