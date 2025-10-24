from states.pending_state import PendingState

class Order:
    """Contexto que mantiene el estado actual y delega el comportamiento."""

    def __init__(self):
        self.state = PendingState()

    def next_state(self):
        self.state.next(self)

    def previous_state(self):
        self.state.prev(self)

    def current_status(self):
        print(f"Estado actual: {self.state.status()}")