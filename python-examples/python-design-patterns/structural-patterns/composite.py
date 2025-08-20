"""
Purpose: Treat individual objects and compositions uniformly.

Pros:
- Simplifies clients with tree structures.
- Supports recursive object structures.

Cons:
- Can make design overly general and complex.

When to use:
- Tree structures like file systems or GUIs.
"""
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Branch({'+'.join(results)})"

leaf1 = Leaf()
leaf2 = Leaf()
branch = Composite()
branch.add(leaf1)
branch.add(leaf2)
print(branch.operation())
# Output: Branch(Leaf+Leaf)
