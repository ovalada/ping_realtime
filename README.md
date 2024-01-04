# Ping Realtime (Dockerizado)

Esta es una versión Dockerizada de la aplicación Ping Realtime.

## Descripción

La aplicación Ping Realtime proporciona mediciones en tiempo real de la latencia de red y la velocidad de descarga y carga de la conexión a Internet.

## Para Construir la Imagen de Docker

Para construir la imagen de Docker, ejecuta el siguiente comando en la terminal:

```bash
docker build -t ping_realtime .

docker run -it ping_realtime