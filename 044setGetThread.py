

from threading import Thread,current_thread


def disp():
    print("Child Thread Object Name",current_thread().getName())
    current_thread().setName("Doc Thread")
    print("Child new Thread Object Name",current_thread().getName())


t1=Thread(target=disp)
t2=Thread(target=disp)
t1.start()
t2.start()

print("Main Thread",current_thread().getName())
current_thread().setName("Geeky Thread")   # seeting our own name to threda