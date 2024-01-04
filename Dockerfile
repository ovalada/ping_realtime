# Imagen de Python como base
FROM python:3.7-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copiar los contenidos del directorio actual al contenedor en /app
COPY . /app

# Instala las dependencias necesarias
RUN apt-get update \
    && apt-get install -y iputils-ping \
    && pip install --no-cache-dir speedtest-cli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expone el puerto 80
EXPOSE 80

# Definir la variable de entorno
ENV SCRIPT RealtimePing

# Ejecutar ping_realtime.py cuando el contenedor se inicia
CMD ["python", "ping_realtime.py"]
