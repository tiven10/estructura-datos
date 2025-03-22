from typing import Union

from fastapi import FastAPI
from mipa import mostrarEjemplo



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ejemplo")
def ejemplo_paquete():
    retorno = mostrarEjemplo()
    return {"mensaje": retorno}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}