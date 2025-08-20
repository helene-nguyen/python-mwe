"""
Purpose: Encapsulate requests as objects for queuing/logging.

Pros:
- Supports undo/redo, task scheduling.
- Decouples invoker from action performer.

Cons:
- Many small classes.

When to use:
- Transactional or delayed operations.
"""
class Command:
    def execute(self):
        pass

class SimpleCommand(Command):
    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        print(f"Executing command with {self.payload}")

command = SimpleCommand("Task")
command.execute()
# Output: Executing command with Task
