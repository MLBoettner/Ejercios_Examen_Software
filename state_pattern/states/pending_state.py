from .base_state import OrderState

class PendingState(OrderState):
    def next(self, order):
        from .approved_state import ApprovedState
        print("Pasando de Pendiente a Aprobado...")
        order.state = ApprovedState()

    def prev(self, order):
        print("La orden aún está pendiente, no hay estado anterior.")

    def status(self):
        return "Pendiente"