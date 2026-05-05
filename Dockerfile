# Usar Python 3 como base
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# Copiar e instalar librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de la aplicación
COPY app.py .

EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
