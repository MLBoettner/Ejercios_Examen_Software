from context.order_context import Order

if __name__ == "__main__":
    order = Order()
    
    order.previous_state()
    order.current_status()
    order.next_state()      # Pendiente → Aprobado
    order.current_status()
    order.next_state()      # Aprobado → Enviado
    order.current_status()
    order.previous_state()      # Enviado → Aprobado
    order.current_status()