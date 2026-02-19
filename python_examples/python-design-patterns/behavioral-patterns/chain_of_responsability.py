"""
Purpose: Pass a request along a chain of handlers.

Pros:
- Reduces coupling between sender and receiver.
- More flexible than hard coding request handling.

Cons:
- No guarantee request will be handled.
- Can be hard to debug due to chain length.

When to use:
- When multiple objects can handle a request.
"""

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if 0 < request <= 10:
            return f"Handler1 handled {request}"
        else:
            return super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if 10 < request <= 20:
            return f"Handler2 handled {request}"
        else:
            return super().handle(request)

handler_chain = ConcreteHandler1(ConcreteHandler2())
print(handler_chain.handle(5))
print(handler_chain.handle(15))
print(handler_chain.handle(25))
# Output:
# Handler1 handled 5
# Handler2 handled 15
# None
