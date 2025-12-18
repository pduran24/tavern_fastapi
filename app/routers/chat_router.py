from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..services import ai_service


router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

get_db = database.get_db

@router.post("/", response_model=schemas.ChatResponse)
def chat_tavern(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    ai_reply = ai_service.get_tavern_response(request.history, db)

    return {"response": ai_reply}
