
from threading import Thread

class MyExam():
    def solve_questions(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Question 1 solved")
    def q2(self):
        print("Question 2 solved")
    def q3(self):
        print("Question 3 solved")

myee=MyExam()
t=Thread(target=myee.solve_questions)
t.start()