class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})
    
    def checkout(self, amount):
        price = 0
        for item in self.cart:
            print(item)
            price += item['price'] * item['quantity']
        if amount < price:
            return f'Please give me more money: {price - amount}'
        elif amount > price: 
            return f'Here are the items and extra money: {amount - price}'
        else:
            return 'Here are the items'


shopping = Shopper('Bag Tan')
shopping.add_to_cart('shirt', 400, 3)
shopping.add_to_cart('shoes', 899, 4)
shopping.add_to_cart('pant', 1400, 2)

reply = shopping.checkout(8000)
print(reply)
