import enum
from sqlalchemy import Column, Float, String, Integer, Boolean, Enum, ForeignKey, DateTime
from .database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cash = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)



class ProductType(str, enum.Enum):
    BEBIDA = "Bebida"
    COMIDA = "Comida"
    OTROS = "Otros"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    stock = Column(Integer, default=0)
    category = Column(Enum(ProductType), default=ProductType.BEBIDA, index=True)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    client = relationship("Client")
    product = relationship("Product")


