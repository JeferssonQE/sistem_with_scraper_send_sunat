"""
Script para empaquetar la aplicación lista para distribución.
Crea un ZIP con todos los archivos necesarios.
"""

import os
import shutil
import zipfile
from datetime import datetime

# Configuración
APP_NAME = "SistemaBoletas"
VERSION = "1.0.0"
OUTPUT_DIR = "release"


def create_distribution_package():
    """Crea el paquete de distribución completo."""

    print("=" * 70)
    print(f"📦 Empaquetando {APP_NAME} v{VERSION} para distribución")
    print("=" * 70)

    # Crear carpeta de salida
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    package_dir = os.path.join(OUTPUT_DIR, APP_NAME)
    os.makedirs(package_dir)

    # Lista de archivos a incluir
    files_to_include = [
        ("dist/SistemaBoletas.exe", "SistemaBoletas.exe"),
        (".env.example", ".env"),  # Renombrar .env.example a .env
        ("version.json", "version.json"),
        ("updater.py", "updater.py"),
        ("README_USUARIO.txt", "README.txt"),
    ]

    # Copiar archivos
    print("\n📋 Copiando archivos...")
    for source, dest in files_to_include:
        if os.path.exists(source):
            dest_path = os.path.join(package_dir, dest)
            shutil.copy2(source, dest_path)
            print(f"   ✓ {dest}")
        else:
            print(f"   ⚠️  {source} no encontrado (omitido)")

    # Crear carpeta DataBase vacía
    db_dir = os.path.join(package_dir, "DataBase")
    os.makedirs(db_dir, exist_ok=True)
    print(f"   ✓ DataBase/ (carpeta vacía)")

    # Crear carpeta logs vacía
    logs_dir = os.path.join(package_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    print(f"   ✓ logs/ (carpeta vacía)")

    # Crear archivo .gitkeep para mantener las carpetas en git
    with open(os.path.join(db_dir, ".gitkeep"), "w") as f:
        f.write("")
    with open(os.path.join(logs_dir, ".gitkeep"), "w") as f:
        f.write("")

    # Crear ZIP
    zip_filename = f"{APP_NAME}_v{VERSION}_{datetime.now().strftime('%Y%m%d')}.zip"
    zip_path = os.path.join(OUTPUT_DIR, zip_filename)

    print(f"\n📦 Creando archivo ZIP: {zip_filename}")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, OUTPUT_DIR)
                zipf.write(file_path, arcname)
                print(f"   ✓ Agregado: {arcname}")

    # Calcular tamaño
    zip_size = os.path.getsize(zip_path) / (1024 * 1024)  # MB

    print("\n" + "=" * 70)
    print("✅ Paquete creado exitosamente!")
    print("=" * 70)
    print(f"\n📍 Ubicación: {zip_path}")
    print(f"📊 Tamaño: {zip_size:.2f} MB")
    print(f"\n📝 Contenido del paquete:")
    print(f"   • {APP_NAME}.exe (ejecutable principal)")
    print(f"   • .env (configuración - DEBE SER EDITADO)")
    print(f"   • version.json (información de versión)")
    print(f"   • updater.py (sistema de actualizaciones)")
    print(f"   • README.txt (manual de usuario)")
    print(f"   • DataBase/ (carpeta para base de datos)")
    print(f"   • logs/ (carpeta para logs)")

    print(f"\n⚠️  IMPORTANTE ANTES DE DISTRIBUIR:")
    print(f"   1. Prueba el ejecutable en una máquina limpia")
    print(f"   2. Verifica que el .env tenga instrucciones claras")
    print(f"   3. Actualiza el README.txt con tu información de contacto")
    print(f"   4. Sube el ZIP a tu servidor de distribución")
    print(f"   5. Actualiza version.json en el servidor de actualizaciones")

    print("\n" + "=" * 70)

    return zip_path


def create_update_package():
    """Crea un paquete solo con los archivos necesarios para actualización."""

    print("\n" + "=" * 70)
    print(f"🔄 Creando paquete de actualización")
    print("=" * 70)

    update_dir = os.path.join(OUTPUT_DIR, "update")
    os.makedirs(update_dir, exist_ok=True)

    # Solo incluir archivos que cambian en actualizaciones
    files_to_include = [
        ("dist/SistemaBoletas.exe", "SistemaBoletas.exe"),
        ("version.json", "version.json"),
    ]

    print("\n📋 Copiando archivos de actualización...")
    for source, dest in files_to_include:
        if os.path.exists(source):
            dest_path = os.path.join(update_dir, dest)
            shutil.copy2(source, dest_path)
            print(f"   ✓ {dest}")

    # Crear ZIP de actualización
    update_zip = f"{APP_NAME}_update_v{VERSION}.zip"
    update_zip_path = os.path.join(OUTPUT_DIR, update_zip)

    print(f"\n📦 Creando ZIP de actualización: {update_zip}")
    with zipfile.ZipFile(update_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(update_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, update_dir)
                zipf.write(file_path, arcname)
                print(f"   ✓ Agregado: {arcname}")

    update_size = os.path.getsize(update_zip_path) / (1024 * 1024)

    print("\n✅ Paquete de actualización creado!")
    print(f"📍 Ubicación: {update_zip_path}")
    print(f"📊 Tamaño: {update_size:.2f} MB")
    print(f"\n📤 Sube este archivo a tu servidor de actualizaciones")
    print(f"🔗 Actualiza la URL en version.json del servidor")

    return update_zip_path


if __name__ == "__main__":
    # Verificar que el ejecutable existe
    if not os.path.exists("dist/SistemaBoletas.exe"):
        print("❌ Error: No se encontró dist/SistemaBoletas.exe")
        print("   Ejecuta primero: python build_exe.py")
        exit(1)

    # Crear paquete completo
    full_package = create_distribution_package()

    # Crear paquete de actualización
    update_package = create_update_package()

    print("\n" + "=" * 70)
    print("🎉 ¡Proceso completado!")
    print("=" * 70)
    print(f"\n📦 Paquetes creados en la carpeta '{OUTPUT_DIR}/':")
    print(f"   1. Paquete completo (para nuevos usuarios)")
    print(f"   2. Paquete de actualización (para usuarios existentes)")
    print("\n✅ Listo para distribución")
    print("=" * 70)
