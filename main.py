from fastapi import FastAPI
import uvicorn as uv
from api.handlers.auth_handlers import register_auth_handlers
from api.controllers.search_controller import router as search_router
from api.controllers.issue_controller import router as issue_router
from api.controllers.trainer_controller import router as train_router
from api.controllers.explain_controller import router as explain_router

app = FastAPI(
    title="SolveDesk BERT API",
    description="API do inteligentnego wyszukiwania i analizy podobnych zgłoszeń przy użyciu modeli BERT",
    version="1.01.001"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_auth_handlers(app)

app.include_router(search_router, prefix="/api", tags=["Search"])
app.include_router(issue_router, prefix="/api", tags=["Data Sync"])
app.include_router(train_router, prefix="/api", tags=["Train Model"])
app.include_router(explain_router, prefix="/api", tags=["Explain"])

if __name__ == "__main__":
    uv.run("main:app", host="127.0.0.1", port=8000, reload=True)