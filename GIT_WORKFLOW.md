# Workflow de Git para el Proyecto

## ✅ Archivos que DEBES subir al repositorio

### Código Fuente
```
Backend/
├── BoletaController.py
├── models.py
├── utils/
└── __init__.py

DataBase/
├── DatabaseManager.py
├── admin_bd.py
└── __init__.py

Frontend/
├── ui_main.py
├── views/
├── dialogs/
└── utils/

Scraping/
└── scraper_sunat.py

utils/
```

### Scripts de Build y Deploy
```
build_exe.py
package_for_distribution.py
updater.py
migrate_database.py
deploy.bat
```

### Configuración
```
.env.example          # ✅ Plantilla sin credenciales
.gitignore
requeriments.txt
version.json          # ✅ Información de versión
```

### Documentación
```
README.md
README_USUARIO.txt
DEPLOYMENT.md
QUICK_START.md
GUIA_PRUEBA_CONTADOR.md
GUIA_ACTUALIZACIONES.md
RESUMEN_DESPLIEGUE.md
ESTRUCTURA_PROYECTO.txt
LOGICA NEGOCIO.txt
COMANDOS_RAPIDOS.txt
```

### Recursos
```
icono.ico
demo/                 # GIFs de demostración
```

### Tests (si existen)
```
Backend/tests/
DataBase/tests/
```

## ❌ Archivos que NO debes subir

### Generados por Build
```
build/               # Archivos temporales de PyInstaller
dist/                # Ejecutables compilados
release/             # Paquetes ZIP para distribución
*.spec               # Generado automáticamente
```

### Datos Locales
```
.env                 # ⚠️ Contiene credenciales
*.db                 # Bases de datos con información
logs/                # Logs de ejecución
```

### Entornos y Caché
```
venv/                # Entorno virtual
__pycache__/         # Cache de Python
*.pyc, *.pyo         # Bytecode compilado
```

### Temporales
```
*.tmp
*.backup
*.log
test_update_server/  # Servidor de prueba local
```

## 📦 Workflow de Release

### 1. Desarrollo Local
```bash
# Trabajar en tu rama
git checkout -b feature/nueva-funcionalidad

# Hacer cambios
# ... editar código ...

# Commit
git add .
git commit -m "feat: descripción del cambio"
```

### 2. Preparar Nueva Versión
```bash
# Actualizar versión en:
# - version.json
# - build_exe.py (VERSION = "X.Y.Z")

# Construir
python build_exe.py
python package_for_distribution.py
```

### 3. Subir Código al Repo
```bash
# Push del código fuente
git push origin feature/nueva-funcionalidad

# Crear Pull Request y merge a main
```

### 4. Crear Release en GitHub

#### A. Subir ejecutables
1. Ve a GitHub → Releases → "Create a new release"
2. Tag: `vX.Y.Z` (ejemplo: `v1.0.1`)
3. Title: `Sistema de Boletas vX.Y.Z`
4. Descripción: Copia el changelog de `version.json`
5. Sube archivos:
   - `release/SistemaBoletas_vX.Y.Z_YYYYMMDD.zip` (paquete completo)
   - `release/SistemaBoletas_update_vX.Y.Z.zip` (solo actualización)
6. Publica el release

#### B. Actualizar GitHub Pages (para auto-updates)
```bash
# Cambiar a rama gh-pages
git checkout gh-pages

# Copiar version.json actualizado
git checkout main -- version.json

# Commit y push
git add version.json
git commit -m "Update version to X.Y.Z"
git push origin gh-pages

# Volver a main
git checkout main
```

## 🔄 Comandos Útiles

### Ver qué archivos se subirán
```bash
git status
git diff
```

### Ver qué archivos están siendo ignorados
```bash
git status --ignored
```

### Verificar antes de commit
```bash
# Ver cambios
git diff

# Ver archivos staged
git diff --cached
```

### Limpiar archivos no rastreados
```bash
# Ver qué se eliminará
git clean -n

# Eliminar archivos no rastreados
git clean -f

# Eliminar también directorios
git clean -fd
```

## 📋 Checklist antes de Push

- [ ] `.env` NO está en el commit (verificar con `git status`)
- [ ] `build/`, `dist/`, `release/` NO están en el commit
- [ ] `version.json` está actualizado con la nueva versión
- [ ] `requeriments.txt` está actualizado si agregaste dependencias
- [ ] `.env.example` tiene todas las variables necesarias (sin valores reales)
- [ ] Documentación actualizada si hay cambios importantes
- [ ] Tests pasan (si existen)

## 🚨 Si subiste .env por error

```bash
# Remover del staging
git reset HEAD .env

# Remover del historial (si ya hiciste commit)
git rm --cached .env
git commit -m "Remove .env from repository"

# Cambiar todas las credenciales expuestas
# ⚠️ Las credenciales en .env están comprometidas
```

## 📝 Convenciones de Commit

```
feat: Nueva funcionalidad
fix: Corrección de bug
docs: Cambios en documentación
style: Formato, punto y coma faltante, etc
refactor: Refactorización de código
test: Agregar tests
chore: Mantenimiento, actualizar dependencias
```

Ejemplos:
```bash
git commit -m "feat: agregar validación de RUC en formulario"
git commit -m "fix: corregir error al crear base de datos"
git commit -m "docs: actualizar guía de instalación"
```
