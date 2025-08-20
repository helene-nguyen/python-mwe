"""
Purpose: Provide a placeholder to control access to another object.

Pros:
- Control over access (security, lazy loading).
- Can add logging or caching transparently.

Cons:
- Adds layers complicating debugging or performance.

When to use:
- For lazy initialization or access control.
"""
class Subject:
    def request(self):
        return "Real subject"

class Proxy:
    def __init__(self):
        self.subject = Subject()

    def request(self):
        return self.subject.request()

proxy = Proxy()
print(proxy.request())
# Output: Real subject
