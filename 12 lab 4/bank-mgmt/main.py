""" Manages Bank Account """

class Account:
    accID = 1

    def __init__(self, name, age, nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        # update acc id
        self.account_id = Account.accID
        Account.accID += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc_1 = Account('Minhaj', 63, 600, 500)
acc_2 = Account('Kona', 62, 500, 1000)

# print(" 1st one ", acc_1.account_id)
# print(" 2nd one ",acc_2.account_id)

print("Deposit")
acc_1.deposit(2000)
acc_2.deposit(200)
print("acc 1", acc_1.balance)
print("acc 2", acc_2.balance)

print("Withdraw")
acc_1.withdraw(100)
acc_2.withdraw(300)
print("acc 1", acc_1.balance)
print("acc 2", acc_2.balance)