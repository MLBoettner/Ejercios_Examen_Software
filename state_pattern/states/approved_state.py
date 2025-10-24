from .base_state import OrderState

class ApprovedState(OrderState):
    def next(self, order):
        from .shipped_state import ShippedState
        print("Pasando de Aprobado a Enviado...")
        order.state = ShippedState()

    def prev(self, order):
        from .pending_state import PendingState
        print("Revirtiendo de Aprobado a Pendiente...")
        order.state = PendingState()

    def status(self):
        return "Aprobado"