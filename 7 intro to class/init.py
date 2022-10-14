class Phone:
    
    manufactured = 'china'

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def send_sms(self, number, text):
        sms = f' sending: {text} to {number}'
        return sms

my_phone = Phone('Oppo', 13000, 'blue')
print(my_phone.brand, my_phone.manufactured)

her_phone = Phone('iPhone', 85000, 'purple')
print(her_phone.brand, her_phone.manufactured)

dad_phone = Phone('Nokia', 7000, 'black')
print(my_phone.price, her_phone.price, dad_phone.price)
print(my_phone.manufactured, her_phone.manufactured, dad_phone.manufactured)