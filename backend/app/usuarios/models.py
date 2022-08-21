from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Usuarios(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(16), nullable=False)
    hashed_password = Column(String(16), nullable=False)
    nombre = Column(String(32))
    aPaterno = Column(String(32))
    aMaterno = Column(String(32))
    email = Column(String(32)) 
    cargo = Column(String(32))
    nivel_acceso = Column(Integer)
    