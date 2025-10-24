from .base_state import OrderState

class ShippedState(OrderState):
    def next(self, order):
        print("La orden ya fue enviada, no hay siguiente estado.")

    def prev(self, order):
        from .approved_state import ApprovedState
        print("Revirtiendo de Enviado a Aprobado...")
        order.state = ApprovedState()

    def status(self):
        return "Enviado"