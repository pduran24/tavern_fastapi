from sqlalchemy import Column, Float, String, Integer, Boolean
from .database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cash = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
