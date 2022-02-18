from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import requests
import os
from PIL import Image
from utils.transforms import create_mercator_transformer

app = FastAPI()
app.mount("/resources", StaticFiles(directory="resources"), name="resources")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    get_wildfires()
    return FileResponse("templates/index.html")


@app.get("/wildfires")
def get_wildfires():
    path = "resources/wildfires.png"
    if not os.path.exists(path):
        path = "https://maps.wild-fire.eu/gwis?LAYERS0LES=&SRS=EPSG:4326&BBOX=-180.0,-90.0,180.0,90.0&WIDTH=1600&HEIGHT=1200&TIME=2021-12-11/2021-12-12"
        requests.get(path)

    with Image.open(path) as img:
        array_of_coordinates = []

        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))

                if pixel[0] >= 100:
                    array_of_coordinates.append((x, y))

        transformer = create_mercator_transformer(img.width)
        return {"coords": transformer(array_of_coordinates)}

    return {"coords": []}
