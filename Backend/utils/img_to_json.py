import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import logging
import re

load_dotenv()


def extract_json_from_text(text):
    """
    Extrae y limpia el JSON de la respuesta del modelo.
    Maneja múltiples formatos de respuesta.
    """
    try:
        # Intentar parsear directamente
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Buscar JSON entre bloques de código markdown
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except json.JSONDecodeError:
            pass

    # Buscar el primer objeto JSON válido en el texto
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except json.JSONDecodeError:
            pass

    # Intentar limpiar líneas de markdown (quitar primera y última línea)
    lines = text.splitlines()
    if len(lines) > 2:
        cleaned_text = "\n".join(lines[1:-1])
        try:
            return json.loads(cleaned_text)
        except json.JSONDecodeError:
            pass

    # Si todo falla, lanzar error
    raise json.JSONDecodeError(
        "No se pudo extraer JSON válido de la respuesta", text, 0
    )


def process_image_to_json(image_path):

    api_key = os.getenv("API_KEY")

    if not api_key:
        logging.error("API_KEY no encontrada en el archivo .env.")
        return

    # Configurar API
    genai.configure(api_key=api_key)

    try:
        # Subir la imagen a través de la API de Gemini
        uploaded_file = genai.upload_file(
            path=image_path, display_name=os.path.basename(image_path)
        )
        logging.info(
            f"Archivo subido '{uploaded_file.display_name}' con URI: {uploaded_file.uri}"
        )
        model = genai.GenerativeModel(model_name="gemini-flash-latest")  # Alias al modelo más reciente
        prompt = """
Analiza la imagen de la boleta y extrae toda la información para convertirla en un JSON con la siguiente estructura UTF-8:

{
    "cliente": {
        "fecha": "dd/mm/yy",
        "cliente": "NOMBRE DEL CLIENTE",
        "dni": "12345678",
        "ruc": "10123456789",
        "telefono": "987654321"
    },
    "productos": [
        {
            "cantidad": 10.5,
            "unidad_medida": "KILOGRAMO",
            "descripcion": "DESCRIPCION DEL PRODUCTO",
            "precio_base": 25.50,
            "igv": 1,
            "precio_total": 30.08
        }
    ],
    "total": 150.75
}

INSTRUCCIONES PARA EXTRAER LA INFORMACIÓN:

1. DATOS DEL CLIENTE (pueden aparecer en cualquier parte de la boleta, superior o inferior):
   - Busca etiquetas como: "Sr:", "Sra:", "Cliente:", "Señor:", "Señora:", o nombres directos
   - DNI: Busca "DNI:", "D.N.I:", o números de 8 dígitos precedidos por estas etiquetas
   - RUC: Busca "RUC:" o números de 11 dígitos que comiencen con "10"
   - Teléfono: Busca "Tel:", "Teléfono:", "Celular:", "Cel:" o números de 9 dígitos
   - Fecha: Busca "Fecha:", formatos dd/mm/yy, dd/mm/yyyy, o fechas escritas

2. PRODUCTOS:
   - Cantidad: Número que indica cuántas unidades (puede ser entero o decimal)
   - Unidad de medida (identifica la unidad exacta que aparece en la boleta):
     * "CAJA" - Para productos empaquetados en cajas
     * "KILOGRAMO" - Para menestras y productos vendidos por peso (frijoles, lentejas, garbanzos, arvejas, etc.)
     * "BOLSA" - Para productos empaquetados en bolsas
     * "UNIDAD" - Para productos vendidos por unidad individual
     * Si aparece otra unidad de medida, úsala tal como aparece en MAYÚSCULAS
   - Descripción: Nombre completo del producto
   - Precio base: Precio unitario o base antes de IGV (si está disponible)
   - IGV: 
     * 0 para menestras peruanas (NO incluyen IGV)
     * 1 para otros productos que incluyen IGV
   - Precio total: Precio total del producto (cantidad × precio unitario)

3. TOTAL: Suma total a pagar por todos los productos

REGLAS IMPORTANTES:
- Convierte TODOS los textos a MAYÚSCULAS
- Si un campo opcional no está presente, usa valores vacíos según el tipo:
  * String: ""
  * Números (int/float): 0
  * NO uses "None" o "null"
- Usa los valores EXACTOS que aparecen en la imagen
- El orden de la información puede variar, busca en toda la imagen
- Asegúrate de que el JSON sea válido y esté bien formado
- Responde ÚNICAMENTE con el JSON, sin texto adicional antes o después
"""

        # Realizar la solicitud al modelo con la imagen y el prompt
        response = model.generate_content([uploaded_file, prompt])

        # Extraer y limpiar el JSON de la respuesta
        try:
            python_obj = extract_json_from_text(response.text)
            logging.info("Objeto JSON convertido exitosamente")
            return json.dumps(python_obj, indent=4, ensure_ascii=False)

        except json.JSONDecodeError as e:
            logging.error("Error al convertir la respuesta en JSON: %s", e)
            logging.debug("Respuesta cruda del modelo: %s", response.text)
            return None

    except Exception as e:
        logging.error(f"Error al procesar la imagen: {e}")
        return None


