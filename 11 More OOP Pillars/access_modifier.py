# public protected private
class Account:
    def __init__(self, holder) -> None:
        self._account_holder = holder
    

class StudentAccount(Account):
    def __init__(self, holder, balance, school):
        self.__balance = balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'No money for you'
        self.__balance -= amount
        return amount

    def deposit(self, amount):
        if amount < 0:
            return 'Negative amount can not be added'
        self.__balance += amount

    def get_balance(self):
        return self.__balance

nas = StudentAccount('Nas Daily', 12000, 'Nas Academy')

# nas.__balance = 890000
nas.deposit(50000)
nas.deposit(15000)
print(nas.get_balance())

# print(dir(nas))
# print(nas.__balance)
# print(nas._StudentAccount__balance)