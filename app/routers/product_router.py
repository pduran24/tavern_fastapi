from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, database
from ..crud import product_crud

# 1. Mapear el router
router = APIRouter(
    prefix="/products", # Todas las rutas empezarán por products
    tags=["products"] # Lo agrupa de manera elegante en la documentación
)

# 2. Inyección de dependencia
get_db = database.get_db

# ---------------------------
# GET ALL
@router.get("/", response_model=List[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db), limit: int = 100, skip: int = 0):
    products = product_crud.get_products(db, limit, skip)
    return products

# GET ONE
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product( product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


# CREATE
@router.post("/", response_model= schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    if product_crud.get_product_by_name(db, product.name):
        raise HTTPException(status_code=409, detail="Dicho producto ya existe")
    return product_crud.create_product(db, product)


# UPDATE
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = product_crud.update_product(db, product_id, product)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


# DELETE
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    success = product_crud.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None
