"""
Entities should be open for extension but closed for modification.

Example: Add new payment types without modifying the existing Payment class.
"""
class Payment:
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        print("Paying with card")

class PaypalPayment(Payment):
    def pay(self):
        print("Paying with PayPal")

# ====================== Anti pattern ===============================================================
class Payment:
    """
    Problem:
    Each new payment type forces changes to this method, risking bugs and breaking existing behavior.
    """
    def pay(self, payment_type):
        if payment_type == 'card':
            print("Paying by card")
        elif payment_type == 'paypal':
            print("Paying via PayPal")
        # Adding a new payment requires modifying this method