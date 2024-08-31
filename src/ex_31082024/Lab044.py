# class and objects
# Create a class
# Person with attributes like name, age, and address.
# Create objects of the Person class and assign values to their attributes.


class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address


# p1 = Person('Kamlesh',23,'Hola')
# print(f'Name:{p1.name} , age:{p1.age} , address:{p1.address}')


#Encapsulation
# Create a class
# BankAccount with private attributes accountNumber and balance.
# Provide public methods to deposit and withdraw money.

class BankAccount:
    def __init__(self , number):
        self.__accountNumber = number
        self.__amount = 0

    def deposit(self,money):
        self.__amount+=money

    def withdraw(self,money):
        try:
            if self.__amount<money:
                raise ValueError
            else:
                self.__amount+=money
        except ValueError:
            print('Insufficient balance')

    def check_balance(self):
        print(f'Current balance is {self.__amount}')


# a1 = BankAccount(1234)
# a1.deposit(200)
# a1.check_balance()
# a1.withdraw(100)
# a1.check_balance()
# a1.withdraw(1000)


# Inheritance:
#
#     Create a base class Animal with methods eat() and sleep().
#     Create derived classes Dog, Cat, and Bird that inherit from Animal and override the eat() method.


class Animal:
    def eat(self):
        pass

    def sleep(self):
        print('sleeping')

class Dog(Animal):
    def eat(self):
        print('Dog is eating')

class Cat(Animal):
    def eat(self):
        print('Cat is Eating')

class Bird(Animal):
    def eat(self):
        print('Bird is eating')

# d1 = Dog()
# d1.eat()
# c1 = Cat()
# c1.eat()
# b1= Bird()
# b1.eat()

# Polymorphism:
#
#     Create a base class Shape with a method calculateArea().
#     Create derived classes Circle, Rectangle, and Triangle that implement the
#     calculateArea() method differently.

PI = 3.14
class Shape:
    def calculateArea(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculateArea(self):
        return PI*(self.radius)**2


class Rectangle(Shape):
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def calculateArea(self):
        return self.length*self.breadth


class Triangle(Shape):
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def calculateArea(self):
        return 1/2 * self.base * self.height


# c1 = Circle(10)
# r1 = Rectangle(2,3)
# t1 = Triangle(3,4)
# print(f'Area is :{c1.calculateArea()}')
# print(f'Area is :{r1.calculateArea()}')
# print(f'Area is :{t1.calculateArea()}')


# Abstraction:
#
#     Create an abstract class Vehicle with abstract methods start() and stop().
#     Create concrete classes Car, Bike, and Truck that implement the abstract methods.


from abc import ABC , abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print('Car started ')

    def stop(self):
        print('Car stopped')

class Bike(Vehicle):
    def start(self):
        print('Bike started')

    def stop(self):
        print('Bike stopped')

class Truck(Vehicle):
    def start(self):
        print('Truck started')

    def stop(self):
        print('Truck stopped')

# c1 = Car()
# c1.start()
# c1.stop()
# b1 = Bike()
# b1.start()
# b1.stop()
# t1 = Truck()
# t1.start()
# t1.stop()


# Method Overloading:
#
#     Create a class
#
# Calculator with overloaded methods add() that can take different numbers of arguments
# (e.g., add(int, int), add(int, int, int)).


class Calculator:
    def add(self,*args)->int:
        return sum(map(int,args))



# c1 = Calculator()
# print(c1.add(20,23))
# print(c1.add(12,14,23))

# Method Overriding:
#
#     Create a base class Shape with a method draw().
#     Create derived classes Circle,
# Rectangle, and Triangle that override the draw() method to draw their respective shapes.


class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('Drawing circle')

class Rectangle(Shape):
    def draw(self):
        print('Drawing Rectangle')

class Triangle(Shape):
    def draw(self):
        print('Drawing Triangle')



# Interface Implementation:
#
#     Create an interface Drawable with a method draw().
#     Create classes Circle, Rectangle, and Triangle that implement the Drawable interface.

class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print('drawing circle')

class Rectangle(Drawable):
    def draw(self):
        print('drawing Rectangle')


class Triangle(Drawable):
    def draw(self):
        print('Drawing Triangle')

# Circle().draw()
# Rectangle().draw()
# Triangle().draw()
#


# Exception Handling:
#
#     Create a class Division with a method divide()
#     that throws an exception if the divisor is zero.


class Division:

    @staticmethod
    def divide(num1,num2):
        try:
            if num2>0:
                return num1/num2
            elif num2==0:
                raise ZeroDivisionError
            else:
                return num1/num2
        except ZeroDivisionError:
            print('0 provided')
            return 0


# print(f'Dividing the values : {Division().divide(10,20)}')
# print(f'Dividing the values : {Division().divide(10,0)}')
# print(f'Dividing the values : {Division().divide(10,-1)}')
# print(f'Dividing the values : {Division().divide(289,2)}')


# Generics:
#
#     Create a generic class Pair that can store two elements of any type.

from typing import Generic , TypeVar
T= TypeVar('T')

class Pair(Generic[T]):
    def __init__(self, item1:T,item2:T):
        self.item1 = item1
        self.item2 = item2

    def get_item(self):
        return self.item1,self.item2

# p1 = Pair(10,20)
# print(p1.get_item())
# p2 = Pair('Hello','Kamlesh')
# print(p2.get_item())
# p3 = Pair('Kittu',10)
# print(p3.get_item())