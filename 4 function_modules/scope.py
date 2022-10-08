balance = 580

def total_cost(price, quantity):
    global balance
    cost = price * quantity
    # balance = 100
    # remaining = balance - cost
    # balance = remaining
    balance = balance - cost
    # print(remaining)
    return cost

print(f'balance: outside before: {balance}')

pay = total_cost(10, 3)
print(f' please pay: {pay}')

print(f'balance: outside after: {balance}')