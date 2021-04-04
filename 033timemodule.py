from time import *


epoch=time()
print(epoch)

et=ctime(epoch)
print(et)

print(ctime())


stobj=localtime()
print(stobj)
print(stobj.tm_mday)
print(stobj.tm_mon)
print(stobj.tm_year)
print(stobj.tm_hour)
print(stobj.tm_min)
print(stobj.tm_sec)