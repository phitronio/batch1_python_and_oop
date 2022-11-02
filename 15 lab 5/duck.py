from unicodedata import name

class School:
    def __init__(self,name) -> None:
        self.schoolName = name
    def say_hello(self):
        print("Hello from School")
class Teacher:
    def __init__(self,name) -> None:
        self.teacherName = name
    def say_hello(self):
        print(f"Hello from teacher") 
        
class Student:
    def __init__(self,name,obj) -> None:
        self.studentName = name
        obj.say_hello()
    
school = School("trust school")
teacher = Teacher("Solaiman sir") 
student = Student("Rakib",teacher)