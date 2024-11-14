from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import os

app = FastAPI()
csv_FILE = "database.csv"

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    quantidade: int

def read_csv():
    produtos = []
    if os.path.exists(csv_FILE):
        with open(csv_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                produtos.append(Produto(**row))
    return produtos

def write_csv(produtos):
    with open(csv_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=Produto.__fields__.keys())
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto.dict())

@app.get("/ping")
def read_root():
    return {"message": "pong"}

@app.get("/produtos/", response_model=list[Produto])
def get_produtos():
    return read_csv()

@app.get("/produtos/{produto_id}", response_model=Produto)
def get_produto(produto_id: int):
    produtos = read_csv()
    for produto in produtos:
        if produto.id == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.post("/produtos/", response_model=Produto)
def create_produto(produto: Produto):
    produtos = read_csv()
    for p in produtos:
        if p.id == produto.id:
            raise HTTPException(status_code=400, detail="Produto com este ID já existe")
    produtos.append(produto)
    write_csv(produtos)
    return produto

@app.put("/produtos/{produto_id}", response_model=Produto)
def update_produto(produto_id: int, produto: Produto):
    produtos = read_csv()
    for i, p in enumerate(produtos):
        if p.id == produto_id:
            produtos[i] = produto
            write_csv(produtos)
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produtos/{produto_id}", response_model=Produto)
def delete_produto(produto_id: int):
    produtos = read_csv()
    for i, p in enumerate(produtos):
        if p.id == produto_id:
            deleted_produto = produtos.pop(i)
            write_csv(produtos)
            return deleted_produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")