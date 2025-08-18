#1)basic 
class Car:
    def __init__(self, brand, color):
        self.brand = brand   # Attribute
        self.color = color   # Attribute

    def display_info(self):  # Method
        print(f"Brand: {self.brand}, Color: {self.color}")

# Creating Objects
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.display_info()
car2.display_info()

#2) inheritance 

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):   # Overriding
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):   # Overriding
        print(f"{self.name} meows!")

dog = Dog("Tommy")
cat = Cat("Kitty")

dog.speak()
cat.speak()



#3) Polymorphism 
# Polymorphism means same function name behaves differently.
class Bird:
    def fly (self):
        print("bairds can fly")
class penguin(Bird):
    def fly (self):
        print("penguin can not fly")
bird = Bird()
penguin =penguin()

bird.fly()
penguin.fly()


# 4)Encapsulation (Data Hiding + Binding)
# Encapsulation means binding data and methods together. In Python,
#  we use _protected and __private to restrict access.
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance #private attribute

    def deposit (self,amount):
        self.__balance += amount

    def withdraw(self,amount):   
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
         return self.__balance

# Usage
account = BankAccount("Souvik", 5000)
account.deposit(2000)
print(account.get_balance())   # ✅ Allowed
# print(account.__balance)     # ❌ Error (private)


# 5)Abstraction (Hiding Details)
# Abstraction means showing essential features and hiding background details.
# We use abc module (Abstract Base Class).

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Class
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

# obj = Vehicle()  # ❌ Not allowed
car = Car()
car.start()
car.stop()
