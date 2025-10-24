# factura/factura_factory.py
from .factura_A import FacturaA
from .factura_B import FacturaB
from descuentos.student_discount import StudentDiscount
from descuentos.consumer_discount import ConsumerDiscount
from impuestos.iva_21 import IVA21
from impuestos.sin_iva import SinIVA

def crear_factura(json_path, tipo_cliente):
    """
    Crea una instancia de la factura según el tipo de cliente.
    """
    if tipo_cliente == "responsable_inscripto":
        print("→ Tipo de cliente detectado: Responsable Inscripto → Factura A\n")
        return FacturaA(
            json_path=json_path,
            discount_strategy=StudentDiscount(),
            tax_strategy=IVA21()
        )

    elif tipo_cliente == "consumidor_final":
        print("→ Tipo de cliente detectado: Consumidor Final → Factura B\n")
        return FacturaB(
            json_path=json_path,
            discount_strategy=ConsumerDiscount(),
            tax_strategy=SinIVA()
        )

    else:
        raise ValueError(f"Tipo de cliente desconocido: {tipo_cliente}")