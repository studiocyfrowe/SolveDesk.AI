from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_train_service

router = APIRouter()

@router.post("/train")
async def train_model(service = Depends(get_train_service)):
    try:
        path = service.train()
        return {
            "status": "ok",
            "model_path": path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
