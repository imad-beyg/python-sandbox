# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


#  Init user object
imad = User('Imad Beyg', 'imad.beyg@gmail.com', 37)
# Init customer object
sami = Customer('Sami Beyg', 'sami.beyg@gmail.com', 25)

sami.set_balance(500)
print(sami.greeting())

imad.has_birthday()
print(imad.greeting())
