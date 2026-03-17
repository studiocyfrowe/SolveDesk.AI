from api.startup import load_chroma_collection, load_embedding_model
from infrastructure.vector_database.chroma_store import ChromaStore
from infrastructure.embedding.sentence_transformer_provider import SentenceTransformerProvider
from application.services.search_service import SearchService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from infrastructure.auth.jwt_provider import JwtProvider
from infrastructure.data_context.external_api_source import ExternalApiSource
from application.services.data_sync_service import DataSyncService
from application.services.manage_data_service import ManageDataService
from model_pipelines.retraining.train_service import TrainService
from dotenv import load_dotenv
import os

load_dotenv()

_model = None
_collection = None
security = HTTPBearer()
jwt_provider = JwtProvider(secret="supersecret")
ISSUES_URL = os.getenv("ISSUES_URL")

def get_model():
    global _model
    if _model is None:
        _model = load_embedding_model()
    return _model

def get_collection():
    global _collection
    if _collection is None:
        _collection = load_chroma_collection()
    return _collection

def get_search_service():
    embedder = SentenceTransformerProvider(get_model())
    store = ChromaStore(get_collection())
    return SearchService(embedder, store)

def get_current_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail="Brak tokena")
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Niepoprawny schemat tokena")
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Pusty token")
    return token

def get_data_sync_service(token: str = Depends(get_current_token)):
    if not token:
        raise HTTPException(status_code=403, detail="Brak uwierzytelnienia do API")
    
    source = ExternalApiSource(ISSUES_URL, token)
    embedder = SentenceTransformerProvider(get_model())
    store = ChromaStore(get_collection())

    return DataSyncService(source, embedder, store)

def manage_data_service(): 
    embedder = SentenceTransformerProvider(get_model())
    store = ChromaStore(get_collection())

    return ManageDataService(embedder, store)

def get_train_service(token: str = Depends(get_current_token)):
    if not token:
        raise HTTPException(status_code=403, detail="Brak uwierzytelnienia do API")
    
    source = ExternalApiSource(ISSUES_URL, token)
    return TrainService(source, get_model())