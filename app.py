import sys
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware


# 1. Cargar el modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
# Inicializar FastAPI
app = FastAPI()
# Permitir que cualquier página web consulte tu API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Definir datos de ejemplo
frases = [
    "La inteligencia artificial es fascinante",
    "El clima está muy frío hoy",
    "Me gusta programar en Python",
    "El fútbol es un deporte popular",
    "Las nubes están oscuras"
]

# 3. Generar embeddings y convertir a float32
embeddings = model.encode(frases).astype('float32')

# 4. Construir el índice vectorial con FAISS (IndexFlatL2)
dimension = embeddings.shape[1] # 384 dimensiones
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 5. Realizar una búsqueda semántica
# Capturar consulta (Parámetro o Prompt)
# Endpoint para recibir la consulta desde el navegador
@app.get("/buscar")
def buscar(consulta: str = Query(..., description="Texto a buscar")):
    query_vector = model.encode([consulta]).astype('float32')
    distancia, indice_resultado = index.search(query_vector, k=1)

    respuesta = frases[indice_resultado[0][0]]
    distancia_valor = float(distancia[0][0])

    # Retornar JSON al navegador
    return {
        "consulta": consulta,
        "respuesta": respuesta,
        "distancia": distancia_valor
    }




