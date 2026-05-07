class Shape:
    """
    A base class representing a generic geometric shape.
    """
    def area(self):
        """
        Returns a placeholder string for the area.
        Subclasses are expected to implement their specific area calculation.
        """
        return "Shape area (maybe unknown). "


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    Calculates its area based on width and height.
    """
    def __init__(self, width: int, height: int):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle,
        prefixed by the base class area message.
        """
        return super().area() + "Rectangle area: " + str(self.width * self.height)


class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    Calculates its area based on the radius.
    """
    def __init__(self, radius: int):
        """
        Initializes a Circle object.

        Args:
            radius (int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return "Circle area: " + str(3.14 * self.radius ** 2)


def print_area(shape: Shape):
    """
    Takes a Shape object and prints the result of its area() method.

    Args:
        shape (Shape): An instance of the Shape class or its subclasses.
    """
    print("shape.area(): " + str(shape.area()))


# --- Usage Example ---
# Create an instance of the base Shape class
shape1 = Shape()
print_area(shape1)

# Create an instance of the Rectangle class
rectangle = Rectangle(4, 5)
print_area(rectangle)

# Create an instance of the Circle class
circle = Circle(3)
print_area(circle)