"""
High-level modules should not depend on low-level modules, both should depend on abstractions.

Ex: A OrderManager class depends on a PaymentService interface, not a concrete implementation.
"""
from abc import ABC, abstractmethod

class PaymentService(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PaypalService(PaymentService):
    def pay(self, amount):
        print(f"Paying {amount} with PayPal")

class OrderManager:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def make_payment(self, amount):
        self.payment_service.pay(amount)

# Usage
service = PaypalService()
manager = OrderManager(service)
manager.make_payment(100)

# ====================== Anti pattern ===============================================================
class Paypal:
    """
    Problem:
    OrderManager directly depends on a concrete implementation (Paypal), making the code rigid and less flexible.
    """
    def pay(self, amount):
        print(f"Paying {amount} via PayPal")

class OrderManager:
    def __init__(self):
        self.paypal = Paypal()

    def make_payment(self, amount):
        self.paypal.pay(amount)
