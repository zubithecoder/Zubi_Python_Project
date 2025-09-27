# Introduction to Object-Oriented Programming (OOP)
"""
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. OOP promotes modularity, reusability and maintainability through four main principles:
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
This document explores each concept with detailed explanations and multiple Python examples.
"""
# 1. Encapsulation
"""
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. It restricts direct access to some of an object's components, which is achieved using access modifiers like private attributes (denoted by __ double underscores in Python).
"""
# 1.1. Key Features of Encapsulation:
"""
• Data Hiding: Protects object integrity by preventing external modification.
• Access Control: Uses getters and setters to manage attribute access.
"""
# 1.2. Example 1: Bank Account
"""
This example demonstrates encapsulation by restricting direct access to the balance attribute.
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f" Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        return "Invalid withdrawal amount."
        
    def get_balance(self):
        return f"Balance: {self.__balance}"

# Testing the Bankaccount class
account = BankAccount("Shehroz", 1000)
print(account.deposit(500))  # Deposited 500. New balance: 1500
print(account.withdraw(200))  # Withdrew 200. New balance: 1300
print(account.get_balance())  # Balance: 1300
# print ( account . __balance ) # AttributeError : ’BankAccount ’ has no attribute ’__balance ’ 
#         (Listing 1: Bank Account with Encapsulation)
# Output:
# Deposited 500. New balance: 1500
# Withdrew 200. New balance: 1300
# Balance: 1300

# 1.3. Example 2: Employee Management
"""
This example uses encapsulation to manage employee details securely.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # Private attribute

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            return f"Salary update to {self.__salary}"
        return "Invalid salary."

    def get_salary(self):
        return f"Salary: {self.__salary}"

# Testing the Employee class
emp = Employee("Waleed", 50000)
print(emp.get_salary())    # Salary: 50000
print(emp.set_salary(60000))    # Salary update to 60000
print(emp.get_salary())    # Salary: 60000
# emp.__salary = 1000   # Does not affect the private attribute
#         (Listing 2: Employee Class with Encapsulation)
# Output:
# Salary: 50000
# Salary update to 60000
# Salary: 60000

# 2. Abstraction
"""
Abstraction hides complex implementation details and exposes only the necessary features of an object. In Python, abstraction is often achieved using abstract base classes (ABCs) from the abc module.
"""
# 2.1. Key Features of Abstraction:
"""
• Simplification: Reduces complexity by showing only essentials features.
• Interface Definition: Defines a contract for subclasses to implement.
"""
# 2.2. Example 1: Shape Abstraction 
"""
This example uses an abstract class to define a shape interface.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Testing the Shape classes
rect = (Rectangle(4, 5))
circle = Circle(3)
print(f"Rectangle Area: {rect.area()}")    # Rectangle Area: 20
print(f"Rectangle Perimeter: {rect.perimeter()}")    # Rectangle Perimeter: 18
print(f"Circle Area: {circle.area()}")    # Circle Area: 28.27431
print(f"Circle Perimeter: {circle.perimeter()}")    # Circle Perimeter: 18.84954
#         (Listing 3: Abstract Shape Class)
# Output:
# Rectangle Area: 20
# Rectangle Perimeter: 18
# Circle Area: 28.27431
# Circle Perimeter: 18.84954

# 2.3. Example 2: Payment System
"""
This example abstracts different payment methods.
"""
# 2.3. Example 2: Payment System
"""
This example abstracts different payment methods.
"""
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass 

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

# Testing the Payment classes
cc = CreditCardPayment()
pp = PayPalPayment()
print(cc.process_payment(100))  # Output: Processing credit card payment of $100
print(pp.process_payment(50))  # Output: Processing PayPal payment of $50
#         (Listing 4: Abstract Payment Class)
# Output:
# Processing credit card payment of $100
# Processing PayPal payment of $50

# 3. Inheritance
"""
Inheritance allows a class (child) to inherit attributes and methods from another class (parent), promoting code reuse and hierarchical relationships.
"""
# 3.1. Key Features of Inheritance
"""
• Code Reusability: Child classes reuse parents class functionally.
• Extensibility: Child classes can extend or override parent methods.
"""
# 3.2. Example 1: Vehicle Hierarchy
"""
This example shows a vehicle class hierarchy.
"""
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.brand} {self.model} engine started"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start_engine(self):
        return f"{self.brand} {self.model} car with {self.doors} doors engine started"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return f"{self.brand} {self.model} motorcycle {'with' if self.has_sidecar else 'without'} sidecar engine started"

# Testing the Vehicle classes
car = Car("Toyota", "Camry", 4)
moto = Motorcycle("Hayley", "Davidson", False)
print(car.start_engine())    # Toyota Camry car with 4 doors engine started
print(moto.start_engine())    # Harley Davidson motorcycle without sidecar engine started
#         (Listing 5: Vehicle Class Hierarchy)
# Output:
# Toyota Camry car with 4 engine started
# Harley Davidson motorcycle without sidecar engine started

# 3.3. Example 2: Animal Hierarchy
"""
This example demonstrates inheritance with animals.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Testing the Animal classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())    # Buddy barks
print(cat.speak())    # Whiskers meows
#         (Listing 6: Animal Class Hierarchy)
# Output:
# Buddy barks
# Whiskers meows

# 4. Polymorphism
"""
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is achieved through method overriding or method overloading (simulated in Python via default arguments).
"""
# 4.1. Key Features of Polymorphism
"""
• Flexibility: Same interface for different data types.
• Extensibility: New classes can be added without modifying existing code.
"""
# 4.2. Example 1: Polymorphic Shapes
"""
This example uses polymorphism to calculate areas.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    print(f"Area: {shape.area()}")

# Testing Polymorphism
square = Square(4)
triangle = Triangle(3, 6)
print_area(square)    # Area: 16
print_area(triangle)  # Area: 9.0
#         (Listing 7: Polymorphic Shape Processing)
# Output:
# Area: 16
# Area: 9.0

# 4.3. Example 2: Polymorphic Media Players
"""
This example shows polymorphism in media playback.
"""
class MediaPlayer:
    def play(self):
        return "Playing media"

class AudioPlayer(MediaPlayer):
    def play(self):
        return "Playing audio"

class VideoPlayer(MediaPlayer):
    def play(self):
        return "Playing video"

def start_playback(player):
    print(player.play())

# Testing polymorphism
audio = AudioPlayer()
video = VideoPlayer()
start_playback(audio)    # Playing audio
start_playback(video)    # Playing video
#         (Listing 8: Polymorphic Media Player)
# Output:
# Playing audio
# Playing video

# 5. Conclusion
"""
OOP in Python provides a powerful way to structure code using Encapsulation, Abstraction, Inheritance, and Polymorphism. These principles enable developers to create modular, reusable, and maintainable software. The examples provided demonstrate practical applications of each concept, helping students understand their implementation in Python.
"""

print("-----------------------")

