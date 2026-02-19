"""
Purpose: Capture and externalize an object’s internal state without violating encapsulation.

Pros:
- Enables undo/redo.
- Keeps encapsulation intact.

Cons:
- Can increase memory use.
- Complexity in managing mementos.

When to use:
- When state rollback or undo feature is needed.
"""
class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self, state):
        self.state = state

    def save(self):
        return Memento(self.state)

    def restore(self, memento):
        self.state = memento.state

originator = Originator("State1")
memento = originator.save()
originator.state = "State2"
originator.restore(memento)
print(originator.state)
# Output: State1
