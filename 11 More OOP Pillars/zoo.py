from abc import ABC, abstractmethod

# abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    @property
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def move(self):
        print('moving around in the zoo')

class Monkey(Animal):
    def __init__(self):
        self.__name = 'monkey'
    def sing(self):
        print('monkey is signing')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self):
        print('eating banana')
    
    def move(self):
        print('hanging on the branches of the trees')
        super().move()


class Tiger(Animal):
    def eat(self):
        pass
    def move(self):
        pass

layka = Monkey()
print(layka)
layka.eat()
layka.move()
layka.name = 'moonkey'
print(layka.name)

