"""
Purpose: Define an interface for creating an object but let subclasses decide which class to instantiate.

Pros:
- Encapsulates object creation.
- Supports open/closed principle by allowing new types without changing client code.

Cons:
- Adds complexity with extra subclasses.
- Clients may need to understand the product hierarchy.

When to use:
- When a class can’t anticipate the class of objects it needs to create.
- To centralize and control complex creation logic.
"""
class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"

class Creator:
    def factory_method(self):
        return Product()

    def some_operation(self):
        product = self.factory_method()
        return product.operation()

class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProductA()

creator = ConcreteCreator()
print(creator.some_operation())
# Output: Result of ConcreteProductA
