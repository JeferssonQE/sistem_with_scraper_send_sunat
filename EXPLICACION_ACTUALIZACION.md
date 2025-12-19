# 🔄 Explicación del Sistema de Actualizaciones

## Escenario Real

### Situación Inicial
El contador tiene instalado en su PC:
```
C:\SistemaBoletas\
├── SistemaBoletas.exe    (versión 1.0.0)
├── version.json          (dice "1.0.0")
├── updater.py            (script de actualización)
├── .env                  (sus credenciales de SUNAT)
├── DataBase\
│   └── billing_system.db (sus clientes y boletas)
└── logs\
```

### Tú Lanzas una Nueva Versión (1.0.1)

1. **Haces cambios en el código** (ejemplo: arreglas un bug)
2. **Actualizas version.json**:
   ```json
   {
     "version": "1.0.1",
     "changelog": ["Fix: Bug en cálculo de IGV"],
     "download_url": "https://github.com/TU_USUARIO/TU_REPO/releases/download/v1.0.1/SistemaBoletas_update_v1.0.1.zip"
   }
   ```
3. **Construyes**: `python build_exe.py`
4. **Empaquetas**: `python package_for_distribution.py`
5. **Subes a GitHub**:
   - Release con el ZIP
   - GitHub Pages con version.json actualizado

## 🎯 Cómo el Contador Actualiza

### Método 1: Ejecutar updater.py (Manual)

El contador abre su terminal en `C:\SistemaBoletas\` y ejecuta:

```cmd
python updater.py
```

**Paso a paso de lo que sucede:**

```
1. updater.py lee version.json LOCAL
   → Encuentra: "1.0.0"

2. updater.py consulta GitHub Pages
   → URL: https://jeferssonqe.github.io/sistem_with_scraper_send_sunat/version.json
   → Encuentra: "1.0.1"

3. Compara versiones
   → 1.0.1 > 1.0.0 ✅ HAY ACTUALIZACIÓN

4. Muestra al contador:
   ┌────────────────────────────────────────┐
   │ 🎉 Nueva versión disponible!          │
   │    Versión actual: 1.0.0              │
   │    Versión nueva: 1.0.1               │
   │                                        │
   │ 📝 Cambios:                           │
   │    • Fix: Bug en cálculo de IGV       │
   │                                        │
   │ ¿Deseas actualizar? (s/n):           │
   └────────────────────────────────────────┘

5. Si el contador escribe "s":
   
   a) Crea backup:
      SistemaBoletas.exe → SistemaBoletas.exe.backup
   
   b) Descarga desde GitHub:
      https://github.com/.../SistemaBoletas_update_v1.0.1.zip
      → Guarda como: update.zip
   
   c) Extrae el ZIP:
      update.zip contiene:
      ├── SistemaBoletas.exe  (nuevo, versión 1.0.1)
      └── version.json        (nuevo, dice "1.0.1")
   
   d) Reemplaza archivos:
      ✅ SistemaBoletas.exe → Reemplazado con v1.0.1
      ✅ version.json → Actualizado a "1.0.1"
      ⚠️ .env → NO SE TOCA (preserva credenciales)
      ⚠️ DataBase/ → NO SE TOCA (preserva datos)
      ⚠️ logs/ → NO SE TOCA (preserva logs)
   
   e) Limpia:
      Elimina update.zip
   
   f) Muestra:
      ✅ Actualización instalada correctamente
      🔄 Reinicia la aplicación para aplicar los cambios

6. El contador cierra y vuelve a abrir SistemaBoletas.exe
   → Ahora está usando la versión 1.0.1
   → Sus datos y configuración siguen intactos
```

### Método 2: Automático al Iniciar (Opcional)

En `main.py` ya está implementado:

```python
def check_updates_on_startup():
    """Verifica actualizaciones al iniciar la aplicación."""
    update_info = updater.check_for_updates(silent=True)
    if update_info:
        print(f"\n🎉 Nueva versión {update_info.get('version')} disponible!")
        print("   Ejecuta 'python updater.py' para actualizar\n")
```

Cuando el contador abre `SistemaBoletas.exe`, la app:
1. Verifica silenciosamente si hay actualizaciones
2. Si hay, muestra un mensaje en la consola (si no es --windowed)
3. NO actualiza automáticamente (el usuario decide)

## 📦 Contenido del ZIP de Actualización

El archivo `SistemaBoletas_update_v1.0.1.zip` contiene **SOLO**:

```
SistemaBoletas_update_v1.0.1.zip
├── SistemaBoletas.exe    ← Ejecutable nuevo
└── version.json          ← Versión actualizada
```

**NO incluye:**
- ❌ .env (cada usuario tiene sus propias credenciales)
- ❌ DataBase/ (cada usuario tiene sus propios datos)
- ❌ logs/ (cada usuario tiene sus propios logs)
- ❌ updater.py (ya lo tienen de la instalación inicial)

## 🔐 Seguridad de los Datos

```
ANTES de actualizar:
C:\SistemaBoletas\
├── SistemaBoletas.exe (v1.0.0)
├── .env (credenciales del contador)
└── DataBase\
    └── billing_system.db (100 boletas del contador)

DESPUÉS de actualizar:
C:\SistemaBoletas\
├── SistemaBoletas.exe (v1.0.1) ← ACTUALIZADO
├── SistemaBoletas.exe.backup (v1.0.0) ← BACKUP
├── .env (credenciales del contador) ← INTACTO
└── DataBase\
    └── billing_system.db (100 boletas) ← INTACTO
```

## 🚨 Si Algo Sale Mal

Si la actualización falla, `updater.py` automáticamente:

```python
# Restaurar backup si existe
if os.path.exists(f"{exe_name}.backup"):
    shutil.copy2(f"{exe_name}.backup", exe_name)
    print("⚠️  Actualización fallida, backup restaurado")
```

El contador vuelve a tener su versión 1.0.0 funcionando.

## 📋 Resumen para el Contador

### Primera Instalación (una sola vez)
1. Descargar `SistemaBoletas_v1.0.0_20251219.zip` (paquete completo)
2. Extraer en `C:\SistemaBoletas\`
3. Configurar `.env` con sus credenciales
4. Ejecutar `SistemaBoletas.exe`

### Actualizaciones (cada vez que lances una nueva versión)
1. Abrir terminal en `C:\SistemaBoletas\`
2. Ejecutar: `python updater.py`
3. Escribir "s" para confirmar
4. Reiniciar la aplicación

**¡Eso es todo!** Sus datos y configuración se preservan automáticamente.

## 🎓 Analogía Simple

Piensa en el sistema como una app de celular:

- **GitHub Release** = Google Play Store (donde está el APK)
- **GitHub Pages** = Servidor que dice "hay versión nueva"
- **updater.py** = Botón de "Actualizar" en Play Store
- **SistemaBoletas.exe** = La app instalada
- **.env y DataBase/** = Datos del usuario (no se tocan al actualizar)

Cuando actualizas WhatsApp:
- ✅ La app se actualiza
- ✅ Tus chats siguen ahí
- ✅ Tu configuración sigue ahí

Lo mismo pasa aquí.
