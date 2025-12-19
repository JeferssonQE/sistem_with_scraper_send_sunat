"""
Script para crear el ejecutable de la aplicación de boletas.
Ejecutar: python build_exe.py
"""

import PyInstaller.__main__
import os
import shutil

# Configuración
APP_NAME = "SistemaBoletas"
VERSION = "1.0.1"
ICON_PATH = "icono.ico"  

# Limpiar builds anteriores
try:
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
except PermissionError:
    print("⚠️  No se pudo limpiar carpetas anteriores.")
    print("   Cierra el ejecutable si está abierto e intenta de nuevo.")
    print("   O elimina manualmente las carpetas 'dist' y 'build'")
    input("\nPresiona Enter para continuar de todas formas...")

# Argumentos para PyInstaller
args = [
    "main.py",
    "--name=" + APP_NAME,
    "--onefile",  # Un solo archivo ejecutable
    "--windowed",  # Sin consola (para apps GUI)
    "--clean",
    # Incluir archivos de datos
    "--add-data=.env;.",
    "--add-data=DataBase;DataBase",
    # Hooks ocultos necesarios
    "--hidden-import=PyQt5",
    "--hidden-import=google.generativeai",
    "--hidden-import=selenium",
    "--hidden-import=selenium.webdriver",
    "--hidden-import=selenium.webdriver.chrome.service",
    "--hidden-import=selenium.webdriver.chrome.options",
    "--hidden-import=webdriver_manager",
    "--hidden-import=webdriver_manager.chrome",
    "--hidden-import=rapidfuzz",
    "--hidden-import=pydantic",
    "--hidden-import=dotenv",
    # Incluir matplotlib y numpy (necesarios para estadísticas)
    "--hidden-import=matplotlib",
    "--hidden-import=matplotlib.pyplot",
    "--hidden-import=matplotlib.backends.backend_qt5agg",
    "--hidden-import=numpy",
    # Runtime hook para Pydantic V2
    "--runtime-hook=pyi_rth_pydantic.py",
    # Excluir módulos innecesarios para reducir tamaño
    "--exclude-module=pandas",
    "--exclude-module=pytest",
    "--exclude-module=black",
    "--exclude-module=pylint",
]

# Agregar icono si existe
if os.path.exists(ICON_PATH):
    args.append(f"--icon={ICON_PATH}")

print(f"🚀 Construyendo {APP_NAME} v{VERSION}...")
print("=" * 60)

# Ejecutar PyInstaller
PyInstaller.__main__.run(args)

print("=" * 60)
print(f"✅ Ejecutable creado en: dist/{APP_NAME}.exe")

# Crear base de datos limpia en dist/
print("\n📝 Creando base de datos limpia...")
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from DataBase.DatabaseManager import DatabaseManager

dist_db_dir = os.path.join("dist", "DataBase")
os.makedirs(dist_db_dir, exist_ok=True)

dist_db_path = os.path.join(dist_db_dir, "billing_system.db")
if os.path.exists(dist_db_path):
    os.remove(dist_db_path)

db = DatabaseManager(dist_db_path)
db.create_tables()
db.close()

print(f"✅ Base de datos limpia creada en: {dist_db_path}")

print("\n📦 Archivos a distribuir:")
print(f"   - dist/{APP_NAME}.exe")
print(f"   - dist/DataBase/billing_system.db (base de datos limpia)")
print("   - .env (configuración)")
print("\n⚠️  IMPORTANTE:")
print("   1. Copia el archivo .env junto al ejecutable")
print("   2. La base de datos ya está lista en dist/DataBase/")
print("   3. Configura las credenciales en el .env")
