#  thread class is in threading module 


#  without using own class

from threading import Thread

def disp(a):
    print("Child Thread")  # this is child thread

t=Thread(target=disp,args=(10,))

t.start()   # to check whether the thread is running or not

for i in range(5):
    print("Main Thread")


#  there are 2 threads in this program 1. main thread and child thread
