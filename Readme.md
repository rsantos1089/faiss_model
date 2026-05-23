# Buscador Semántico con FAISS y FastAPI

Este proyecto implementa un motor de búsqueda semántica utilizando el modelo `all-MiniLM-L6-v2` y la biblioteca FAISS para indexación vectorial de alta velocidad.

## 🚀 Pasos para la instalación y ejecución

### Requisitos previos
* Docker instalado
* Python 3.11

### Ejecución con Docker (Recomendado)
1. **Construir la imagen:**
   ```bash
   docker build -t buscador-faiss .
   ```

2. **Ejecutar el contenedor:**
   ```bash
   docker run -p 8000:8000 --name mi_buscador buscador-faiss
   ```

3. **Probar la API:**

   En el navegador ingresar  
   `http://localhost:8000/docs `

![api](/assets/api.png)

4. **Ingresar consulta**

    Tipear `consulta deseada`

## 🛠️ Estructura del Proyecto
* `app.py`: Servidor FastAPI con lógica de búsqueda y persistencia.
* `data.json`: Fuente de datos para las frases.
* `vector_index.faiss`: Archivo donde se guarda el índice (se genera automáticamente).
