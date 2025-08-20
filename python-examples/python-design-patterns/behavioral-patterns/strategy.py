"""
Purpose: Encapsulate interchangeable algorithms.

Pros:
- Flexible and extensible behavior.
- Avoids conditional code.

Cons:
- Extra classes increase complexity.
- Clients aware of multiple strategies.

When to use:
- Multiple behaviors or algorithms interchangeable at runtime.
"""
class Strategy:
    def do_algorithm(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(data)

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.do_algorithm(data)

data = [1,5,3]
context = Context(ConcreteStrategyA())
print(list(context.execute(data)))
# Output: [1, 3, 5]
