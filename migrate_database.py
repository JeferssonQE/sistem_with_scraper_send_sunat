"""
Script para migrar la base de datos y agregar la columna telefono
"""

import sqlite3
import os

def migrate_database():
    """Agrega la columna telefono a la tabla clients si no existe"""
    
    # Ruta a la base de datos
    db_path = os.path.join("DataBase", "billing_system.db")
    
    if not os.path.exists(db_path):
        print(f"❌ No se encontró la base de datos en: {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Verificar si la columna ya existe
        cursor.execute("PRAGMA table_info(clients)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'telefono' in columns:
            print("✅ La columna 'telefono' ya existe en la tabla clients")
        else:
            print("📝 Agregando columna 'telefono' a la tabla clients...")
            cursor.execute("ALTER TABLE clients ADD COLUMN telefono TEXT")
            conn.commit()
            print("✅ Columna 'telefono' agregada exitosamente")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error al migrar la base de datos: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("🔄 Migración de Base de Datos - Sistema de Boletas")
    print("=" * 60)
    print()
    
    if migrate_database():
        print()
        print("=" * 60)
        print("✅ Migración completada exitosamente")
        print("=" * 60)
    else:
        print()
        print("=" * 60)
        print("❌ Migración fallida")
        print("=" * 60)
