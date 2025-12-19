# 🚀 Guía de Despliegue - Sistema de Boletas

## 📋 Requisitos Previos

1. Python 3.10 o superior instalado
2. Todas las dependencias instaladas: `pip install -r requeriments.txt`
3. Archivo `.env` configurado con las credenciales necesarias

## 🔨 Crear el Ejecutable

### Opción 1: Usando el script automatizado (Recomendado)

```bash
python build_exe.py
```

Este script:
- Limpia builds anteriores
- Crea un ejecutable optimizado
- Incluye todos los archivos necesarios
- Genera el archivo en `dist/SistemaBoletas.exe`

### Opción 2: Manual con PyInstaller

```bash
pyinstaller --name=SistemaBoletas --onefile --windowed --clean main.py
```

## 📦 Preparar el Paquete de Distribución

Crea una carpeta con los siguientes archivos:

```
SistemaBoletas/
├── SistemaBoletas.exe          # Ejecutable principal
├── .env                         # Configuración (IMPORTANTE)
├── version.json                 # Información de versión
├── updater.py                   # Sistema de actualización
├── README.txt                   # Instrucciones para el usuario
└── DataBase/
    └── billing_system.db        # Base de datos (se crea automáticamente)
```

### Crear el archivo README.txt para el usuario:

```
SISTEMA DE BOLETAS - INSTRUCCIONES DE USO

1. INSTALACIÓN:
   - Descomprime todos los archivos en una carpeta
   - NO muevas el archivo .env ni la carpeta DataBase

2. CONFIGURACIÓN INICIAL:
   - Abre el archivo .env con un editor de texto
   - Configura tu API_KEY de Google Gemini
   - Configura las credenciales de SUNAT si es necesario

3. PRIMER USO:
   - Ejecuta SistemaBoletas.exe
   - Registra tu información como remitente
   - Comienza a emitir boletas

4. ACTUALIZACIONES:
   - El sistema verificará automáticamente si hay actualizaciones
   - También puedes ejecutar: python updater.py

5. SOPORTE:
   - Email: tu-email@ejemplo.com
   - Teléfono: +51 XXX XXX XXX

6. LOGS:
   - Los logs se guardan en la carpeta "logs/"
   - Útiles para diagnosticar problemas
```

## 🌐 Configurar Servidor de Actualizaciones

### 1. Preparar el servidor

Necesitas un servidor web (puede ser GitHub Releases, Dropbox, Google Drive, o tu propio servidor) donde alojar:

```
https://tu-servidor.com/updates/
├── version.json                          # Información de la última versión
└── SistemaBoletas_v1.0.0.zip            # Paquete de actualización
```

### 2. Actualizar version.json en el servidor

Cada vez que lances una nueva versión, actualiza este archivo:

```json
{
  "version": "1.0.1",
  "release_date": "2025-12-20",
  "changelog": [
    "Corrección de errores en procesamiento de PDFs",
    "Mejora en la interfaz de usuario",
    "Optimización de rendimiento"
  ],
  "download_url": "https://tu-servidor.com/updates/SistemaBoletas_v1.0.1.zip",
  "required": false
}
```

### 3. Crear el paquete ZIP de actualización

```bash
# Comprimir los archivos necesarios
zip -r SistemaBoletas_v1.0.1.zip SistemaBoletas.exe version.json updater.py
```

## 🔄 Proceso de Actualización

### Para el desarrollador:

1. **Hacer cambios en el código**
2. **Actualizar version.json local** con la nueva versión
3. **Crear nuevo ejecutable**: `python build_exe.py`
4. **Crear ZIP de actualización**:
   ```bash
   zip -r SistemaBoletas_v1.0.1.zip SistemaBoletas.exe version.json
   ```
5. **Subir al servidor**:
   - Subir el ZIP
   - Actualizar version.json en el servidor
6. **Notificar a los usuarios** (opcional)

### Para el usuario final:

**Opción A: Automática (al iniciar la app)**
- La app verifica automáticamente al iniciar
- Si hay actualización, pregunta si desea instalar
- Descarga e instala automáticamente

**Opción B: Manual**
```bash
python updater.py
```

## 🐛 Depuración en Producción

### 1. Logs

Los logs se guardan automáticamente en `logs/boletas_YYYY-MM-DD.log`

Para revisar errores:
```bash
# Ver últimas líneas del log de hoy
tail -n 50 logs/boletas_2025-12-18.log

# Buscar errores
grep "ERROR" logs/boletas_2025-12-18.log
```

### 2. Modo Debug Remoto

Agrega al inicio de `main.py`:

```python
# Habilitar logging detallado
logging.basicConfig(level=logging.DEBUG)
```

### 3. Recopilar información del usuario

Pide al usuario que te envíe:
- El archivo de log del día del error
- Captura de pantalla del error
- Pasos para reproducir el problema

### 4. Hotfix Rápido

Para correcciones urgentes:

1. Corrige el error
2. Incrementa solo el último número de versión (1.0.0 → 1.0.1)
3. Marca como `"required": true` en version.json
4. Despliega inmediatamente

## 📊 Monitoreo

### Opcional: Sistema de telemetría

Puedes agregar un sistema simple de telemetría para saber cuántos usuarios tienen qué versión:

```python
# En main.py, al iniciar
def send_telemetry():
    try:
        version = get_current_version()
        requests.post(
            "https://tu-servidor.com/telemetry",
            json={"version": version, "timestamp": datetime.now().isoformat()},
            timeout=5
        )
    except:
        pass  # No bloquear si falla
```

## 🔒 Seguridad

1. **NO incluyas credenciales en el ejecutable**
   - Siempre usa el archivo .env
   - Nunca hagas commit del .env al repositorio

2. **Firma el ejecutable** (opcional pero recomendado)
   - Usa un certificado de firma de código
   - Evita advertencias de Windows SmartScreen

3. **Encripta datos sensibles**
   - Contraseñas en la base de datos
   - Credenciales de API

## 📝 Checklist de Despliegue

- [ ] Código probado y funcionando
- [ ] version.json actualizado
- [ ] Ejecutable creado con `build_exe.py`
- [ ] Archivo .env de ejemplo incluido
- [ ] README.txt para el usuario creado
- [ ] Paquete ZIP creado
- [ ] Subido al servidor de actualizaciones
- [ ] version.json del servidor actualizado
- [ ] Probado el proceso de actualización
- [ ] Documentación actualizada
- [ ] Usuarios notificados (si aplica)

## 🆘 Solución de Problemas Comunes

### "El ejecutable no inicia"
- Verifica que el .env esté en la misma carpeta
- Revisa los logs en la carpeta logs/
- Ejecuta desde CMD para ver errores: `SistemaBoletas.exe`

### "Error de API_KEY"
- Verifica que el .env tenga la API_KEY correcta
- Asegúrate de que no haya espacios extra

### "No se puede conectar a SUNAT"
- Verifica la conexión a internet
- Revisa las credenciales en el .env
- Verifica que el firewall no bloquee la app

### "La actualización falla"
- Verifica la conexión a internet
- Asegúrate de que el servidor esté accesible
- Revisa los permisos de escritura en la carpeta

## 📞 Soporte

Para problemas o dudas:
- Email: tu-email@ejemplo.com
- Teléfono: +51 XXX XXX XXX
- GitHub Issues: https://github.com/tu-usuario/tu-repo/issues
