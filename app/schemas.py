from pydantic import BaseModel

class DisasterBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class DisasterCreate(DisasterBase):
    type_id: int

class Disaster(DisasterBase):
    id: int
    type_id: int

    class Config:
        orm_mode = True


class TypeBase(BaseModel):
    name: str
    description: str

class TypeCreate(TypeBase):
    pass

class Type(TypeBase):
    id: int

    class Config:
        orm_mode = True