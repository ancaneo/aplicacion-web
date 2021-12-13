from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import requests
import os

app = FastAPI()
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