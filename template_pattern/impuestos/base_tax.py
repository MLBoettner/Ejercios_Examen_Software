from abc import ABC, abstractmethod

class BaseTax(ABC):
    @abstractmethod
    def apply_tax(self, amount):
        pass