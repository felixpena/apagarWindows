import subprocess
import time

# Preguntar al usuario en cuántas horas quiere que se apague el PC
horas = float(input("Ingrese en cuántas horas desea apagar el computador: "))

# Convertir horas a segundos
tiempo_espera = int(horas * 60 * 60)

# Iniciar un bucle que dure el tiempo de espera
for i in range(tiempo_espera, 0, -1):
    mins, secs = divmod(i, 60)
    hours, mins = divmod(mins, 60)
    time_left = f"El computador se apagará en {hours} horas, {mins} minutos y {secs} segundos..."
    print(time_left, end='\r', flush=True)
    time.sleep(1)  # Espera un segundo

# Ejecutar el comando para apagar el computador
subprocess.run("shutdown /s /t 1")
