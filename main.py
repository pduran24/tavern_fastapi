from fastapi import FastAPI
from app import models, database

# Todo lo que herede de Base en models.py se convertirá en tablas en la base de datos automáticamente
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Base de datos": "Creada correctamente"}