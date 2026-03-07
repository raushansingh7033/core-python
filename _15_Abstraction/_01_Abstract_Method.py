
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Area of Rectangle")


class Circle(Shape):

    def area(self):
        print("Area of Circle")


r = Rectangle()
r.area()