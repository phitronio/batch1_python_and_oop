def add(a, b):
    sum = a + b
    print(sum)

def deduct(x, y):
    result = x - y
    return result 


class Phone:
    color = 'black'
    features = ['camera', 'water proof', 'can be used as a hammer']

    def call(self):
        print('ring ring ring')
    
    def send_sms(self, number, text):
        sms = f'sending sms: {text} to: {number}'
        return sms

my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01717225544', 'I missed to miss you')
print(sms)