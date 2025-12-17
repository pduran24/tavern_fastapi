from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models, schemas
from crud import client_crud, product_crud


def process_purchase(db: Session, transaction: schemas.TransactionCreate):
    db_product = product_crud.get_product_by_id(db, transaction.product_id)
    db_client = client_crud.get_client_by_id(db, transaction.client_id)

    if not db_product:
        raise HTTPException(status_code=404, detail=f"Producto {db_product.name} no encontrado")
    if not db_client:
        raise HTTPException(status_code=404, detail=f"Cliente {db_client.name} no encontrado")
    
    # Stock
    if db_product.stock < transaction.quantity:
        raise HTTPException(status_code=400, detail=f"No hay suficiente stock (máximo {db_product.stock} )")
    
    # Dinero
    total_price = transaction.quantity * db_product.price
    if db_client.cash < total_price:
        raise HTTPException(status_code=400, detail=f"Saldo insuficiente (total= {total_price} monedas)")

    # Ejecución transacción
    db_product.stock -= transaction.quantity
    db_client.cash -= total_price

    # Persistencia
    db.add(db_product)
    db.add(db_client)
    db.commit()

    db.refresh(db_product)
    db.refresh(db_client)

    return {
        "message": "Compra exitosa",
        "client": db_client.name,
        "new_balance": db_client.cash,
        "product": db_product.name,
        "remaining_stock": db_product.stock
    }