def process_pdf_to_json(pdf_path):
    # Cargar variables de entorno
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        logging.error("API_KEY no encontrada en el archivo .env.")
        return None

    # Configurar API
    genai.configure(api_key=api_key)

    try:
        logging.info(f"Enviando PDF '{pdf_path}' a Gemini...")
        uploaded_file = genai.upload_file(
            path=pdf_path, display_name=os.path.basename(pdf_path)
        )
        logging.info(f"PDF subido correctamente: {uploaded_file.uri}")

        # Procesar el PDF con el prompt dado
        model = genai.GenerativeModel("gemini-flash-latest")  # Alias al modelo más reciente
        prompt_text = """
Analiza el PDF de la boleta y extrae toda la información para convertirla en un JSON con la siguiente estructura UTF-8:

{
    "cliente": {
        "fecha": "dd/mm/yy",
        "cliente": "NOMBRE DEL CLIENTE",
        "dni": "12345678",
        "ruc": "10123456789",
        "telefono": "987654321"
    },
    "productos": [
        {
            "cantidad": 10.5,
            "unidad_medida": "KILOGRAMO",
            "descripcion": "DESCRIPCION DEL PRODUCTO",
            "precio_base": 25.50,
            "igv": 1,
            "precio_total": 30.08
        }
    ],
    "total": 150.75
}

INSTRUCCIONES PARA EXTRAER LA INFORMACIÓN:

1. DATOS DEL CLIENTE (pueden aparecer en cualquier parte de la boleta, superior o inferior):
   - Busca etiquetas como: "Sr:", "Sra:", "Cliente:", "Señor:", "Señora:", o nombres directos
   - DNI: Busca "DNI:", "D.N.I:", o números de 8 dígitos precedidos por estas etiquetas
   - RUC: Busca "RUC:" o números de 11 dígitos que comiencen con "10"
   - Teléfono: Busca "Tel:", "Teléfono:", "Celular:", "Cel:" o números de 9 dígitos
   - Fecha: Busca "Fecha:", formatos dd/mm/yy, dd/mm/yyyy, o fechas escritas

2. PRODUCTOS:
   - Cantidad: Número que indica cuántas unidades (puede ser entero o decimal)
   - Unidad de medida (identifica la unidad exacta que aparece en la boleta):
     * "CAJA" - Para productos empaquetados en cajas
     * "KILOGRAMO" - Para menestras y productos vendidos por peso (frijoles, lentejas, garbanzos, arvejas, etc.)
     * "BOLSA" - Para productos empaquetados en bolsas
     * "UNIDAD" - Para productos vendidos por unidad individual
     * Si aparece otra unidad de medida, úsala tal como aparece en MAYÚSCULAS
   - Descripción: Nombre completo del producto
   - Precio base: Precio unitario o base antes de IGV (si está disponible)
   - IGV: 
     * 0 para menestras peruanas (NO incluyen IGV)
     * 1 para otros productos que incluyen IGV
   - Precio total: Precio total del producto (cantidad × precio unitario)

3. TOTAL: Suma total a pagar por todos los productos

REGLAS IMPORTANTES:
- Convierte TODOS los textos a MAYÚSCULAS
- Si un campo opcional no está presente, usa valores vacíos según el tipo:
  * String: ""
  * Números (int/float): 0
  * NO uses "None" o "null"
- Usa los valores EXACTOS que aparecen en el PDF
- El orden de la información puede variar, busca en todo el documento
- Asegúrate de que el JSON sea válido y esté bien formado
- Responde ÚNICAMENTE con el JSON, sin texto adicional antes o después
"""

        response = model.generate_content([prompt_text, uploaded_file])

        # Extraer y limpiar el JSON de la respuesta
        try:
            python_obj = extract_json_from_text(response.text)
            logging.info("Objeto JSON convertido exitosamente")
            return json.dumps(python_obj, indent=4, ensure_ascii=False)

        except json.JSONDecodeError as e:
            logging.error("Error al convertir la respuesta en JSON: %s", e)
            logging.debug("Respuesta cruda del modelo: %s", response.text)
            return None

    except Exception as e:
        logging.error(f"Error al procesar el PDF: {e}")
        return None


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)

    prompt = "Extrae todos los datos del PDF y conviértelos a JSON estructurado."
    resultado = process_pdf_to_json(
        "C:\\Users\\jefersson\\Downloads\\___ Factura Electronica - Impresion ___.pdf"
    )

    if resultado:
        print("Resultado:\n", resultado)
    else:
        print("No se obtuvo respuesta.")
