from abc import ABC, abstractmethod

class OrderState(ABC):
    """Clase base abstracta para los estados de la orden."""

    @abstractmethod
    def next(self, order):
        pass

    @abstractmethod
    def prev(self, order):
        pass

    @abstractmethod
    def status(self):
        pass