import unittest
from context.order_context import Order
from states.pending_state import PendingState
from states.approved_state import ApprovedState
from states.shipped_state import ShippedState


class TestOrderStates(unittest.TestCase):

    def test_initial_state_is_pending(self):
        """Verifica que una nueva orden comience en estado Pendiente."""
        order = Order()
        self.assertIsInstance(order.state, PendingState)
        self.assertEqual(order.state.status(), "Pendiente")

    def test_transition_pending_to_approved(self):
        """Pendiente → Aprobado"""
        order = Order()
        order.next_state()
        self.assertIsInstance(order.state, ApprovedState)
        self.assertEqual(order.state.status(), "Aprobado")

    def test_transition_approved_to_shipped(self):
        """Aprobado → Enviado"""
        order = Order()
        order.next_state()  # Pendiente → Aprobado
        order.next_state()  # Aprobado → Enviado
        self.assertIsInstance(order.state, ShippedState)
        self.assertEqual(order.state.status(), "Enviado")

    def test_transition_back_from_shipped_to_approved(self):
        """Enviado → Aprobado"""
        order = Order()
        order.next_state()  # Pendiente → Aprobado
        order.next_state()  # Aprobado → Enviado
        order.previous_state()  # Enviado → Aprobado
        self.assertIsInstance(order.state, ApprovedState)
        self.assertEqual(order.state.status(), "Aprobado")

    def test_invalid_previous_from_pending(self):
        """Pendiente no tiene estado anterior (no cambia)."""
        order = Order()
        order.previous_state()  # No debería cambiar
        self.assertIsInstance(order.state, PendingState)
        self.assertEqual(order.state.status(), "Pendiente")


if __name__ == "__main__":
    unittest.main()