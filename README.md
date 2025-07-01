# 💻 Programa de Acceso para Alumnos – Jean Marco Vilca

Este repositorio contiene una aplicación educativa diseñada para facilitar el acceso de los alumnos a su entorno de trabajo personalizado, de forma segura y automatizada.

## 📂 Estructura del proyecto

/
├─ iniciar.bat
├─ programa.py
├─ backup-proyecto-clase/
├─ codigo-alumno/
│ └─ codigos.txt
├─ trabajos/
│ └─ 1234/
├─ proyecto-clase/
├─ logs/
│ └─ accesos.txt
├─ vscode-portable/
│ └─ Code.exe


### 🗂️ Descripción de carpetas y archivos

| Carpeta / Archivo             | Descripción                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `iniciar.bat`                | Archivo que puede usarse para ejecutar la aplicación `.exe`                 |
| `programa.py`                | Código fuente en Python con interfaz gráfica (`tkinter`)                    |
| `backup-proyecto-clase/`     | Proyecto base que se copia cada vez que un alumno accede                    |
| `codigo-alumno/codigos.txt`  | Lista de códigos válidos, uno por línea, que habilitan el acceso            |
| `trabajos/`                  | Carpeta donde se crean subcarpetas por código de alumno                     |
| `proyecto-clase/`            | Carpeta temporal donde se copia el proyecto base visible al alumno          |
| `logs/`                      | Registra la fecha y el código de cada acceso exitoso                        |
| `vscode-portable/Code.exe`   | Visual Studio Code portable que se lanza automáticamente con el acceso      |

## 🧩 Funcionamiento del programa

1. El alumno abre la aplicación e ingresa su código.
2. El sistema valida el código desde `codigo-alumno/codigos.txt`.
3. Si el código es válido:
   - Se crea una carpeta personalizada en `trabajos/` (si no existe).
   - Se copia el contenido de `backup-proyecto-clase/` a `proyecto-clase/`.
   - Se abre automáticamente `proyecto-clase/` y Visual Studio Code portable.
   - Se guarda un registro del acceso en `logs/accesos.txt`.

## 🚀 Ejecutar la aplicación

- Puedes abrir la aplicación usando:
  - El archivo `programa.py` (requiere Python instalado).
  - O el archivo `.exe` generado con PyInstaller (opcional).

## 🛠️ Requisitos

- Python 3.x (si se usa el script directamente).
- Windows 10 o superior.
- PyInstaller (solo si deseas compilar el `.exe`):  
  ```bash
  pip install pyinstaller
