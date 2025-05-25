from sqlalchemy import Column, Integer, String, Float, Enum, TIMESTAMP, func
from app.core.database import Base
import enum

class StatusEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    max_kw = Column(Float, nullable=False)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.inactivo)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(),
                        onupdate=func.now(), nullable=False)
