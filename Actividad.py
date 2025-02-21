from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class PayPalPayment(Payment):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def process_payment(self):
        print(f"Processing PayPal payment for {self.email}")

class CreditCardPayment(Payment):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def process_payment(self):
        print(f"Processing Credit Card payment for card {self.card_number}")

class PaymentSystem:
    def __init__(self):
        self.payment_method: Payment = None

    def set_payment_method(self, payment_method: Payment):
        self.payment_method = payment_method

    def make_payment(self):
        if self.payment_method:
            self.payment_method.process_payment()
        else:
            print("No payment method selected.")

if __name__ == "__main__":
    system = PaymentSystem()
    
    paypal = PayPalPayment("user@example.com", "securepassword")
    system.set_payment_method(paypal)
    system.make_payment()
    
    # Cambiando a Tarjeta de Crédito
    credit_card = CreditCardPayment("1234-5678-9012-3456", "123")
    system.set_payment_method(credit_card)
    system.make_payment()
