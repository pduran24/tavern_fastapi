from sqlalchemy.orm import Session
from .. import models, schemas

def get_transactions(db: Session, limit: int = 100, skip: int = 0):
    return db.query(models.Order).order_by(models.Order.id).offset(skip).limit(limit).all()