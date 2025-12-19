"""
Sistema de actualización automática para la aplicación.
Verifica si hay nuevas versiones disponibles y las descarga.
"""

import json
import logging
import os
import sys
import urllib.request
import zipfile
import shutil
from pathlib import Path

# URL donde se aloja el archivo de versión en GitHub Pages
#UPDATE_SERVER = "https://jeferssonqe.github.io/sistem_with_scraper_send_sunat/version.json"
UPDATE_SERVER= "http://localhost:8888/version.json"
CURRENT_VERSION_FILE = "version.json"


def get_current_version():
    """Obtiene la versión actual instalada."""
    try:
        if os.path.exists(CURRENT_VERSION_FILE):
            with open(CURRENT_VERSION_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("version", "0.0.0")
    except Exception as e:
        logging.error(f"Error al leer versión actual: {e}")
    return "0.0.0"


def get_latest_version():
    """Consulta la última versión disponible en el servidor."""
    try:
        with urllib.request.urlopen(UPDATE_SERVER, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        logging.error(f"Error al consultar actualizaciones: {e}")
        return None


def compare_versions(current, latest):
    """Compara dos versiones en formato X.Y.Z"""
    current_parts = [int(x) for x in current.split(".")]
    latest_parts = [int(x) for x in latest.split(".")]

    for c, l in zip(current_parts, latest_parts):
        if l > c:
            return True
        elif l < c:
            return False
    return False


def download_update(url, destination):
    """Descarga la actualización desde el servidor."""
    try:
        print(f"📥 Descargando actualización desde {url}...")
        urllib.request.urlretrieve(url, destination)
        print("✅ Descarga completada")
        return True
    except Exception as e:
        logging.error(f"Error al descargar actualización: {e}")
        return False


def install_update(zip_path):
    """Instala la actualización descargada."""
    try:
        print("📦 Instalando actualización...")

        # Crear backup del ejecutable actual
        exe_name = "SistemaBoletas.exe"
        if os.path.exists(exe_name):
            backup_name = f"{exe_name}.backup"
            shutil.copy2(exe_name, backup_name)
            print(f"💾 Backup creado: {backup_name}")

        # Extraer el zip
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(".")

        # Eliminar el zip
        os.remove(zip_path)

        print("✅ Actualización instalada correctamente")
        print("🔄 Reinicia la aplicación para aplicar los cambios")
        return True

    except Exception as e:
        logging.error(f"Error al instalar actualización: {e}")
        # Restaurar backup si existe
        if os.path.exists(f"{exe_name}.backup"):
            shutil.copy2(f"{exe_name}.backup", exe_name)
            print("⚠️  Actualización fallida, backup restaurado")
        return False


def check_for_updates(silent=False):
    """
    Verifica si hay actualizaciones disponibles.
    
    Args:
        silent: Si es True, no muestra mensajes si no hay actualizaciones
    
    Returns:
        dict con información de la actualización o None
    """
    current_version = get_current_version()
    latest_info = get_latest_version()

    if not latest_info:
        if not silent:
            print("❌ No se pudo conectar al servidor de actualizaciones")
        return None

    latest_version = latest_info.get("version", "0.0.0")

    if compare_versions(current_version, latest_version):
        print(f"\n🎉 Nueva versión disponible!")
        print(f"   Versión actual: {current_version}")
        print(f"   Versión nueva: {latest_version}")
        print(f"\n📝 Cambios:")
        for change in latest_info.get("changelog", []):
            print(f"   • {change}")

        return latest_info
    else:
        if not silent:
            print(f"✅ Estás usando la última versión ({current_version})")
        return None


def update_app():
    """Proceso completo de actualización."""
    update_info = check_for_updates()

    if not update_info:
        return False

    # Preguntar al usuario si desea actualizar
    if update_info.get("required", False):
        print("\n⚠️  Esta actualización es OBLIGATORIA")
        response = "s"
    else:
        response = input("\n¿Deseas descargar e instalar la actualización? (s/n): ")

    if response.lower() != "s":
        print("❌ Actualización cancelada")
        return False

    # Descargar actualización
    download_url = update_info.get("download_url")
    if not download_url:
        print("❌ URL de descarga no disponible")
        return False

    zip_path = "update.zip"
    if not download_update(download_url, zip_path):
        return False

    # Instalar actualización
    if install_update(zip_path):
        # Actualizar archivo de versión local
        with open(CURRENT_VERSION_FILE, "w", encoding="utf-8") as f:
            json.dump(update_info, f, indent=2, ensure_ascii=False)
        return True

    return False


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    print("=" * 60)
    print("🔄 Sistema de Actualización - Sistema de Boletas")
    print("=" * 60)

    if "--check" in sys.argv:
        # Solo verificar sin instalar
        check_for_updates()
    else:
        # Verificar e instalar si hay actualizaciones
        update_app()

    print("=" * 60)
