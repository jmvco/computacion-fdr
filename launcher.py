import os
import sys
import time
import shutil
import threading
import subprocess
import ctypes
from colorama import init, Fore, Style

# === Inicializar colorama ===
init(autoreset=True)

# === Establecer tamaño y colores de consola (solo Windows) ===
if os.name == 'nt':
    os.system("mode con: cols=80 lines=30")
    ctypes.windll.kernel32.SetConsoleTitleW("CLASE DE COMPUTACIÓN - ACCESO")

# === Obtener ruta raíz del script o ejecutable ===
script_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__))

# === Rutas importantes ===
ruta_codigos = os.path.join(script_dir, 'codigo-alumno', 'codigos.txt')
ruta_trabajos = os.path.join(script_dir, 'trabajos')
ruta_backup = os.path.join(script_dir, 'backup-proyecto-clase')
ruta_logs = os.path.join(script_dir, 'logs', 'accesos.txt')
ruta_vscode = os.path.join(script_dir, 'vscode-portable', 'Code.exe')
alias = 'proyecto-clase'
ruta_alias = os.path.join(script_dir, alias)

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# === Verificar si existe codigos.txt ===
if not os.path.exists(ruta_codigos):
    print(Fore.RED + '[X] ERROR: No se encontró el archivo de códigos.')
    input('Presione ENTER para salir.')
    sys.exit()

# === Cargar códigos ===
dic_codigos = {}
with open(ruta_codigos, 'r', encoding='utf-8') as file:
    for linea in file:
        partes = linea.strip().split(',')
        if len(partes) == 2:
            dic_codigos[partes[0]] = partes[1]

# === Ingreso de código ===
codigo_valido = False
while not codigo_valido:
    limpiar()
    print(Fore.GREEN + '=' * 60)
    print(Fore.GREEN + '           BIENVENIDO A LA CLASE DE COMPUTACIÓN')
    print(Fore.GREEN + '=' * 60)
    codigo = input(Fore.YELLOW + '>> Ingrese su código de alumno: ').strip()

    if codigo in dic_codigos:
        nombre_alumno = dic_codigos[codigo]
        codigo_valido = True
    else:
        print(Fore.RED + '\n[!] Código incorrecto. Intente de nuevo.')
        time.sleep(2)

# === Mensaje de bienvenida ===
print(Fore.GREEN + f'\n[✔] Bienvenido, {nombre_alumno} (Código: {codigo})')
print(Fore.CYAN + '[~] Preparando entorno de trabajo...')

# === Rutas del alumno ===
ruta_alumno = os.path.join(ruta_trabajos, codigo)

try:
    if not os.path.exists(ruta_alumno):
        print(Fore.CYAN + '[+] Creando carpeta de trabajo del alumno...')
        shutil.copytree(ruta_backup, ruta_alumno)

    os.system(f'attrib -h "{ruta_alumno}"')

    if os.path.exists(ruta_alias):
        shutil.rmtree(ruta_alias)

    shutil.copytree(ruta_alumno, ruta_alias)

except Exception as e:
    print(Fore.RED + f'[X] ERROR al preparar carpeta: {e}')
    input('Presione ENTER para salir.')
    sys.exit()

# === Registrar acceso ===
try:
    os.makedirs(os.path.dirname(ruta_logs), exist_ok=True)
    with open(ruta_logs, 'a', encoding='utf-8') as log:
        log.write(f'{codigo} - {nombre_alumno} - {time.strftime("%Y-%m-%d %H:%M:%S")}\n')
except:
    pass

# === Función para sincronizar cada 5 segundos ===
def sincronizar_cambios_periodicamente():
    while vscode_proc.poll() is None:
        try:
            shutil.copytree(ruta_alias, ruta_alumno, dirs_exist_ok=True)
        except:
            pass
        time.sleep(5)

# === Abrir VSCode ===
print(Fore.CYAN + '[~] Abriendo Visual Studio Code...')
vscode_proc = subprocess.Popen([ruta_vscode, ruta_alias])

# === Hilo de sincronización ===
hilo_sync = threading.Thread(target=sincronizar_cambios_periodicamente)
hilo_sync.start()

# === Esperar que se cierre VSCode ===
vscode_proc.wait()

# === Última sincronización ===
try:
    print(Fore.CYAN + '[~] Guardando cambios finales...')
    shutil.copytree(ruta_alias, ruta_alumno, dirs_exist_ok=True)
except Exception as e:
    print(Fore.RED + f'[X] ERROR al sincronizar: {e}')

# === Limpiar y ocultar ===
try:
    if os.path.exists(ruta_alias):
        shutil.rmtree(ruta_alias)
    os.system(f'attrib +h "{ruta_alumno}"')
except:
    pass

print(Fore.GREEN + '\n[✔] Sesión finalizada. Cambios guardados correctamente.')
time.sleep(2)
sys.exit()
