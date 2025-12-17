from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, database
from ..crud import client_crud

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

get_db = database.get_db

@router.get("/", response_model=List[schemas.ClientResponse])
def get_clients(db: Session = Depends(get_db), limit: int = 100, skip: int = 0):
    clients = client_crud.get_clients(db, limit, skip)
    return clients

@router.get("/{client_id}", response_model=schemas.ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = client_crud.get_client_by_id(db, client_id)

    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

@router.post("/", response_model=schemas.ClientResponse, status_code=status.HTTP_201_CREATED)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return client_crud.create_client(db, client)

@router.put("/{client_id}", response_model=schemas.ClientResponse)
def update_client(client_id: int, client_data: schemas.ClientCreate, db: Session = Depends(get_db)):
    client = client_crud.update_client(db, client_id, client_data)
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    success = client_crud.delete_client(db, client_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return None

@router.put("/{client_id}/recharge", response_model=schemas.ClientResponse)
def recharge_client(client_id: int, recharge: schemas.ClienteRecharge, db: Session = Depends(get_db)):
    client = client_crud.add_cash(db, client_id, recharge.amount)
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client


