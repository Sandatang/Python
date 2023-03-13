class Person(object):
    def __init__(self,lastname:str,firstname:str)->None:
        self.lastname = lastname
        self.firstname = firstname
    def __str__(self)->str:
            return f"{self.lastname} {self.firstname}"

class Student(Person):
    def __init__(self,idno:str,lastname:str,firstname:str,course:str,level:str)->None:
        super().__init__(lastname,firstname)
        self.idno=idno
        self.course=course
        self.level=level
    
    def __str__(self)->str:
        return f"{self.idno} {super().__str__()} {self.course} {self.level}"

    def __eq__(self,idno)->bool:
        return self.idno == idno
