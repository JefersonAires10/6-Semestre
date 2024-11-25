from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import xml.etree.ElementTree as ET
import os

app = FastAPI()

xml_FILE = "livros.xml"

class Livro (BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    genero: str

def read_xml():
    livros = []
    if os.path.exists(xml_FILE):
        try:
            tree = ET.parse(xml_FILE)
            root = tree.getroot()
            for livro in root:
                livros.append(Livro(**livro.attrib))
        except ET.ParseError:
            pass
    return livros

def write_xml(livros):
    root = ET.Element("livros")
    for livro in livros:
        livro_attrib = {k: str(v) for k, v in livro.dict().items()}
        ET.SubElement(root, "livro", livro_attrib)
    tree = ET.ElementTree(root)
    tree.write(xml_FILE)

@app.get("/ping")
def read_root():
    return {"message": "pong"}

@app.get("/livros/", response_model=list[Livro])
def get_livros():
    return read_xml()

@app.get("/livros/{livro_id}", response_model=Livro)
def get_livro(livro_id: int):
    livros = read_xml()
    for livro in livros:
        if livro.id == livro_id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/livros/", response_model=Livro)
def create_livro(livro: Livro):
    livros = read_xml()
    for l in livros:
        if l.id == livro.id:
            raise HTTPException(status_code=400, detail="Livro com este ID já existe")
    livros.append(livro)
    write_xml(livros)
    return livro

@app.put("/livros/{livro_id}", response_model=Livro)
def update_livro(livro_id: int, livro: Livro):
    livros = read_xml()
    for i, l in enumerate(livros):
        if l.id == livro_id:
            livros[i] = livro
            write_xml(livros)
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{livro_id}", response_model=Livro)
def delete_livro(livro_id: int):
    livros = read_xml()
    for i, l in enumerate(livros):
        if l.id == livro_id:
            livro = livros.pop(i)
            write_xml(livros)
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

