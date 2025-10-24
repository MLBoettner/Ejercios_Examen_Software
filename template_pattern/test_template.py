# tests/test_facturacion.py
import os
import json
import unittest
from template_pattern.factura.factura_factory import crear_factura
from template_pattern.factura.factura_A import FacturaA
from template_pattern.factura.factura_B import FacturaB


class TestFacturacion(unittest.TestCase):

    def setUp(self):
        """Configura archivos JSON de prueba en memoria antes de cada test"""
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.temp_json = os.path.join(self.base_dir, "temp_test.json")

    def tearDown(self):
        """Elimina archivos temporales después de cada test"""
        if os.path.exists(self.temp_json):
            os.remove(self.temp_json)

    # ===========================================================
    # TEST 1: Factory Method crea la clase correcta
    # ===========================================================
    def test_factory_crea_factura_A(self):
        data = {
            "cliente": "Juan Pérez",
            "tipo": "responsable_inscripto",
            "productos": [
                {"descripcion": "Laptop", "cantidad": 1, "precio_unitario": 1000.0}
            ]
        }
        with open(self.temp_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        factura = crear_factura(self.temp_json, data["tipo"])
        self.assertIsInstance(factura, FacturaA)

    def test_factory_crea_factura_B(self):
        data = {
            "cliente": "María López",
            "tipo": "consumidor_final",
            "productos": [
                {"descripcion": "Monitor", "cantidad": 1, "precio_unitario": 500.0}
            ]
        }
        with open(self.temp_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        factura = crear_factura(self.temp_json, data["tipo"])
        self.assertIsInstance(factura, FacturaB)

    # ===========================================================
    # TEST 2: Template Method ejecuta sin errores
    # ===========================================================
    def test_generar_factura_A(self):
        data = {
            "cliente": "Juan Pérez",
            "tipo": "responsable_inscripto",
            "productos": [
                {"descripcion": "Mouse", "cantidad": 2, "precio_unitario": 50.0}
            ]
        }
        with open(self.temp_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        factura = crear_factura(self.temp_json, data["tipo"])
        try:
            factura.generar_factura()  # no debe lanzar excepciones
        except Exception as e:
            self.fail(f"generar_factura lanzó una excepción inesperada: {e}")

    def test_generar_factura_B(self):
        data = {
            "cliente": "María López",
            "tipo": "consumidor_final",
            "productos": [
                {"descripcion": "Teclado", "cantidad": 1, "precio_unitario": 120.0}
            ]
        }
        with open(self.temp_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        factura = crear_factura(self.temp_json, data["tipo"])
        try:
            factura.generar_factura()
        except Exception as e:
            self.fail(f"generar_factura lanzó una excepción inesperada: {e}")


if __name__ == "__main__":
    unittest.main()