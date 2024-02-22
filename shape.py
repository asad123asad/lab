import math

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)  # For circle, we'll consider length and width as radius
    
    # Getter method for radius
    def get_radius(self):
        return self.length
    
    # Setter method for radius
    def set_radius(self, radius):
        self.length = radius
        self.width = radius
    
    # Overriding calculate_area method for circle
    def calculate_area(self):
        return math.pi * self.length * self.length  # Area of circle = π * r^2

# Example usage:
rectangle = Rectangle(5, 4)
area_rectangle = rectangle.calculate_area()
print("Area of the rectangle:", area_rectangle)

circle = Circle(3)
area_circle = circle.calculate_area()
print("Area of the circle:", area_circle)

# Testing getter and setter for circle radius
print("Radius of the circle:", circle.get_radius())
circle.set_radius(5)
print("New radius of the circle:", circle.get_radius())
