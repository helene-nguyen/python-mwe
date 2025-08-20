"""
Purpose: Create families of related or dependent objects without specifying their concrete classes.

Pros:
- Guarantees compatibility among products.
- Isolates concrete classes from clients.

Cons:
- Increased complexity with multiple factories.
- Harder to introduce new product types.

When to use:
- Systems should be independent of how their products are created.
- Related objects must be used together consistently.
"""
class Chair:
    def has_legs(self):
        pass

class VictorianChair(Chair):
    def has_legs(self):
        return "Victorian chair legs"

class ModernChair(Chair):
    def has_legs(self):
        return "Modern chair legs"

class FurnitureFactory:
    def create_chair(self):
        pass

class VictorianFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

def client(factory):
    chair = factory.create_chair()
    print(chair.has_legs())

client(VictorianFactory())
client(ModernFactory())
# Output:
# Victorian chair legs
# Modern chair legs
