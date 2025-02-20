# Description: Open/Closed Principle
from abc import ABC, abstractmethod


class PaymentProccesor(ABC):
    # En python no existen los metodos privados, pero se puede simular con __
    # si cambio el nombre de calculate a __calculate, no seria sobre escrito en las clases hijas
    # por lo que lo mantengo con el mismo nombre para cumplir con el principio OCP
    @abstractmethod
    def calculate(self, amount):
        return amount

class VIPDiscount(PaymentProccesor):
    def calculate(self, amount):
        return amount * 0.5

class NoDiscount(PaymentProccesor):
    def calculate(self, amount):
        return amount