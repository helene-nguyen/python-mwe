"""
Purpose: Decouple an abstraction from its implementation so the two can vary independently.

Pros:
- Increases flexibility by separating abstraction and implementation.
- Helps avoid permanent binding between abstraction and implementation.

Cons:
- Can increase complexity with many classes.

When to use:
- When you want to vary both abstraction and implementation independently.
"""
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x},{y} radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x},{y} radius {radius}")

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

circle1 = Circle(5, 10, 2, DrawingAPI1())
circle1.draw()
circle2 = Circle
