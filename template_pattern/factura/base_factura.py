# factura/base_factura.py
from abc import ABC, abstractmethod
import json

class BaseFactura(ABC):
    """
    Clase base que define el método plantilla (Template Method)
    para generar una factura completa a partir de un archivo JSON.
    """

    def __init__(self, json_path, discount_strategy, tax_strategy):
        self.json_path = json_path
        self.discount_strategy = discount_strategy
        self.tax_strategy = tax_strategy
        self.data = None  # acá se guardan los datos leídos

    # === MÉTODO PLANTILLA ===
    def generar_factura(self):
        """Define el flujo general del proceso"""
        self.validar_datos()
        subtotal = self.calcular_subtotal()
        subtotal_desc = self.discount_strategy.apply_discount(subtotal)
        total = self.tax_strategy.apply_tax(subtotal_desc)
        self.exportar_factura(total)
        self.notificar_cliente()
        return total 

    # === PASOS ABSTRACTOS ===
    @abstractmethod
    def validar_datos(self):
        pass

    @abstractmethod
    def calcular_subtotal(self):
        pass

    @abstractmethod
    def exportar_factura(self, total):
        pass

    # === PASO COMÚN ===
    def notificar_cliente(self):
        cliente = self.data.get("cliente", "Cliente no identificado") if self.data else "Desconocido"
        print(f"Factura generada y notificada a {cliente}.\n")

    # === UTILIDAD COMÚN ===
    def _leer_json(self):
        """Carga los datos desde el archivo JSON"""
        with open(self.json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)