"""
Purpose: Attach additional responsibilities to an object dynamically.

Pros:
- Adds functionality without subclassing.
- More flexible than static inheritance.

Cons:
- Can result in many small classes.
- Can complicate debugging.

When to use:
- To extend behavior of objects dynamically.
- When subclassing would create too many variations.
"""
class Component:
    def operation(self):
        return "Component"

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return f"Decorator({self.component.operation()})"

component = Component()
decorated = Decorator(component)
print(decorated.operation())
# Output: Decorator(Component)
