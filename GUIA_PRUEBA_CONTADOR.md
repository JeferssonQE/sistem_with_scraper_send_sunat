# 🧪 Guía de Prueba - Sistema de Boletas

## Simular Instalación del Contador

Esta guía te ayuda a probar el sistema como si fueras el contador recibiéndolo por primera vez.

---

## 📦 Paso 1: Extraer el Paquete

El paquete ya está extraído en:
```
C:\Users\jefersson\Desktop\PruebaContador\SistemaBoletas\
```

**Contenido:**
- ✅ `SistemaBoletas.exe` (94 MB)
- ✅ `.env` (configuración)
- ✅ `version.json` (versión)
- ✅ `updater.py` (actualizaciones)
- ✅ `README.txt` (manual)
- ✅ `DataBase/` (carpeta vacía)
- ✅ `logs/` (carpeta vacía)

---

## ⚙️ Paso 2: Configurar el .env

1. **Abre el archivo `.env`** con Bloc de notas:
   ```
   C:\Users\jefersson\Desktop\PruebaContador\SistemaBoletas\.env
   ```

2. **Busca la línea:**
   ```
   API_KEY=tu_api_key_de_google_gemini_aqui
   ```

3. **Reemplaza con tu API Key real:**
   ```
   API_KEY=AIzaSyDO4Yu61G3wgHwAclZplY3JdtfGylQdERQ
   ```
   (O la que uses)

4. **Guarda y cierra**

---

## 🚀 Paso 3: Ejecutar por Primera Vez

1. **Doble clic en:**
   ```
   SistemaBoletas.exe
   ```

2. **Espera a que cargue** (puede tardar 5-10 segundos la primera vez)

3. **Verifica que se abre la ventana principal**

---

## 🧪 Paso 4: Pruebas Básicas

### Prueba 1: Registrar un Remitente

1. Haz clic en **"Seleccionar Remitente"**
2. Haz clic en **"Agregar"**
3. Completa los datos:
   - **Nombre**: EMPRESA DE PRUEBA
   - **RUC**: 20123456789
   - **Usuario**: usuario_prueba
   - **Contraseña**: password123
4. Haz clic en **"Guardar"**
5. **Selecciona el remitente** que acabas de crear

✅ **Resultado esperado**: El remitente aparece seleccionado en la ventana principal

---

### Prueba 2: Agregar un Producto

1. Ve a la pestaña **"Productos"** (si existe) o usa el botón **"Agregar producto"**
2. Completa:
   - **Descripción**: ARROZ SUPERIOR
   - **Unidad**: KILOGRAMO
   - **Precio**: 3.50
   - **IGV**: No (0)
3. Haz clic en **"Agregar"**

✅ **Resultado esperado**: El producto aparece en la lista

---

### Prueba 3: Procesar una Imagen (Opcional)

Si tienes una imagen de boleta:

1. Haz clic en **"Subir Imagen"**
2. Selecciona una imagen de boleta
3. Espera a que procese (5-10 segundos)

✅ **Resultado esperado**: Los datos se llenan automáticamente

---

### Prueba 4: Emitir una Boleta Manual

1. **Completa los datos del cliente:**
   - DNI: 12345678
   - Nombre: CLIENTE DE PRUEBA
   - Teléfono: 987654321

2. **Agrega productos:**
   - Cantidad: 2
   - Unidad: KILOGRAMO
   - Descripción: ARROZ SUPERIOR
   - Precio Base: 3.50
   - IGV: No
   - Precio Total: 7.00

3. **Haz clic en "Emitir"**

4. **Observa:**
   - ¿Se abre Chrome automáticamente?
   - ¿Inicia sesión en SUNAT?
   - ¿Llena el formulario?

✅ **Resultado esperado**: 
- Chrome se abre
- Inicia sesión en SUNAT
- Llena el formulario automáticamente
- Mensaje de éxito

---

### Prueba 5: Verificar Base de Datos

1. **Cierra la aplicación**

2. **Verifica que se creó la base de datos:**
   ```
   C:\Users\jefersson\Desktop\PruebaContador\SistemaBoletas\DataBase\billing_system.db
   ```

3. **Verifica que se crearon logs:**
   ```
   C:\Users\jefersson\Desktop\PruebaContador\SistemaBoletas\logs\boletas_2025-12-19.log
   ```

✅ **Resultado esperado**: Ambos archivos existen

---

### Prueba 6: Verificar Logs

1. **Abre el log más reciente:**
   ```
   C:\Users\jefersson\Desktop\PruebaContador\SistemaBoletas\logs\boletas_2025-12-19.log
   ```

2. **Busca:**
   - "Aplicación iniciada desde"
   - "Boleta validada correctamente"
   - "BOLETA enviado correctamente a sunat"

✅ **Resultado esperado**: No hay errores críticos

---

## 🔄 Paso 5: Probar Actualización (Opcional)

1. **Abre CMD en la carpeta:**
   ```
   cd C:\Users\jefersson\Desktop\PruebaContador\SistemaBoletas
   ```

2. **Ejecuta:**
   ```
   python updater.py --check
   ```

✅ **Resultado esperado**: Muestra la versión actual

---

## ✅ Checklist de Pruebas

Marca lo que funciona:

- [ ] El ejecutable se abre sin errores
- [ ] Se puede registrar un remitente
- [ ] Se puede agregar un producto
- [ ] Se puede procesar una imagen (si tienes una)
- [ ] Se puede emitir una boleta manualmente
- [ ] Chrome se abre automáticamente
- [ ] Se conecta a SUNAT
- [ ] Llena el formulario automáticamente
- [ ] Se guarda en la base de datos
- [ ] Se crean los logs correctamente
- [ ] No hay errores en los logs

---

## 🐛 Problemas Comunes

### "No se puede abrir el ejecutable"
- Verifica que Windows no lo esté bloqueando
- Clic derecho → Propiedades → Desbloquear

### "Error de API_KEY"
- Verifica que el `.env` tenga la API Key correcta
- Sin espacios: `API_KEY=tu_clave` (correcto)
- No usar comillas: `API_KEY="tu_clave"` (incorrecto)

### "Chrome no se abre"
- Verifica que Chrome esté instalado
- Verifica que tengas internet
- Revisa los logs para más detalles

### "Error en la base de datos"
- Ejecuta: `python migrate_database.py`
- Esto agregará la columna `telefono` si falta

---

## 📊 Resultados de la Prueba

**Fecha de prueba**: _________________

**Versión probada**: 1.0.0

**Funciona correctamente**: ☐ Sí  ☐ No

**Problemas encontrados**:
_____________________________________________
_____________________________________________
_____________________________________________

**Notas adicionales**:
_____________________________________________
_____________________________________________
_____________________________________________

---

## 🎯 Siguiente Paso

Si todas las pruebas pasan:
✅ **El sistema está listo para entregar al contador**

Si hay problemas:
❌ **Documenta los errores y corrígelos antes de distribuir**

---

## 📞 Soporte

Si encuentras problemas durante las pruebas:
1. Revisa los logs en `logs/`
2. Documenta el error exacto
3. Incluye capturas de pantalla
4. Contacta al desarrollador

---

**¡Buena suerte con las pruebas!** 🚀
