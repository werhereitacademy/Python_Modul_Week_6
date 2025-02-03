# class car:
#     def __init__(self,speed=100):
#         self.__speed = speed
#     def set_speed(self, speed):
#         if speed >= 0 :
#             self.__speed = speed
#         else:
#             print("Hatalı hız")
    
#     def get_speed(self):
#         return self.__speed
    
#  araba = car(100)
#  print(araba.get_speed())
"""--------------------------------------"""
# class BankAccount:
#     def __init__(self, amaunt = 0):
#         self.__blance = amaunt
    
#     def deposit(self, amaunt=0):
#         self.__blance += amaunt
    
#     def withdraw(self, amount=0):
#         if amount > self.__blance:
#             print("Not Enough Balance")
#             return False
#         self.__blance -= amount
#         return True
    
#     def get_balance(self):
#         return self.__blance

# hesap = BankAccount(1000)
# hesap.deposit(500)
# print(hesap.get_balance())
# hesap.withdraw(300)
# print(hesap.get_balance())
"""--------------------------------------"""
# class Employee:
#     def __init__(self):
#         self.__salary = 0
    
#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self, salary):
#         if salary < 0 :
#             print("Salary is not less 0")
#         else:
#             self.__salary = salary

# kisi = Employee()
# kisi.set_salary(2000)
# print(kisi.get_salary())
"""--------------------------------------"""
# class Annimal:
#     def __init__(self):
#         pass
    
#     def speak(self):
#         raise "Hatalı fonksiyon"

# class Dog(Annimal):
#     def __init__(self):
#         self.__sound = "Hav"
        
#     def speak(self):
#         return self.__sound

# class Cat(Annimal):
#     def __init__(self):
#         self.__sound = "Miyav"

#     def speak(self):
#         return self.__sound

# def sound(animal):
#     print(animal.speak())

# dog1= Dog()
# cat1= Cat()

# sound(dog1)
# sound(cat1)
"""--------------------------------------"""
# class Shape:
#     def __init__(self):
#         pass
    
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius = 1):
#         self.__radius = radius
    
#     def area(self):
#         return (self.__radius ** 2) * 3.14

#     def set_radius(self,radius):
#         self.__radius = radius

# class Square(Shape):
#     def __init__(self,side = 1):
#         self.__side = side

#     def area(self):
#         return (self.__side ** 2) 

# def display_area(shape):
#     return shape.area()

# daire = Circle(3)
# kare = Square(5)

# print(display_area(daire))
# print(display_area(kare))
"""--------------------------------------"""
# class MathOperations:
#     def __init__(self):
#         pass

#     @staticmethod
#     def add_numbers(a,b):
#         return a+b

# print(MathOperations.add_numbers(10,8))
"""--------------------------------------"""
# class Account:
#     def __init__(self):
#         pass
#     @staticmethod
#     def greet_user(name):
#         return "Selam "+name

# print(Account.greet_user("Musafa"))
"""--------------------------------------"""

# class Circle:
#     def __init__(self,radius=1):
#         self.__radius = radius
#     def area(self):
#         return 3.14 * self.__radius**2
#     @classmethod
#     def create_unit_circle(cls):
#         obj = Circle()
#         return obj

# cobj = Circle.create_unit_circle()
# print(cobj.area())

# class Rectangle:
#     def __init__(self,height, width):
#         self.__height = height
#         self.__width = width
    
#     @property
#     def width(self):
#         return self.__width * self.__height
#     @width.setter
#     def set_width(self, width):
#         self.__width = width

#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def set_height(self, height):
#         self.__height = height
    
#     @property
#     def area(self):
#         return self.__height * self.__width

# obj = Rectangle(2,1)
# print(obj.area)
# obj.height = 3
# obj.width = 5
# print(obj.area)
        

        
