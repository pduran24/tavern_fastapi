from sqlalchemy.orm import Session
from .. import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    """
    Crea un nuevo producto en la BD
    """
    # 1. Convertir DTO a Entidad (Modelo DB)
    db_product = models.Product(**product.model_dump())

    # 2. Añadir a la sesión -> persist de Hibernate
    db.add(db_product)

    # 3. Confirmación de cambios
    db.commit()

    # 4. Refrescar para obtener el id
    db.refresh(db_product)

    return db_product


def get_products(db: Session, limit: int = 100, skip: int = 0):
    """
    Devuelve una lista de todos los productos dentro del límite introducido
    """
    return db.query(models.Product).order_by(models.Product.id).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    """
    Devuelve un producto por su id
    """
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_product_by_name(db: Session, product_name: str):
    """
    Devuelve un producto por su nombre
    """
    return db.query(models.Product).filter(models.Product.name == product_name).first()


def update_product(db: Session, product_id: int, product_update: schemas.ProductCreate):
    """
    Actualiza un producto existente
    """
    # 1. Determino si el producto existe
    db_product = get_product_by_id(db, product_id)

    if not db_product:
        return None
    
    # 2. Actualizar campos
    update_data = product_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_product, key, value)

    # 3. Guardar cambios
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):
    """
    Elimina un producto por su id
    """
    db_product = get_product_by_id(db, product_id)

    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    
    return False

def add_amount(db: Session, product_id: int, amount: int):
    db_product = get_product_by_id(db, product_id)

    if not db_product:
        return None
    
    db_product.stock += amount
    db.commit()
    db.refresh(db_product)

    return db_product
