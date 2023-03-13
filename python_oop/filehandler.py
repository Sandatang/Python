from Oop import Student
filename = 'test.txt'

def saveit(student:list):
    with open(filename, 'a') as f:
        for i in student:
            k =[i.idno,i.lastname,i.firstname,i.course,i.level]
            f.write(k.__str__())
            f.write("\n")

def loadlist():
    with open(filename, 'r') as f:
        k=[]
        for i in f.readlines():
            o = i.strip().split(',')
            k.append(o)
        f.flush()
        return k

def delete(idno):
    lines=[]
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename,'w') as f:
        for line in lines:
            if idno not in line:
                f.write(line.__str__())
