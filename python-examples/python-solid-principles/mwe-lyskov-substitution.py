"""
Derived classes must be substitutable for their base classes without altering program behavior.

Example:A subclass Square should be able to replace the Rectangle class without issues.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# ====================== Anti pattern ===============================================================
class Rectangle:
    """
    Problem:
    Square cannot be substituted without breaking expectations about Rectangle behavior (inconsistent state).
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # Forces height to be equal

    def set_height(self, height):
        self.width = height
        self.height = height