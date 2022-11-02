from unicodedata import name


class School:
    def __init__(self,name) -> None:
        self.schoolName = name
    def say_name(self):
        print(f"Hello I am {self.schoolName}")
    def __repr__(self) -> str:
        return f"School({self.schoolName})"
    
class Teacher:
    def __init__(self,name) -> None:
        self.teacherName = name
    def say_name(self):
        print(f"Hello I am {self.teacherName}")
    def __repr__(self) -> str:
        return f"Teacher({self.teacherName})"
    
class Student(Teacher,School):
    def __init__(self,name,teacherName,schoolName) -> None:
        Teacher.__init__(self,teacherName)
        School.__init__(self,schoolName)
        self.studentName = name
    def say_name(self):
        print(f"Hello I am {self.studentName}")
    def __repr__(self) -> str:
        return f"Student({self.studentName})"
    
student = Student("Rakib","Ms Rahima","Trust School")
student.say_name()