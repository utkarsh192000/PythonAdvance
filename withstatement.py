#  with statement need not to close the file

with open('student.txt','r') as f:
    data=f.read()
    print(data)
    print(f.closed)