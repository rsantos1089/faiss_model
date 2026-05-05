# Buscador Semántico con FAISS y FastAPI

Este proyecto implementa un motor de búsqueda semántica utilizando el modelo `all-MiniLM-L6-v2` y la biblioteca FAISS para indexación vectorial de alta velocidad.

## 🚀 Pasos para la instalación y ejecución

### Requisitos previos
* Docker instalado
* Python 3.11

### Ejecución con Docker (Recomendado)
1. **Construir la imagen:**
   ```bash
   docker build -t faiss-fastapi .
   ```

2. **Ejecutar el contenedor:**
   ```bash
   docker run -it --rm faiss-fastapi
   ```

3. **Probar la API:**

   `Tipear la consulta deseada `


4. **Terminar ejecucion**

    Tipear `exit`

## 🛠️ Estructura del Proyecto
* `app.py`: Servidor FastAPI con lógica de búsqueda y persistencia.
* `data.json`: Fuente de datos para las frases.
* `vector_index.faiss`: Archivo donde se guarda el índice (se genera automáticamente).
