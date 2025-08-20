"""
Purpose: Access elements sequentially without exposing structure.

Pros:
- Uniform traversal interface.
- Simplifies container use.

Cons:
- Extra code complexity.

When to use:
- When hiding collection structure during iteration.
"""
class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.position = 0

    def has_next(self):
        return self.position < len(self.collection)

    def next(self):
        result = self.collection[self.position]
        self.position += 1
        return result

it = Iterator([1,2,3])
while it.has_next():
    print(it.next())
# Output:
# 1
# 2
# 3
