# R+ simply means that we can read and then write without writing second time
#  w+ first writing then read
#  a+ is simply append and then read


# f=open('stu.txt','w+')

# data=f.read()
# f.write("GEEKYSHOWS")
# print(data)
# print(f.tell())



f=open('stu.txt','w+')
f.write("Youtube")
data=f.read()
print(data)   # currently pointer is at last
f.seek(2)
print(f.read())