# main.py
import os
import json
from factura.factura_factory import crear_factura

def main():
    print("=== Generando facturas automáticamente desde JSON ===\n")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "orden.json")

    # Leer lista de facturas
    with open(json_path, "r", encoding="utf-8") as f:
        facturas_data = json.load(f)

    # Recorrer cada objeto de la lista
    for i, data in enumerate(facturas_data, start=1):
        tipo_cliente = data.get("tipo")
        print(f"\n--- Procesando factura #{i} ({tipo_cliente}) ---\n")

        # Crear archivo temporal por cada factura
        temp_path = os.path.join(base_dir, "temp_factura.json")
        with open(temp_path, "w", encoding="utf-8") as tmp:
            json.dump(data, tmp, indent=4)

        factura = crear_factura(temp_path, tipo_cliente)
        factura.generar_factura()

if __name__ == "__main__":
    main()