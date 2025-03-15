import abc
from math import pi
class Shape(abc.ABC):
    @abc.abstractmethod
    def calculate_square(self):
        pass
    @abc.abstractmethod
    def calculate_volume(self):
        pass
class Square(Shape):
    def __init__(self, a):
        self.a = a
    def calculate_square(self):
        print(self.a * self.a)
    def calculate_volume(self):
        print("Это 2Д фигура")
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def calculate_square(self):
        print(self.r * self.r * pi)

    def calculate_volume(self):
        print("Это 2Д фигура")

class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def calculate_square(self):
        print(self.a * self.h / 2)

    def calculate_volume(self):
        print("Это 2Д фигура")
class Cube(Shape):
    def __init__(self, a):
        self.a = a
    def calculate_square(self):
        print("Это 3Д фигура")
    def calculate_volume(self):
        print(self.a * self.a * self.a)
class Ball(Shape):
    def __init__(self, r):
        self.r = r
    def calculate_square(self):
        print("Это 3Д фигура")

    def calculate_volume(self):
        print((4/3) * pi * self.r * self.r * self.r)
class Piramide(Shape):
    def __init__(self, s, h):
        self.s = s
        self.h = h
    def calculate_square(self):
        print("Это 3Д фигура")

    def calculate_volume(self):
        print((1/3) * self.s * self.h)
