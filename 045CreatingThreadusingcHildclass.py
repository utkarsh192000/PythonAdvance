
from threading import Thread

class Mythread(Thread):
    def run(self):
        print("Run Method")
        for i in range(5):
            print("Child Thread")

t=Mythread()
print(t.name)
t.start()
for i in range(5):
    print("Main Thread")