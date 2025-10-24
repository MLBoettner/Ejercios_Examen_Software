from template_pattern.descuentos.base_discount import BaseDiscount

class StudentDiscount(BaseDiscount):
    def apply_discount(self, amount):
        print("Aplicando descuento de estudiante (10%)...")
        return amount * 0.9