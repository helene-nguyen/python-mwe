"""
Purpose: Create new objects by copying existing ones.

Pros:
- Efficient for complex objects.
- Reduces need for subclassing.

Cons:
- Careful cloning required.
- Issues with shallow vs deep copy.

When to use:
- When object creation is costly or complex.
- Many similar objects needed with slight differences.
"""
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Sheep(Prototype):
    def __init__(self, name):
        self.name = name

sheep1 = Sheep("Dolly")
sheep2 = sheep1.clone()
print(sheep2.name)
# Output: Dolly
