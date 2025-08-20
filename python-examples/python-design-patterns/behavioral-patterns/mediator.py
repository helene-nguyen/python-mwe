"""
Purpose: Define an object that encapsulates how objects interact.

Pros:
- Reduces dependencies between communicating objects.
- Simplifies object protocols.

Cons:
- Mediator can become complex over time.

When to use:
- For complex communications between many objects.
"""

class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self.component1 = component1
        self.component2 = component2
        self.component1.mediator = self
        self.component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following:")
            self.component2.do_c()
        elif event == "B":
            print("Mediator reacts on B and triggers following:")
            self.component1.do_a()

class BaseComponent:
    def __init__(self, mediator=None):
        self.mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A")
        self.mediator.notify(self, "A")

class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C")
        self.mediator.notify(self, "B")

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)
c1.do_a()
# Output:
# Component 1 does A
# Mediator reacts on A and triggers following:
# Component 2 does C
