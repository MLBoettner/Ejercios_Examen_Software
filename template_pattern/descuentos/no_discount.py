from template_pattern.descuentos.base_discount import BaseDiscount

class NoDiscount(BaseDiscount):
    def apply_discount(self, amount):
        print("Sin aplicar descuentos...")
        return amount