# 1. classes
# class is a blue_print for creating new objects.
# An object is an instance of a class.
# class : Human
# objects : John , Mary , Jack


# 2.Creating classes
# class MyPoint  ---> Pascal naming concvention
'''
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
'''


# 3. Constructor ---> magic method
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()
'''

# 4. Class vs Instance attributes


'''

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()
point.z = 10

another = Point(3, 4)
print(another.default_color)
another.draw()

print(point.x)
point.draw()

'''

# 5. class vs Instance Methods
#  @class method --> define a method at class level

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point {(self.x) , (self.y)}")


point = Point(0, 0)
point.draw()
point = Point.zero()
point.draw()
'''


# 6. Magic methods
# using the str function we can get the same result as a
# point object
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x} , {self.y})"  # we can use return

    def draw(self):
        print(f"Point ({self.x} , {self.y}")


point = Point(1, 2)
print(str(point))
'''

# 7. Comparing Objects

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
# print(point == other)
print(point > other)
'''

# 8. Performing Arithmetic Operations
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
other = Point(10, 20)
combined = point + other
print(combined.x)
'''

# 9. Making Custom containers

'''
class TagCloud:
    def __init__(self):
        self.tags = {}  # Initializing tags attribute to an empty dictionary

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
# we can only read we cannot set any value to implement we use the below magic method after getitem
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
'''

# 10. Private Members
'''

class TagCloud:
    def __init__(self):
        self.__tags = {}  # Initializing tags attribute to an empty dictionary

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)
'''

'''
cloud = TagCloud()
print(cloud.__tags)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags["PYTHON"])
'''
'''
cloud = TagCloud()
print(cloud.__dict__)
print(cloud._TagCloud__tags)
'''

# 11. Properties

# Solution 1 ----> ugly unpythonic it's not using
# language or features to its full potential.
# This kind of code is written by a java programmer learning python code


'''

class Product:
    def __init__(self, price):
        self.setprice(price)
        # self.__price = price

    def getprice(self):
        return self.__price

    def setprice(self, value):
        if value < 0:
            raise ValueError("price caanot be negative")
        self.__price = value


product = Product(-50)
'''
# Solution2 --->
# A PROPERTY is an object that sits infront of an attribute
# and allows us to get or set that value of the attribute

'''
class Product:
    def __init__(self, price):
        self.price = price
        # self.setprice(price)
        # self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value

    price = property(getprice, setprice)


product = Product(10)
# product.price = -1
print(product.price)

'''

# 12. Inheritance

'''
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")
 # Animal : Parent, base class
 # Mammal : Child, Sub class


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
'''

# 13. The Object Class

'''
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
o = object
print(issubclass(Mammal, object))
'''

# 14. Method overriding

'''
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # 
        print("Mammal Constructor")
        self.weight = 2


m = Mammal()
print(m.age)
print(m.weight)
'''

# 15.Multi-level Inheritance

'''
class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass

'''
# 16. Multiple Inheritance

'''
class Employee:
    def greet(self):
        print("Employee greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()
'''

# 17. A good example of Inheritance
''' 
 
class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")        
'''

# 18. Abstract Base Classes


'''

from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

# stream = Stream()
# stream.open()
# stream = MemoryStream()
# stream.open()

'''

# 19. Polymorphism
