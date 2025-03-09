import requests
import time
from functools import lru_cache
from src.config.environment import LLM_HOST , LLM_MODEL , EMBEDDINGS_MODEL , EMBEDDINGS_HOST , CHROMADB_HOST_PORT , CHROMADB_COLLECTION_ID
from src.utils.helpers.chat import format_system_message
from llama_index.core.memory import ChatMemoryBuffer
from src.utils.constants.courses import courses
from src.utils.constants.questions import MAX_TIMEOUT

@lru_cache(maxsize=10000)
def get_chat_response(messages, context):
    print(f"Consultando el modelo con mensajes: {messages}")
    system_prompt = format_system_message(context)
    messages_to_send = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]
    messages_to_send.extend([dict(message) for message in messages])
    data = {
        "model": LLM_MODEL,
        "messages": messages_to_send,
        "stream": False
    }
    start_time = time.time()
    response = requests.post(f"{LLM_HOST}/api/chat", json=data , timeout=MAX_TIMEOUT)
    response = response.json()
    print(data)
    elapsed_time = time.time() - start_time
    print(f"Tiempo de respuesta: {elapsed_time} segundos")
    return response

def get_relevant_documents(embeddings):
    data = { 
        "query_embeddings": [embeddings],
        "n_results": 2,
        "include": ["metadatas"]
    }
    
    response = requests.post(f"{CHROMADB_HOST_PORT}/api/v1/collections/{CHROMADB_COLLECTION_ID}/query", json=data)
    response = response.json()
    return response['metadatas'][0]

async def get_chat_engine(data_source, thread_id,config):
    index = config.indexes[data_source]
    if not index:
        return None
    chat_memory = ChatMemoryBuffer.from_defaults(
        token_limit=3000,
        chat_store=config.chat_store,
        chat_store_key=thread_id,
    )
    chat_engine = index.as_chat_engine(
        chat_mode="condense_plus_context",
        llm=config.llm,
        memory=chat_memory,
        context_prompt=(
            "Eres un asistente academico capaz de tener interacciones normales en castellano \n sobre el curso: "
            f"{courses[data_source]}. \n"
            "A continuación se muestran los documentos relevantes para el contexto:\n"
            "{context_str}"
            "\nInstrucciones: Utiliza el historial de chat anterior, o el contexto anterior, para interactuar y ayudar al usuario. No uses conocimiento previo."
            "Algunas reglas a seguir: \n"
            "1. Nunca hagas referencia directa al contexto dado en tu respuesta.\n"
            "2. Evita afirmaciones como 'Basado en el contexto,...' o 'La información de contexto...' o cualquier cosa por el estilo.\n"
            "3. Siempre responde en castellano.\n"
            "4. Siempre responde amablemente."
            # Cuando tengas mas de una idea, responde en varios parrafos.
        ),
        verbose=True,
    )
    return chat_engine

def generate_embeddings(query: str):
    data = {
        "model": EMBEDDINGS_MODEL,
        "prompt": query
    }

    response = requests.post(f"{EMBEDDINGS_HOST}/api/embeddings", json=data)
    response = response.json()

    return response['embedding']
