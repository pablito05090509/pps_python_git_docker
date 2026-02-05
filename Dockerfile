# Fase base
FROM python:3.11-slim AS base
WORKDIR /app

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Ejecutar la app
CMD ["python", "app.py"]
