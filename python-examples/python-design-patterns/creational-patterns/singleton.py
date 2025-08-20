"""
Purpose: Ensure a class has only one instance and provide a global access point.

Pros:
- Controlled access to a single instance.
- Reduced memory footprint for shared resources.

Cons:
- Can introduce global state, hurting testability.
- Violates single responsibility principle if overused.

When to use:
- Managing shared resources (e.g., configuration, logging) where only one instance is needed.
"""
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
# Output: True
