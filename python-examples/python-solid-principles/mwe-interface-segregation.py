"""
Prefer many specific interfaces over a single general-purpose interface.

Example: Instead of one big Device interface, create specific ones.
"""
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class AllInOnePrinterScanner(Printer, Scanner):
    pass

# ====================== Anti pattern ===============================================================
class Device:
    """
    Problem:
    The printer is forced to implement scan() which it does not support.
    """
    def print(self):
        pass

    def scan(self):
        pass

class Printer(Device):
    def print(self):
        print("Printing")

    def scan(self):
        raise NotImplementedError("Printer cannot scan")
