#region --Controller Componets--
class Person:
    def __init__(self,lastname,firstname):
        self.lastname = lastname
        self.firstname = firstname
    def getLastname(self):
        return self.lastname
    def getFirstname(self):
        return self.firstname

class Student(Person):
    def __init__(self, **kwargs):
        kwarg = list(kwargs.values())
        super().__init__(kwarg[1],kwarg[2])
        self.idno = kwarg[0]
        self.course = kwarg[3]
        self.level = kwarg[4]
        self.header_str = ','.join(kwargs.keys())

    def getHeader(self):
        return self.header_str

    def getStudentDATA(self):
        return dict(idno=self.idno,lastname=self.lastname,firstname=self.firstname,course=self.course,level=self.level)

    def check_DATA(self):
        data:list = [self.getStudentDATA()]
        return True if "" not in data else False
#endregion
