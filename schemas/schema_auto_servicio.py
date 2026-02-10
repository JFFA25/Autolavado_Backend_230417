'''
Docstring for schemas.schema_rol
'''

from pydantic import BaseModel
from datetime import datetime


class Auto_ServicioBase(BaseModel):
    '''Esquema base para los autos de servicio'''
    nombre_auto: str
    estado: bool = True
    fecha_registro: datetime
    fecha_actualizacion: datetime