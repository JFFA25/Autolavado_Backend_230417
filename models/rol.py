''''Esta clase permite generar el modelo para los tipos de roles'''
from sqlalchemy import Column, Integer, String, Boolean
from config.db import Base

class Rol(Base):
    '''Modelo para la tabla de roles'''
    __tablename__ = "tbc_roles"
    id = Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(50), unique=True, index=True, nullable=False)