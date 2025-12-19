╔══════════════════════════════════════════════════════════════╗
║         SISTEMA DE BOLETAS Y FACTURAS - VERSIÓN 1.0         ║
║                    Manual de Usuario                         ║
╚══════════════════════════════════════════════════════════════╝

📋 CONTENIDO
═══════════════════════════════════════════════════════════════
1. Instalación
2. Configuración Inicial
3. Primer Uso
4. Funcionalidades Principales
5. Actualizaciones
6. Solución de Problemas
7. Soporte Técnico


1️⃣ INSTALACIÓN
═══════════════════════════════════════════════════════════════

PASO 1: Descomprimir archivos
   • Extrae todos los archivos en una carpeta de tu elección
   • Ejemplo: C:\Programas\SistemaBoletas\

PASO 2: Verificar archivos necesarios
   ✓ SistemaBoletas.exe (ejecutable principal)
   ✓ .env (archivo de configuración)
   ✓ version.json (información de versión)
   ✓ updater.py (sistema de actualizaciones)
   ✓ DataBase/ (carpeta de base de datos)

⚠️ IMPORTANTE: NO muevas ni elimines ningún archivo


2️⃣ CONFIGURACIÓN INICIAL
═══════════════════════════════════════════════════════════════

PASO 1: Configurar API de Google Gemini (OBLIGATORIO)
   
   a) Obtén tu API Key:
      • Visita: https://makersuite.google.com/app/apikey
      • Inicia sesión con tu cuenta de Google
      • Crea una nueva API Key
      • Copia la clave generada

   b) Configura el archivo .env:
      • Abre el archivo ".env" con el Bloc de notas
      • Busca la línea: API_KEY=tu_api_key_aqui
      • Reemplaza "tu_api_key_aqui" con tu clave
      • Ejemplo: API_KEY=AIzaSyABC123XYZ789...
      • Guarda y cierra el archivo

PASO 2: Configurar credenciales SUNAT (OPCIONAL)
   
   Si deseas enviar boletas directamente a SUNAT:
   • Abre el archivo ".env"
   • Completa los campos:
     - TEST_USER_1_NAME (nombre de tu empresa)
     - TEST_USER_1_RUC (RUC de tu empresa)
     - TEST_USER_1_USER (usuario SUNAT)
     - TEST_USER_1_PASSWORD (contraseña SUNAT)
   • Guarda el archivo


3️⃣ PRIMER USO
═══════════════════════════════════════════════════════════════

PASO 1: Iniciar la aplicación
   • Doble clic en "SistemaBoletas.exe"
   • Espera a que cargue la interfaz

PASO 2: Registrar tu empresa (Remitente)
   • Ve a la sección "Remitentes"
   • Haz clic en "Agregar Remitente"
   • Completa los datos:
     - Nombre de la empresa
     - RUC
     - Usuario SUNAT
     - Contraseña SUNAT
   • Guarda

PASO 3: Registrar productos (Opcional)
   • Ve a la sección "Productos"
   • Agrega los productos que vendes frecuentemente
   • Esto agilizará la emisión de boletas

PASO 4: Emitir tu primera boleta
   • Ve a la sección principal
   • Selecciona tu remitente
   • Opción A: Sube una imagen/PDF de la boleta
   • Opción B: Ingresa los datos manualmente
   • Haz clic en "Emitir"


4️⃣ FUNCIONALIDADES PRINCIPALES
═══════════════════════════════════════════════════════════════

📸 PROCESAMIENTO DE IMÁGENES/PDFs
   • Sube una foto o PDF de la boleta
   • La IA extrae automáticamente:
     - Datos del cliente (nombre, DNI, RUC, teléfono)
     - Productos (cantidad, descripción, precios)
     - Totales
   • Revisa y corrige si es necesario
   • Emite la boleta

✍️ INGRESO MANUAL
   • Completa los campos del formulario:
     - Datos del cliente
     - Productos (cantidad, descripción, precio)
     - Tipo de documento (Boleta/Factura)
   • El sistema calcula automáticamente los totales
   • Emite la boleta

👥 GESTIÓN DE CLIENTES
   • Los clientes se guardan automáticamente
   • Autocompletado al escribir el nombre
   • Historial de compras por cliente

