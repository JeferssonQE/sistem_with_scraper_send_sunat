"""Archivo principal que lanza la aplicación de boletas con PyQt5."""

from datetime import datetime
import logging
import sys
import os

from PyQt5.QtWidgets import QApplication
from Frontend.ui_main import BoletaApp
from DataBase.admin_bd import modo_consola_sqlite


# Obtener el directorio correcto tanto para desarrollo como para ejecutable
if getattr(sys, 'frozen', False):
    # Ejecutando desde ejecutable
    application_path = os.path.dirname(sys.executable)
else:
    # Ejecutando desde Python
    application_path = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(application_path, "logs")
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"boletas_{datetime.today().date()}.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler()],
)

logging.info(f"Aplicación iniciada desde: {application_path}")
logging.info(f"Log guardado en: {log_file}")


def check_updates_on_startup():
    """Verifica actualizaciones al iniciar la aplicación."""
    try:
        # Importar solo si existe el módulo
        if os.path.exists("updater.py"):
            import updater

            update_info = updater.check_for_updates(silent=True)
            if update_info:
                logging.info(
                    f"Nueva versión disponible: {update_info.get('version')}"
                )
                print(
                    f"\n🎉 Nueva versión {update_info.get('version')} disponible!"
                )
                print("   Ejecuta 'python updater.py' para actualizar\n")
    except Exception as e:
        logging.debug(f"No se pudo verificar actualizaciones: {e}")


def main():
    """Inicializar la app  y usamos un user admin para conexion en BD sqlite"""
    if "--admin" in sys.argv:
        modo_consola_sqlite()
        print("Modo administrador activado.")
    else:
        # Verificar actualizaciones al iniciar
        check_updates_on_startup()

        app = QApplication(sys.argv)
        window = BoletaApp()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error al ejecutar la app", e)
