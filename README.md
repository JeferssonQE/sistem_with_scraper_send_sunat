# Sistema de Facturación Automatizada

Sistema de escritorio para la emisión automatizada de boletas y facturas electrónicas con envío directo a SUNAT mediante web scraping e inteligencia artificial.

[Ver Demo](#demo)

## Descripción

El proceso manual de emitir boletas y facturas electrónicas, calcular el IGV y subirlas al sistema de SUNAT es lento y repetitivo. Este sistema automatiza todo el flujo mediante:

- **Extracción inteligente de datos**: Procesa imágenes o PDFs de comprobantes usando IA para extraer automáticamente la información
- **Validación de datos**: Valida campos obligatorios y cálculos de IGV usando Pydantic
- **Búsqueda fuzzy**: Encuentra productos similares aunque haya errores de escritura
- **Envío automatizado**: Sube los comprobantes directamente a SUNAT mediante Selenium
- **Gestión completa**: Administra remitentes, productos, clientes e historial de ventas

## 🚀 Funcionalidades

- **Procesamiento automático**: Carga imágenes o PDFs de comprobantes y extrae los datos automáticamente
- **Búsqueda inteligente**: Encuentra productos similares usando algoritmos de coincidencia aproximada (RapidFuzz)
- **Gestión de catálogo**: Administra productos con precios, unidades de medida e IGV por remitente
- **Multi-remitente**: Soporta múltiples empresas emisoras con sus propias credenciales de SUNAT
- **Envío a SUNAT**: Automatiza el proceso de carga de comprobantes al sistema oficial
- **Historial de ventas**: Consulta boletas y facturas emitidas con detalles completos
- **Base de datos local**: Almacena toda la información en SQLite sin necesidad de servidor

## Tecnologías

- **Python 3.11+** - Lenguaje principal
- **PyQt5** - Interfaz gráfica de escritorio
- **Selenium** - Automatización del sistema SUNAT
- **Pydantic** - Validación de datos y modelos
- **RapidFuzz** - Búsqueda difusa de productos
- **SQLite** - Base de datos embebida
- **Matplotlib** - Gráficos y reportes
- **Google Generative AI** - Extracción de datos de imágenes/PDFs

## Requisitos

- Python 3.11.1 o superior
- pip (gestor de paquetes de Python)
- Credenciales de SUNAT (usuario y contraseña SOL)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

2. Crear y activar entorno virtual (recomendado):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno (opcional):
Crear archivo `.env` con las credenciales de prueba si es necesario.

## Uso

### Iniciar la aplicación
```bash
python main.py
```

### Modo administrador de base de datos
```bash
python main.py --admin
```

### Flujo de trabajo típico

1. **Configurar remitente**: Ir a Gestión > Remitentes y agregar la empresa emisora con sus credenciales de SUNAT
2. **Agregar productos**: Ir a Gestión > Productos y crear el catálogo de productos con precios e IGV
3. **Seleccionar remitente**: En la pantalla principal, elegir el remitente activo
4. **Cargar comprobante**: 
   - Opción 1: Subir imagen/PDF y dejar que la IA extraiga los datos
   - Opción 2: Llenar manualmente los campos del cliente y productos
5. **Revisar y emitir**: Verificar los datos y hacer clic en "Emitir"
6. **Consultar historial**: Ver boletas emitidas en Historial > Ver historial del remitente

<a name="demo"></a>
## Demo

### Demostración del flujo completo
![Demo](demo/demo.gif)

### Interfaz de usuario
![UI](demo/ui_show.gif)

## Estructura del Proyecto

```
├── Backend/              # Lógica de negocio
│   ├── BoletaController.py   # Controlador principal
│   ├── models.py             # Modelos Pydantic
│   └── utils/                # Utilidades (procesamiento IA)
├── DataBase/             # Capa de datos
│   ├── DatabaseManager.py    # Gestor de SQLite
│   └── billing_system.db     # Base de datos
├── Frontend/             # Interfaz gráfica
│   ├── ui_main.py            # Ventana principal
│   ├── views/                # Vistas de componentes
│   └── dialogs/              # Diálogos modales
├── Scraping/             # Automatización SUNAT
│   └── scraper_sunat.py      # Script de Selenium
├── logs/                 # Archivos de log
└── main.py               # Punto de entrada
```

## Características Técnicas

- **Arquitectura MVC**: Separación clara entre Backend, Frontend y DataBase
- **Validación robusta**: Modelos Pydantic con validaciones personalizadas
- **Búsqueda fuzzy**: Algoritmo WRatio de RapidFuzz con umbral de 60% de similitud
- **Procesamiento asíncrono**: Uso de QThreads para operaciones pesadas sin bloquear la UI
- **Logging completo**: Registro detallado de operaciones en archivos diarios
- **Caché inteligente**: Almacenamiento en memoria de productos y clientes para búsquedas rápidas

## Mejoras Futuras

- Integración con API oficial de facturación electrónica de SUNAT
- Exportación de reportes a Excel y Google Sheets
- Sistema de autenticación con roles (administrador, contador, usuario)
- Respaldos automáticos programados de la base de datos
- Modo multiusuario con sincronización en red
- Generación de reportes estadísticos avanzados
- Soporte para notas de crédito y débito

## Autor

**Jefersson Quicaña Erquinio**

## Licencia

Este proyecto es de uso educativo y demostrativo.
