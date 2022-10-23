class Student:
    def __init__(self, name, id, marks) -> None:
        self._name = name
        self.__id = id
        self.marks = marks
    
    @property
    def student_id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


chowdhury = Student('choto chowdhury', 15, 55)

print(chowdhury.student_id)
# chowdhury.student_id = 77
print(chowdhury.student_id)
print(chowdhury.name)

del chowdhury.name

print(dir(chowdhury))