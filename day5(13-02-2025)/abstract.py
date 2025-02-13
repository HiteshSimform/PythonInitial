from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(Computer):
    # def process(self):
    #     return super().process()
    def process(self):
        print("it's running")

# com = Computer()
# com.process()

com1=laptop()
com1.process()


# from abc import ABC, abstractmethod

# Abstract class representing a generic payment method
class PaymentMethod(ABC):
    
    # Abstract method to process payment, no implementation here
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    # Concrete method common for all payment methods
    def payment_success(self):
        print("Payment processed successfully.")

# Subclass representing CreditCard payment
class CreditCard(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of {amount} dollars...")
        # Additional logic specific to Credit Card processing
        self.payment_success()

# Subclass representing PayPal payment
class PayPal(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} dollars...")
        # Additional logic specific to PayPal processing
        self.payment_success()

# Subclass representing Bitcoin payment
class Bitcoin(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of {amount} BTC...")
        # Additional logic specific to Bitcoin processing
        self.payment_success()

# Now using the classes in the system
def process_transaction(payment_method: PaymentMethod, amount):
    payment_method.process_payment(amount)

# Testing with different payment methods
credit_card = CreditCard()
paypal = PayPal()
bitcoin = Bitcoin()

process_transaction(credit_card, 100)  # Using CreditCard
process_transaction(paypal, 200)  # Using PayPal
process_transaction(bitcoin, 0.5)  # Using Bitcoin
