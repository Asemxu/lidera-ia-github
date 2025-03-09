from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb
from llama_index.core import get_response_synthesizer
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from src.config.environment import LLM_HOST , LLM_MODEL , EMBEDDINGS_MODEL , EMBEDDINGS_HOST , CHROMADB_HOST , CHROMADB_PORT , CHROMADB_K_DOCUMENTS , COLLECTION_NAMES , CHROMADB_HOST_PORT
from src.utils.constants.courses import courses
from llama_index.core.response_synthesizers import ResponseMode
class Config:
    def __init__(self):
        
        self.llm = Ollama(
            base_url=LLM_HOST,
            model=LLM_MODEL,
            request_timeout=60.0,
        )

        self.ollama_embedding = OllamaEmbedding(
            model_name=EMBEDDINGS_MODEL,
            base_url=EMBEDDINGS_HOST,
            ollama_additional_kwargs={"mirostat": 0},
        )
        print(CHROMADB_HOST_PORT)
        self.chroma_client = chromadb.HttpClient(
            host=CHROMADB_HOST,
            port=CHROMADB_PORT,
        )

        self.synthesizer = get_response_synthesizer(
            response_mode=ResponseMode.COMPACT, llm=self.llm
        )

        self.chat_store = SimpleChatStore()

        self.collection_names = COLLECTION_NAMES
        self.courses = courses
        self.indexes = self.create_indexes()
    

    def create_indexes(self):
        indexes = {}
        for collection_name in self.collection_names:
            collection = self.chroma_client.get_collection(collection_name)
        
            vector_store = ChromaVectorStore(
                chroma_collection=collection,
                similarity_top_k=int(CHROMADB_K_DOCUMENTS),
            )
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            indexes[collection_name] = VectorStoreIndex.from_vector_store(
                vector_store,
                storage_context=storage_context,
                embed_model=self.ollama_embedding,
            )
        return indexes

global_config = Config()