from typing import Union, List
from fastapi import FastAPI, HTTPExceptiojnv
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    nome: str
    valor: float
    is_oferta: Union[bool, None] = None

# Lista para armazenar os itens
itens: List[Item] = []

@app.get("/ping")
def read_root():
    return {"msg": "pong"}

@app.get("/itens/{item_id}")
def le_item(item_id: int):
    for item in itens:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.put("/itens/{item_id}")
def atualiza_item(item_id: int, item: Item):
    for i, existing_item in enumerate(itens):
        if existing_item.id == item_id:
            itens[i] = item
            return {"msg": "Item atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.post("/itens/")
def cria_item(item: Item):
    itens.append(item)
    return {"msg": "Item criado com sucesso"}

@app.delete("/itens/{item_id}")
def deleta_item(item_id: int):
    for i, item in enumerate(itens):
        if item.id == item_id:
            del itens[i]
            return {"msg": "Item deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.get("/itens/")
def le_itens():
    return itens