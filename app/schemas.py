from pydantic import BaseModel
from .models import ProductType
from typing import Optional


# 1. Cliente base -> campos compartidos comunes (para crear y leer)
class ClientBase(BaseModel):
    name: str
    cash: float = 0.0
    is_active: bool = True

# 2. Cliente para crear -> hereda de ClientBase
class ClientCreate(ClientBase):
    pass

# 3. Cliente para leer -> hereda de ClientBase y agrega id (devolver los datos al usuario)
class ClientResponse(ClientBase):
    id: int

    # Configuración para que Pydantic funcione con ORM (SQLAlchemy)
    class Config:
        from_attributes = True
        

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: int = 0
    category: ProductType = ProductType.BEBIDA

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        from_attributes = True

