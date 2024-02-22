class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

# Example usage:
rectangle = Shape(5, 4)
area = rectangle.calculate_area()
print("Area of the rectangle:", area)