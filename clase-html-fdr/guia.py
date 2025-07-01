import subprocess
import os
import sys

# Ruta del ejecutable portable (relativa al script)
ruta_script = os.path.dirname(os.path.abspath(sys.argv[0]))
ruta_portable = os.path.join(ruta_script, 'webopener-portable', 'WebOpener.exe')

# Ejecutar el programa
subprocess.Popen(ruta_portable, shell=True)