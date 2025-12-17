from fastapi import APIRouter, status, Depends
from typing import List

from sqlalchemy.orm import Session
from .. import database, schemas
from ..services import transaction_service
from ..crud import transaction_crud



router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

get_db = database.get_db

@router.post("/buy", status_code=status.HTTP_200_OK)
def buy_product(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return transaction_service.process_purchase(db, transaction)

@router.get("/history", response_model=List[schemas.OrderResponse])
def get_transaction_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = transaction_crud.get_transactions(db, limit, skip)
    return transactions