import hashlib
# Rtrams
# smart
# Splkiyoanr
# lion

email = 'jkr@gmail.com'
pwd = 'ChairOnTableWith3Legs'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = 'jkr@gmail.com'
your_password = '2329e22c9a4de221abeabaf22b72c7fc'

hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()
if email == your_email and pwd_hash == hashed_your_password:
    print('right user')
else:
    print('wrong password')

hacker_email = 'jkr@gmail.com'
hacker_password = '2329e22c9a4de221abeabaf22b72c7fc'

print(pwd)
print(pwd_hash)