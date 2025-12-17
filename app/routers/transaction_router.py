from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from services import transaction_service

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

get_db = database.get_db

@router.get("/buy", status_code=status.HTTP_200_OK)
def buy_product(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return transaction_service.process_purchase(db, transaction)