# Abstract Class
class Book:
    def __init__(self, name) -> None:
        self.name = name

    def read(self):
        raise NotImplementedError

    def exercise(self):
        pass

class Physics (Book):
    def __init__(self, name) -> None:
        super().__init__(name)
    

topon = Physics('Shahjahan Topon rana Chowdhury')
# topon.read()
topon.exercise()