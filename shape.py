import math

class Shape:
    def __init__(self):
        self.unit = "meters"
    
    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def display(self):
        print(f"Circle - Radius: {self.radius} {self.unit}")
        print(f"\t Area: {self.area()} {self.unit} squared") 
        print(f"\t Perimeter: {self.perimeter()} {self.unit}")     

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def display(self):
        print(f"Rectangle - Width: {self.width} {self.unit}, Height: {self.length} {self.unit}")
        print(f"\t Area: {self.area()} {self.unit} squared") 
        print(f"\t Perimeter: {self.perimeter()} {self.unit}")

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    circle.display()
    print("\n" + "-"*50 + "\n")
    rectangle.display()
