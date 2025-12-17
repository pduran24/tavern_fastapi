from sqlalchemy.orm import Session
from .. import models, schemas

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client

def get_clients(db: Session, limit: int = 100, skip: int = 0):
    return db.query(models.Client).order_by(models.Client.id).offset(skip).limit(limit).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id) .first()

def update_client(db: Session, client_id: int, client_update: schemas.ClientCreate):
    db_client = get_client_by_id(db, client_id)

    if not db_client:
        return None
    
    update_data = client_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_client, key, value)

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client_by_id(db, client_id)

    if db_client:
        db.delete(db_client)
        db.commit()
        return True
    
    return False
