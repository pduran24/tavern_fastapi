from fastapi import FastAPI
from app import models, database
from app.routers import product_router, client_router, transaction_router, chat_router

# Todo lo que herede de Base en models.py se convertirá en tablas en la base de datos automáticamente
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(product_router.router)
app.include_router(client_router.router)
app.include_router(transaction_router.router)
app.include_router(chat_router.router)

@app.get("/")
def read_root():
    return {"Base de datos": "Bienvenido al Dragón Verde"}