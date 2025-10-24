from abc import ABC, abstractmethod

class BaseDiscount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass