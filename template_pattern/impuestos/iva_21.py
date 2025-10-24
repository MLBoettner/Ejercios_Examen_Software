from template_pattern.impuestos.base_tax import BaseTax

class IVA21(BaseTax):
    def apply_tax(self, amount):
        print("Aplicando IVA del 21%...")
        return amount * 1.21