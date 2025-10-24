# factura/factura_A.py
from .base_factura import BaseFactura

class FacturaA(BaseFactura):
    """
    Factura A: responsable inscripto, con IVA.
    """

    def validar_datos(self):
        print("Validando datos para Factura A...")
        self._leer_json()
        tipo = self.data.get("tipo")
        if tipo != "responsable_inscripto":
            raise ValueError("El cliente no corresponde al tipo Factura A.")
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
        print(f"Generando Factura A para {self.data['cliente']}")
        print(f"TOTAL FINAL (IVA + descuentos): ${total:.2f}")
        return total  # permite que la API devuelva el total