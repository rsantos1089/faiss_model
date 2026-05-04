
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Cargar el modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

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
consulta = "Me encanta escribir código"
query_vector = model.encode([consulta]).astype('float32')

# Buscar el vector más similar (k=1)
distancia, indice_resultado = index.search(query_vector, k=1)

# 6. Mostrar el resultado
respuesta = frases[indice_resultado[0][0]]
print(f"\n--- Resultado de la Búsqueda ---")
print(f"Consulta: {consulta}")
print(f"Respuesta encontrada: {respuesta}")


