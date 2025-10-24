# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from factura.factura_factory import crear_factura
import json
import os

app = FastAPI(title="API de Facturación", version="1.0")

# Modelo de entrada con Pydantic
class Producto(BaseModel):
    descripcion: str
    cantidad: int
    precio_unitario: float

class Orden(BaseModel):
    cliente: str
    tipo: str
    productos: list[Producto]


@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Facturación"}


@app.post("/facturar")
def generar_factura(orden: Orden):
    """
    Recibe una orden JSON, detecta el tipo de cliente,
    crea la factura adecuada y devuelve el total.
    """
    try:
        # Guardar temporalmente el JSON recibido
        base_dir = os.path.dirname(os.path.abspath(__file__))
        temp_json = os.path.join(base_dir, "orden_temp.json")

        with open(temp_json, "w", encoding="utf-8") as f:
            json.dump(orden.dict(), f, indent=4)

        # Crear la factura adecuada (Factory Method)
        factura = crear_factura(temp_json, orden.tipo)

        # Ejecutar el proceso completo (Template Method)
        total = factura.generar_factura()

        # Devolver respuesta en JSON
        return {
            "cliente": orden.cliente,
            "tipo_factura": orden.tipo,
            "total_final": total,
            "status": "Factura generada correctamente"
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {e}")