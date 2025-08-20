"""
Purpose: One-to-many dependency, observers update automatically.

Pros:
- Promotes loose coupling.
- Supports event-driven designs.

Cons:
- Risk of memory leaks if observers not detached.
- Notification order unpredictable.

When to use:
- Event handling, distributed systems.
"""
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

class Observer:
    def update(self, message):
        print(f"Observer: {message}")

subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify("Event occurred!")
# Output: Observer: Event occurred!
