# Guía del Sistema de Actualizaciones

## Cómo Funciona

El sistema verifica automáticamente si hay nuevas versiones disponibles comparando:
- **Versión local**: `version.json` en la carpeta de la aplicación
- **Versión remota**: `https://jeferssonqe.github.io/sistem_with_scraper_send_sunat/version.json`

## Prueba Local (Sin GitHub)

### 1. Preparar versión antigua
```cmd
cd dist
echo {"version": "1.0.0"} > version.json
```

### 2. Modificar temporalmente updater.py
Cambia la línea 18:
```python
UPDATE_SERVER = "http://localhost:8888/version.json"
```

### 3. Iniciar servidor local
```cmd
python test_updater.py
```

### 4. Probar actualización
En otra terminal:
```cmd
cd dist
python ..\updater.py
```

## Prueba Real (Con GitHub)

### 1. Construir nueva versión
```cmd
python build_exe.py
python package_for_distribution.py
```

### 2. Subir a GitHub

#### A. Crear Release
1. Ve a tu repositorio en GitHub
2. Click en "Releases" → "Create a new release"
3. Tag: `v1.0.1`
4. Title: `Sistema de Boletas v1.0.1`
5. Sube el archivo: `release/SistemaBoletas_update_v1.0.1.zip`
6. Publica el release

#### B. Actualizar GitHub Pages
1. Copia `version.json` a tu rama de GitHub Pages
2. Commit y push:
```cmd
git checkout gh-pages
copy version.json .
git add version.json
git commit -m "Update to v1.0.1"
git push
```

### 3. Probar desde una instalación antigua
```cmd
cd dist
REM Simular versión antigua
echo {"version": "1.0.0"} > version.json

REM Probar actualización
python ..\updater.py
```

## Flujo de Actualización para Usuarios

Los usuarios pueden actualizar de 3 formas:

### 1. Automática al iniciar
La app verifica actualizaciones al iniciar (silenciosamente)

### 2. Manual con updater.py
```cmd
python updater.py
```

### 3. Solo verificar (sin instalar)
```cmd
python updater.py --check
```

## Estructura de version.json

```json
{
  "version": "1.0.1",
  "release_date": "2025-12-19",
  "changelog": [
    "Cambio 1",
    "Cambio 2"
  ],
  "download_url": "https://github.com/USER/REPO/releases/download/v1.0.1/update.zip",
  "required": false
}
```

- `required: true` → Actualización obligatoria
- `required: false` → Usuario puede cancelar

## Troubleshooting

### Error: No se puede conectar al servidor
- Verifica que GitHub Pages esté activo
- Verifica la URL en `UPDATE_SERVER`

### Error: URL de descarga no disponible
- Verifica que el Release esté publicado
- Verifica que el archivo ZIP esté subido

### Error al instalar actualización
- Se restaura automáticamente el backup
- Archivo: `SistemaBoletas.exe.backup`

## Notas Importantes

1. **Backup automático**: Se crea antes de actualizar
2. **Rollback**: Si falla, se restaura la versión anterior
3. **Archivos preservados**: `.env`, `DataBase/`, `logs/` no se sobrescriben
4. **Solo se actualiza**: El ejecutable y `version.json`
