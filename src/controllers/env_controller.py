from src.config.environment import CHROMADB_HOST , CHROMADB_PORT , CHROMADB_K_DOCUMENTS , LLM_HOST , LLM_MODEL , EMBEDDINGS_HOST , EMBEDDINGS_MODEL , COLLECTION_NAMES
class EnvController:
    def __init__(self):
        pass

    async def get_env(self):
        return {
            "CHROMADB_HOST": CHROMADB_HOST,
            "CHROMADB_PORT": CHROMADB_PORT,
            "CHROMADB_K_DOCUMENTS": CHROMADB_K_DOCUMENTS,
            "LLM_HOST": LLM_HOST,
            "LLM_MODEL": LLM_MODEL,
            "EMBEDDINGS_HOST": EMBEDDINGS_HOST,
            "EMBEDDINGS_MODEL": EMBEDDINGS_MODEL,
            "COLLECTION_NAMES": COLLECTION_NAMES,
        }