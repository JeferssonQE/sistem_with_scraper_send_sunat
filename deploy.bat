@echo off
REM ============================================
REM Script de Despliegue Rápido
REM Sistema de Boletas
REM ============================================

echo.
echo ========================================
echo   SISTEMA DE BOLETAS - DESPLIEGUE
echo ========================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado o no esta en el PATH
    echo Por favor instala Python 3.10 o superior
    pause
    exit /b 1
)

echo [1/3] Construyendo ejecutable...
python build_exe.py
if errorlevel 1 (
    echo [ERROR] Fallo al construir el ejecutable
    pause
    exit /b 1
)

echo.
echo [2/3] Creando paquetes de distribucion...
python package_for_distribution.py
if errorlevel 1 (
    echo [ERROR] Fallo al crear paquetes
    pause
    exit /b 1
)

echo.
echo [3/3] Proceso completado!
echo.
echo ========================================
echo   ARCHIVOS LISTOS PARA DISTRIBUCION
echo ========================================
echo.
echo Ubicacion: release\
echo.
echo Paquete completo:
dir /b release\SistemaBoletas_v*.zip 2>nul
echo.
echo Paquete de actualizacion:
dir /b release\SistemaBoletas_update_v*.zip 2>nul
echo.
echo ========================================
echo.
echo Siguiente paso:
echo 1. Sube los archivos a tu servidor
echo 2. Actualiza version.json en el servidor
echo 3. Distribuye al cliente
echo.
echo ========================================
echo.

pause
