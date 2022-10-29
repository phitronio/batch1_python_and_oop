import hashlib
from brta import BRTA

license_authority = BRTA()

class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, 'user created')
    
    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()

        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print('valid user')
            return True
        else:
            print('invalid user')
            return False
        # print('password found', stored_password)


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare

class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print('Sorry you failed, try again')
        else: 
            self.license = result
            self.valid_driver = True


    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination

    

hero = User('Hero Alom', 'hero@alom.com', 'heroOhHero')
hero.log_in('hero@alom.com', 'heroOhHero')

kuber = Driver('Kuber Maji', 'kuber@maji.com', 'kopilaJaisna', 54, 4556)

result = license_authority.validate_license(kuber.email, kuber.license)
print(result)
kuber.take_driving_test()
result = license_authority.validate_license(kuber.email, kuber.license)
print(result)
