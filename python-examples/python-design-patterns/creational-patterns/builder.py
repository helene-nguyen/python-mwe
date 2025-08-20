"""
Purpose: Separate construction of a complex object from its representation.

Pros:
- Allows step-by-step construction.
- Supports building different representations with the same process.

Cons:
- Can lead to many small builder classes.

When to use:
- For constructing complex objects with many optional parts.
"""
class House:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

class Builder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add("Walls")

    def build_roof(self):
        self.house.add("Roof")

    def get_result(self):
        return self.house

builder = Builder()
builder.build_walls()
builder.build_roof()
house = builder.get_result()
print(house.parts)
# Output: ['Walls', 'Roof']
