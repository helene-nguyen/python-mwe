"""
Purpose: Use sharing to support many fine-grained objects efficiently.

Pros:
- Saves memory by sharing common data.
- Improves performance with large numbers of objects.

Cons:
- Can make code more complex.
- Intrinsic vs extrinsic state must be managed carefully.

When to use:
- When many similar objects are needed.
"""
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Shared: {self.shared_state}, Unique: {unique_state}")

class FlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

factory = FlyweightFactory()
fw1 = factory.get_flyweight("A")
fw1.operation("X")
fw2 = factory.get_flyweight("A")
print(fw1 is fw2)
# Output:
# Shared: A, Unique: X
# True
