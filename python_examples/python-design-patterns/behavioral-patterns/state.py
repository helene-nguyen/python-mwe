"""
Purpose: Allow an object to change its behavior when its internal state changes.

Pros:
- Localizes state-specific behavior.
- Simplifies complex conditionals.

Cons:
- Can increase number of classes.

When to use:
- When an object’s behavior depends on its state.
"""
class State:
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("State A handles request.")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        print("State B handles request.")
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

context = Context(ConcreteStateA())
context.request()
context.request()
# Output:
# State A handles request.
# State B handles request.
