from .base_tax import BaseTax

class SinIVA(BaseTax):
    def apply_tax(self, amount):
        print("Factura exenta de IVA...")
        return amount