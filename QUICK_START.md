# 🚀 Inicio Rápido - Despliegue a Producción

## Para el Desarrollador

### 1️⃣ Construir el Ejecutable

```bash
# Instalar dependencias (si no lo has hecho)
pip install -r requeriments.txt

# Construir el ejecutable
python build_exe.py
```

Esto creará `dist/SistemaBoletas.exe`

### 2️⃣ Crear Paquete de Distribución

```bash
# Crear paquetes completos (instalación + actualización)
python package_for_distribution.py
```

Esto creará en la carpeta `release/`:
- `SistemaBoletas_v1.0.0_YYYYMMDD.zip` (paquete completo)
- `SistemaBoletas_update_v1.0.0.zip` (solo actualización)

### 3️⃣ Configurar Servidor de Actualizaciones

**Opción A: GitHub Releases (Gratis y Fácil)**

1. Crea un nuevo Release en GitHub
2. Sube `SistemaBoletas_update_v1.0.0.zip`
3. Copia la URL del archivo
4. Actualiza `version.json`:
   ```json
   {
     "version": "1.0.0",
     "download_url": "https://github.com/tu-usuario/tu-repo/releases/download/v1.0.0/SistemaBoletas_update_v1.0.0.zip"
   }
   ```
5. Sube `version.json` a GitHub Pages o a tu servidor

**Opción B: Dropbox/Google Drive**

1. Sube el ZIP a Dropbox/Drive
2. Obtén el enlace de descarga directa
3. Actualiza `version.json` con la URL
4. Aloja `version.json` en un servidor web

**Opción C: Tu Propio Servidor**

1. Sube ambos archivos a tu servidor:
   - `version.json`
   - `SistemaBoletas_update_v1.0.0.zip`
2. Asegúrate de que sean accesibles vía HTTP/HTTPS

### 4️⃣ Actualizar updater.py

Edita `updater.py` y cambia:
```python
UPDATE_SERVER = "https://tu-servidor.com/updates/version.json"
```

Por la URL real donde alojaste `version.json`

### 5️⃣ Distribuir al Cliente

Envía al contador:
- `SistemaBoletas_v1.0.0_YYYYMMDD.zip` (paquete completo)
- Instrucciones del `README_USUARIO.txt`

---

## Para el Contador (Usuario Final)

### 📥 Instalación

1. **Descomprimir**
   - Extrae el ZIP en una carpeta (ej: `C:\SistemaBoletas\`)

2. **Configurar API Key**
   - Abre el archivo `.env` con Bloc de notas
   - Obtén tu API Key en: https://makersuite.google.com/app/apikey
   - Pega tu API Key en la línea: `API_KEY=tu_clave_aqui`
   - Guarda el archivo

3. **Ejecutar**
   - Doble clic en `SistemaBoletas.exe`
   - ¡Listo!

### 🔄 Actualización

**Automática:**
- Al iniciar, el sistema verifica actualizaciones
- Si hay una nueva versión, te pregunta si deseas instalar

**Manual:**
```bash
python updater.py
```

---

## 🔧 Proceso de Actualización (Desarrollador)

### Cuando corrijas un bug o agregues una feature:

1. **Hacer los cambios en el código**

2. **Actualizar versión**
   ```bash
   # Edita version.json
   # Cambia "1.0.0" a "1.0.1" (o la versión que corresponda)
   ```

3. **Construir nuevo ejecutable**
   ```bash
   python build_exe.py
   ```

4. **Crear paquete de actualización**
   ```bash
   python package_for_distribution.py
   ```

5. **Subir al servidor**
   - Sube `SistemaBoletas_update_v1.0.1.zip`
   - Actualiza `version.json` en el servidor con:
     - Nueva versión
     - Nueva URL de descarga
     - Changelog (qué cambió)

6. **Notificar al cliente** (opcional)
   - Envía un email/WhatsApp
   - O espera a que el sistema notifique automáticamente

---

## 📊 Versionado Semántico

Usa el formato: `MAJOR.MINOR.PATCH`

- **MAJOR** (1.0.0 → 2.0.0): Cambios grandes, incompatibles
- **MINOR** (1.0.0 → 1.1.0): Nuevas funcionalidades
- **PATCH** (1.0.0 → 1.0.1): Corrección de bugs

Ejemplos:
- Bug fix: `1.0.0` → `1.0.1`
- Nueva feature: `1.0.1` → `1.1.0`
- Cambio mayor: `1.1.0` → `2.0.0`

---

## 🐛 Depuración Remota

### Cuando el contador reporte un error:

1. **Pedir el archivo de log**
   - Ubicación: `logs/boletas_YYYY-MM-DD.log`
   - Pedir el log del día que ocurrió el error

2. **Analizar el log**
   ```bash
   # Buscar errores
   grep "ERROR" logs/boletas_2025-12-18.log
   
   # Ver últimas líneas
   tail -n 100 logs/boletas_2025-12-18.log
   ```

3. **Reproducir el error localmente**
   - Usa los mismos datos que el usuario
   - Revisa el log para entender el contexto

4. **Corregir y desplegar**
   - Corrige el bug
   - Incrementa versión PATCH
   - Despliega actualización

### Hotfix Urgente

Si es crítico:
```json
{
  "version": "1.0.2",
  "required": true,  // ← Forzar actualización
  "changelog": ["Corrección urgente de bug crítico"]
}
```

---

## 📝 Checklist de Despliegue

Antes de enviar al cliente:

- [ ] Código probado y funcionando
- [ ] Ejecutable creado (`python build_exe.py`)
- [ ] Paquete de distribución creado
- [ ] `version.json` actualizado
- [ ] `.env.example` tiene instrucciones claras
- [ ] `README_USUARIO.txt` actualizado con tu contacto
- [ ] Servidor de actualizaciones configurado
- [ ] URL en `updater.py` actualizada
- [ ] Probado en máquina limpia (sin Python instalado)
- [ ] Documentación actualizada

---

## 💡 Tips

### Para el Desarrollador:

1. **Mantén un changelog**: Documenta todos los cambios
2. **Versionado consistente**: Sigue semántica de versiones
3. **Backups**: Guarda copias de cada versión desplegada
4. **Testing**: Prueba en Windows limpio antes de distribuir
5. **Logs**: Revisa logs periódicamente para detectar problemas

### Para el Usuario:

1. **Backup regular**: Copia la carpeta `DataBase/` semanalmente
2. **Mantén actualizado**: Acepta las actualizaciones
3. **Imágenes de calidad**: Mejor calidad = mejor precisión
4. **Revisa antes de emitir**: Siempre verifica los datos extraídos

---

## 🆘 Problemas Comunes

### "PyInstaller no encontrado"
```bash
pip install pyinstaller
```

### "El ejecutable es muy grande"
- Normal, incluye Python y todas las librerías
- Tamaño típico: 50-150 MB

### "Windows SmartScreen bloquea el ejecutable"
- Normal para ejecutables sin firma
- Clic en "Más información" → "Ejecutar de todas formas"
- Solución: Firma el ejecutable con certificado de código

### "Error al crear el ejecutable"
```bash
# Limpiar y reintentar
python build_exe.py
```

---

## 📞 Soporte

¿Dudas? Contacta:
- Email: tu-email@ejemplo.com
- WhatsApp: +51 XXX XXX XXX

---

**¡Éxito con tu despliegue! 🎉**
