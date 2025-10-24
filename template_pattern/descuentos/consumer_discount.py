# descuentos/consumer_discount.py
from template_pattern.descuentos.base_discount import BaseDiscount

class ConsumerDiscount(BaseDiscount):
    def apply_discount(self, amount):
        print("Aplicando descuento para consumidor final (5%)...")
        return amount * 0.95