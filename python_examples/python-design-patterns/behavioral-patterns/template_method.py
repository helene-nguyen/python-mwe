"""
Purpose: Define the skeleton of an algorithm deferring some steps to subclasses.

Pros:
- Promotes code reuse.
- Controls steps of algorithm.

Cons:
- Requires subclassing.
- Harder to modify algorithm structure.

When to use:
- When algorithm structure is fixed but steps vary.
"""

class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.required_operations2()
        self.hook()

    def base_operation1(self):
        print("Base operation 1")

    def base_operation2(self):
        print("Base operation 2")

    def required_operations1(self):
        pass

    def required_operations2(self):
        pass

    def hook(self):
        pass

class ConcreteClass(AbstractClass):
    def required_operations1(self):
        print("Concrete operation 1")

    def required_operations2(self):
        print("Concrete operation 2")

    def hook(self):
        print("Hook method")

concrete = ConcreteClass()
concrete.template_method()
# Output:
# Base operation 1
# Concrete operation 1
# Base operation 2
# Concrete operation 2
# Hook method
