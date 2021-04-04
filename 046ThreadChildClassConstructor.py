

from threading import  *

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child Constructor ")   

    def run(self):
        pass

t=MyThread()
t.start()

print("Main Thread")