📦 GESTIÓN DE PRODUCTOS
   • Crea un catálogo de productos
   • Precios predefinidos
   • Búsqueda rápida con autocompletado

📊 HISTORIAL
   • Consulta todas las boletas emitidas
   • Filtra por fecha, cliente, remitente
   • Exporta reportes

🏢 MÚLTIPLES EMPRESAS
   • Registra varias empresas (remitentes)
   • Cambia entre empresas fácilmente
   • Cada empresa tiene su propio catálogo


5️⃣ ACTUALIZACIONES
═══════════════════════════════════════════════════════════════

VERIFICACIÓN AUTOMÁTICA
   • Al iniciar, el sistema verifica actualizaciones
   • Te notifica si hay una nueva versión disponible

ACTUALIZACIÓN MANUAL
   • Opción 1: Ejecuta "python updater.py"
   • Opción 2: Descarga manualmente desde el servidor

PROCESO DE ACTUALIZACIÓN
   1. El sistema crea un backup automático
   2. Descarga la nueva versión
   3. Instala los archivos actualizados
   4. Reinicia la aplicación

⚠️ IMPORTANTE: 
   • No cierres la aplicación durante la actualización
   • Tus datos NO se perderán (están en la base de datos)


6️⃣ SOLUCIÓN DE PROBLEMAS
═══════════════════════════════════════════════════════════════

❌ "Error: API_KEY no encontrada"
   SOLUCIÓN:
   • Verifica que el archivo .env esté en la misma carpeta
   • Abre .env y verifica que API_KEY esté configurada
   • No debe haber espacios: API_KEY=tu_clave (correcto)
   • No usar comillas: API_KEY="tu_clave" (incorrecto)

❌ "No se puede procesar la imagen"
   SOLUCIÓN:
   • Verifica tu conexión a internet
   • Asegúrate de que la imagen sea legible
   • Intenta con mejor calidad de imagen
   • Verifica que tu API_KEY sea válida

❌ "Error al conectar con SUNAT"
   SOLUCIÓN:
   • Verifica tu conexión a internet
   • Revisa las credenciales en el .env
   • Asegúrate de que tu usuario SUNAT esté activo
   • Verifica que el firewall no bloquee la aplicación

❌ "La aplicación no inicia"
   SOLUCIÓN:
   • Ejecuta desde CMD para ver el error:
     1. Abre CMD (Símbolo del sistema)
     2. Navega a la carpeta: cd C:\ruta\a\SistemaBoletas
     3. Ejecuta: SistemaBoletas.exe
   • Revisa los logs en la carpeta "logs/"
   • Contacta soporte técnico con el archivo de log

❌ "Error en la base de datos"
   SOLUCIÓN:
   • Cierra la aplicación completamente
   • Verifica que la carpeta DataBase/ exista
   • Si persiste, elimina billing_system.db (se creará nuevo)
   • ⚠️ Esto borrará todos los datos

📝 LOGS
   • Los logs se guardan en: logs/boletas_YYYY-MM-DD.log
   • Útiles para diagnosticar problemas
   • Envía el log al soporte técnico si necesitas ayuda


7️⃣ SOPORTE TÉCNICO
═══════════════════════════════════════════════════════════════

📧 Email: tu-email@ejemplo.com
📱 WhatsApp: +51 XXX XXX XXX
🌐 Web: https://tu-sitio-web.com
⏰ Horario: Lunes a Viernes, 9:00 AM - 6:00 PM

Al contactar soporte, ten a mano:
   • Versión del sistema (ver en version.json)
   • Descripción del problema
   • Archivo de log del día del error
   • Captura de pantalla (si aplica)


═══════════════════════════════════════════════════════════════
💡 CONSEJOS Y BUENAS PRÁCTICAS
═══════════════════════════════════════════════════════════════

✓ Haz backup periódico de la carpeta DataBase/
✓ Mantén el sistema actualizado
✓ Usa imágenes de buena calidad para mejor precisión
✓ Revisa siempre los datos antes de emitir
✓ Guarda tus credenciales en un lugar seguro
✓ No compartas tu archivo .env con nadie


═══════════════════════════════════════════════════════════════
                    ¡Gracias por usar nuestro sistema!
═══════════════════════════════════════════════════════════════

Versión: 1.0.0
Fecha: Diciembre 2025
