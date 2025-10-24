# factura/factura_B.py
from template_pattern.factura.base_factura import BaseFactura

class FacturaB(BaseFactura):
    """
    Factura B: consumidor final, sin IVA.
    """

    def validar_datos(self):
        print("Validando datos para Factura B...")
        self._leer_json()
        tipo = self.data.get("tipo")
        if tipo != "consumidor_final":
            raise ValueError("El cliente no corresponde al tipo Factura B.")
        print(f"Cliente: {self.data['cliente']} - Tipo: {tipo}")

    def calcular_subtotal(self):
        print("Calculando subtotal desde archivo JSON...")
        subtotal = 0.0
        for p in self.data["productos"]:
            linea = p["cantidad"] * p["precio_unitario"]
            subtotal += linea
            print(f"  {p['descripcion']}: {p['cantidad']} x ${p['precio_unitario']} = ${linea}")
        print(f"Subtotal total: ${subtotal}")
        return subtotal

    def exportar_factura(self, total):
        print(f"Generando Factura B para {self.data['cliente']}")
        print(f"TOTAL FINAL (sin IVA, con descuento): ${total:.2f}")
        return total  