"""
Purpose: Allow incompatible interfaces to work together.

Pros:
- Reuse legacy or unrelated code.
- Separation between client and incompatible classes.

Cons:
- Can increase complexity with many adapters.

When to use:
- Integrating third-party or legacy systems.
- For incompatible interfaces collaboration.
"""
class Target:
    def request(self):
        return "Target: default behavior"

class Adaptee:
    def specific_request(self):
        return "Adaptee: specific behavior"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

adapter = Adapter(Adaptee())
print(adapter.request())
# Output: Adaptee: specific behavior
