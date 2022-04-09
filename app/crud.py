from sqlalchemy.orm import Session
from . import models, schemas

def get_disaster(db: Session, disaster_id: int):
    return db.query(models.NaturalDisaster).filter(models.NaturalDisaster.id == disaster_id).first()

def get_disasters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.NaturalDisaster).offset(skip).limit(limit).all()

def create_disaster(db: Session, disaster: schemas.DisasterCreate):
    db_disaster = models.NaturalDisaster(
        name = disaster.name,
        type_id = disaster.type_id,
        longitude = disaster.longitude, 
        latitude = disaster.latitude
    )
    db.add(db_disaster)
    db.commit()
    db.refresh(db_disaster)
    return db_disaster

def get_types(db: Session, skip: int, limit: int):
    return db.query(models.DisasterType).offset(skip).limit(limit).all()

def create_type(db: Session, type: schemas.TypeCreate):
    db_type = models.DisasterType(
        name = type.name,
        description = type.description,
    )
    db.add(db_type)
    db.commit()
    db.refresh(db_type)

    return db_type