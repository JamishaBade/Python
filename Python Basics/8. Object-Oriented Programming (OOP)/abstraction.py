from abc import ABC, abstractmethod


# Abstract class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # we don’t define how, just that it must exist


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")


# Using the classes
payment1 = CreditCardPayment()
payment1.pay(100)  # Paid $100 using Credit Card.

payment2 = PayPalPayment()
payment2.pay(50)  # Paid $50 using PayPal.
