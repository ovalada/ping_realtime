import subprocess
import time
from queue import Queue
from threading import Thread

# Función para medir la velocidad en segundo plano
def measure_speed():
    while True:
        result = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
        
        # Verificar si la salida tiene el formato esperado
        if len(result.stdout.split("\n")) >= 2:
            download_speed = result.stdout.split("\n")[0].split(":")[1].strip()
            upload_speed = result.stdout.split("\n")[1].split(":")[1].strip()
            speed_queue.put((download_speed, upload_speed))
        else:
            print("Error: No se pudo obtener la velocidad. Verifica la salida de 'speedtest-cli --simple'.")

        time.sleep(1)

# Inicializar las variables
prev_download_speed = ""
prev_upload_speed = ""
speed_queue = Queue()

# Iniciar el hilo para medir la velocidad en segundo plano
speed_thread = Thread(target=measure_speed)
speed_thread.daemon = True
speed_thread.start()

try:
    while True:
        # Realizar una solicitud de ping a google.com y extraer la latencia
        ping_result = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)

        # Verificar si la cadena "time=" está presente en la salida
        if "time=" in ping_result.stdout:
            latency = ping_result.stdout.split("time=")[1].split()[0]

            # Mostrar la latencia en tiempo real
            print(f"Latencia: {latency} ms", end="\r")
        else:
            print("Error: No se pudo obtener la latencia. Verifica la salida de 'ping google.com'.")

        # Obtener la velocidad de descarga y carga desde la cola
        if not speed_queue.empty():
            download_speed, upload_speed = speed_queue.get()
            
            # Actualizar las mediciones anteriores solo si hay cambios
            if download_speed != prev_download_speed or upload_speed != prev_upload_speed:
                # Mostrar los resultados del ancho de banda solo si hay cambios
                print(f"Latencia: {latency} ms  Velocidad de Bajada: {download_speed}  Velocidad de Subida: {upload_speed}", end="\r")

                # Actualizar las mediciones anteriores
                prev_download_speed = download_speed
                prev_upload_speed = upload_speed

        # Dormir durante un segundo antes de la próxima iteración
        time.sleep(1)

except KeyboardInterrupt:
    print("\nSaliendo del script...")
