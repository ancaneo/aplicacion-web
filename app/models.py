from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class NaturalDisaster(Base):
    __tablename__ = "NaturalDisaster"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("DisasterType.id"))
    name = Column(String)

    latitude = Column(Numeric)
    longitude = Column(Numeric)

    type = relationship("DisasterType", back_populates="disasters")


class DisasterType(Base):
    __tablename__ = "DisasterType"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    disasters = relationship("NaturalDisaster", back_populates="type")