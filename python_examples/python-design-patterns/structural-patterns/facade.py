"""
Purpose: Provide a simplified interface to a complex subsystem.

Pros:
- Simplifies usage for clients.
- Decouples client from subsystem complexity.

Cons:
- May hide too much, limiting flexibility.

When to use:
- Simplify complex or legacy system interfaces.
"""
class SubsystemA:
    def operation_a(self):
        return "Subsystem A"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B"

class Facade:
    def __init__(self):
        self.subA = SubsystemA()
        self.subB = SubsystemB()

    def operation(self):
        return f"{self.subA.operation_a()} + {self.subB.operation_b()}"

facade = Facade()
print(facade.operation())
# Output: Subsystem A + Subsystem B
