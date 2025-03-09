import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("FASTAPI_ENV", "development")

print(ENV)

if ENV == "production":
    load_dotenv(".env")
    print("Running production environment")
else:
    print("Running development environment")
    load_dotenv(".env.dev", override=True)
    
LLM_HOST = os.getenv("LLM_HOST")
LLM_MODEL = os.getenv("LLM_MODEL")

EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL")
EMBEDDINGS_HOST = os.getenv("EMBEDDINGS_HOST")

CHROMADB_HOST = os.getenv("CHROMADB_HOST")

CHROMADB_PORT = os.getenv("CHROMADB_PORT")

CHROMADB_HOST_PORT = f"http://{CHROMADB_HOST}:{CHROMADB_PORT}"

CHROMADB_COLLECTION_ID = os.getenv("CHROMADB_COLLECTION_ID")

COLLECTION_NAMES = os.getenv("COLLECTION_NAMES").split(",")

CHROMADB_K_DOCUMENTS = os.getenv("CHROMADB_K_DOCUMENTS")