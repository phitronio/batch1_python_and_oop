class Washing:
    '''Subsystem # 1'''
 
    def wash(self):
        print("Washing...")
 
 
class Rinsing:
    '''Subsystem # 2'''
 
    def rinse(self):
        print("Rinsing...")
 
 
class Spinning:
    '''Subsystem # 3'''
 
    def spin(self):
        print("Spinning...")

class Dryer:
    '''Subsystem # 4'''
    def dry(self):
        print('drying your clothes')


class Ironing:
    '''Subsystem # 5'''

    def iron(self):
        print('ironing your clothes by iron man')


class WashingMachine:
    '''Facade'''
 
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
        self.drying = Dryer()
        self.iron = Ironing()
 
    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
        self.drying.dry()
        self.iron.iron()


philips = WashingMachine()
philips.startWashing()