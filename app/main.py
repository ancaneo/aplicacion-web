from typing import Optional, final
from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List
from sqlalchemy.orm import Session
import requests
import os
from .database import SessionLocal, engine
from . import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

'''
app.mount("/resources", StaticFiles(directory="resources"), name="resources")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    get_wildfires()
    return FileResponse("templates/index.html")

@app.get("/wildfires")
def get_wildfires():
    path="resources/wildfires.png"
    if not os.path.exists(path):
        r = requests.get("https://maps.wild-fire.eu/gwis?LAYERS=viirs.hs&FORMAT=image/png&TRANSPARENT=true&SINGLETILE=false&SERVICE=wms&VERSION=1.1.1&REQUEST=GetMap&STYLES=&SRS=EPSG:4326&BBOX=-180.0,-90.0,180.0,90.0&WIDTH=1600&HEIGHT=1200&TIME=2021-12-11/2021-12-12")
        with open(path,'wb') as f:
            f.write(r.content)
    return {'path':path}
'''

@app.get("/disasters", response_model=List[schemas.Disaster])
def get_disasters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_disasters(db, skip, limit)

@app.post("/disasters", response_model=schemas.Disaster)
def create_disaster(disaster: schemas.DisasterCreate, db: Session = Depends(get_db)):
    return crud.create_disaster(db, disaster)

@app.get("/types", response_model=List[schemas.Type])
def get_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_types(db, skip, limit)

@app.post("/types", response_model=schemas.Type)
def create_type(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    return crud.create_type(db, type)