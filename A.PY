import math
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

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.sides = [side1, side2, side3]

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        return 0.5 * self.base * self.height

# Example usage
def print_shape_details(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}\n")

# Creating instances of different shapes
rectangle = Rectangle(5, 8)
square = Square(5)
circle = Circle(7)
triangle = Triangle(5, 12, 5, 12, 13)

# Printing details of each shape
print("Rectangle details:")
print_shape_details(rectangle)

print("Square details:")
print_shape_details(square)

print("Circle details:")
print_shape_details(circle)

print("Triangle details:")
print_shape_details(triangle)
